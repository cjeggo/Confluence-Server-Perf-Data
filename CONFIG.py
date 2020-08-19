########################################################
#              General Configuration                   #
########################################################

# System or PID monitoring. P for PID monitoring, S for System. Case sensitive
componentMon = "P"



########################################################
#               Monitor Configuration                  #
########################################################

# How many rounds of thread dumps and CPU stats do you want? Default = 6
dataCount = 6

# How many seconds between thread dumps? Default = 10
sleepTime = 10

# For how many seconds should the CPU be high before triggering data collection? Default = 5
utilLength = 5

# What CPU utilization %'age is the high water mark i.e. where we start paying attention? Default = 95%
highCPU = 95

# What is the low water mark i.e. it was just a spike so reset? Default = 85%
lowCPU = 85

# CPU sample interval, seconds. Default = 1
interval = 1

# Log location. User must have write access. Linux default = /tmp.
logLoco = "/tmp/"

# Monitor type. S = one time and exit, R = repeat i.e. constantly run in the background. Case sensitive. Beware logging with R!!
monType = "S"


########################################################
#               Application Directories                #
########################################################

# Application install directory
installDir = ''

# Application data directory
dataDir = ''