import sys
import CONFIG as config
import scripts.linuxSystemCPU as lindump
import scripts.windowsSystemCPU as windump
import scripts.pidCPU as piddump

runningOS = sys.platform

# Config logic check
if config.highCPU < config.lowCPU:
    print("The 'high CPU value' is lower then the 'low CPU' value. Exiting")
    exit()
elif config.highCPU > 100:
    print("'High CPU' value is greater than 100%. Exiting")
    exit()
else:
    pass

if config.installDir == '':
    print("The application installation directory setting is empty. Exiting")
    exit()
elif config.dataDir == '':
    print("The application data directory setting is empty. Exiting")
    exit()
else:
    pass

if config.componentMon == 'S':
    if runningOS == "linux":
        lindump.logFile()
        lindump.configToLog()
        try:
            lindump.monitor()
            # piddump.monitor()
        except KeyboardInterrupt:
            print(" Stopping....")
            exit()
    elif runningOS == "windows":
        windump.holder()
    else:
        print("Unable to determine OS.")
elif config.componentMon == "P":
    if runningOS == "linux":
        piddump.logFile()
        piddump.configToLog()
        try:
            piddump.monitor()
        except KeyboardInterrupt:
            print(" Stopping....")
            exit()
    elif runningOS == "windows":
        windump.holder()
    else:
        print("Unable to determine OS.")

