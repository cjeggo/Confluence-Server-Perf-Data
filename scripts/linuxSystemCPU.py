import os
import socket
import psutil
import time
import datetime
import CONFIG as config
import scripts.zipper as zipper


#################################################################
# Take a thread dump when cpu% at value for iterations. LINUX!! #
#################################################################


# Logging
def logFile():
    try:
        open(config.logLoco + "/atlassian_system_cpu.log", "+a")
    except PermissionError:
        print(config.logLoco + "/atlassian_system_cpu.log already exists but this user does not have write access or this user does not have write permissions to " + config.logLoco)
        exit()
    except FileNotFoundError:
        try:
            with open(config.logLoco + "/atlassian_system_cpu.log", "+w") as f:
                f.close()
        except PermissionError:
            print(config.logLoco + "/atlassian_system_cpu.log already exists but this user does not have write access or this user does not have write permissions to " + config.logLoco)
            exit()

# Write config to log
try:
    f = open(config.logLoco + "/atlassian_system_cpu.log", "+a")
except PermissionError:
    print("ERROR " + config.logLoco + "/atlassian_system_cpu.log already exists but this user does not have write access. Adjust permissions or delete existing file")
    exit()

def configToLog():
    with open(config.logLoco + "/atlassian_system_cpu.log", "+a") as f:
        f.write("############ \n" + "Hostname: " + socket.gethostname() + "\n" + "Script start time: " + str(datetime.datetime.now()) + "\n"
                + "Application PID: " + str(pid()) + "\n" + "CPU High Threshold: " + str(config.highCPU) + "% \n"
                 + "Seconds Over Threshold Before Dump: " + str(config.utilLength) + "\n" + "CPU Low Threshold: " + str(config.lowCPU) + "% \n"
                + "No. Thread Dumps to collect: " + str(config.dataCount) + "\n" + "Seconds Between Thread Dumps: " + str(config.sleepTime) + "\n"
                + "############ \n")

def pidFile():
    installDir = config.installDir
    pwd = os.getcwd()
    filename = "/work/catalina.pid"
    # path = pwd + filename
    path = installDir + filename
    return path

def pid():
    try:
        with open(pidFile()) as f:
            pid = f.read().strip('\n')
            return pid
    except PermissionError:
        return False

def takeDumps():
    # Number of thread dumps and CPU stats to capture
    for x in range(config.dataCount):
        os.system("top -b -H -p " + str(pid()) + " -n1 > " + config.logLoco + "/atlassian_system_cpu_usage.`date +%s`.txt")
        os.system("jstack " + str(pid()) + " > " + config.logLoco+ "/atlassian_system_thread_dump.`date +%s`.txt")
        # Duration between dumps
        time.sleep(config.sleepTime)

def fileList():
    # do an ls on logLoco and grep for conf_ so we know what was collected
    return os.system("ls -al " + config.logLoco + " | grep atlassian_system_")

def monitor():
    i = 0
    with open(config.logLoco + "/atlassian_system_cpu.log", "+a") as f:
        if pid() == False:
            f.write(str(datetime.datetime.now()) + " Unable to read PID file. Please run this as the Confluence user\n")
            print("Unable to read PID file. Please run this as the Confluence user")
            exit()
        else:
            print("Script is running....Ctrl+C to stop")
            # How many times do you want to see the CPU high before dumping
            while i <= config.utilLength:
                cpu_value = psutil.cpu_percent(interval=config.interval, percpu=False)
                # Lower CPU% value to clear counter i.e. clear after spike.
                if cpu_value < config.lowCPU:
                    f.write(str(datetime.datetime.now()) + " System CPU utilization under " + str(config.lowCPU) + "%, resetting counter \n")
                    i = 0
                # CPU% value at which to increment our count, probably 90%
                elif cpu_value > config.highCPU:
                    i += 1
                    f.write(str(datetime.datetime.now()) + ' System CPU utilization at ' + str(cpu_value) + '%. Over threshold ' + str(i) + ' time(s) \n')
                    # f.write(str(datetime.datetime.now()) + str(psutil.cpu_times_percent(interval=1.0, percpu=False)))
                if i == config.utilLength:
                    print(str(datetime.datetime.now()) + " Threshold met! Writing thread dumps to " + config.logLoco)
                    f.write(str(datetime.datetime.now()) + " Threshold met! Dumping to " + config.logLoco + "\n")
                    takeDumps()
                    print("The following files have been generated in " + config.logLoco + ":" )
                    fileList()
                    f.write(str(datetime.datetime.now()) + " Dump complete \n")
                    if config.monType == "R":
                        zipper.zipit()
                        print("Zipping and continuing to monitor \n")
                        monitor()
                    else:
                        print("Exiting")
                        f.write(str(datetime.datetime.now()) + " Single run selected, exiting \n")
                        zipper.zipit()
                        exit()


