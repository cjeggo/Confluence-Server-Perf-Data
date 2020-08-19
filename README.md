**Atlassian Monitor**
====


**What is it?** \
A lightweight CPU monitoring tool which triggers a thread dump on the application PID when a condition is met.
Conditions include:
* System CPU utilization
* More maybe coming soon

**Usage**\
This is written in Python3, which may need to be installed separately. 
The script relies on certain application files being hardcoded, therefore the script must be run from the application installation directory.
If you are unsure, the directory structure looks like this:
```bash
/6.12.0/install_dir$ ls
bin           CONTRIBUTING.md  jre       logs         README.txt       systemThreadDumps.py  work
BUILDING.txt  ha.log.0         lib       NOTICE       RELEASE-NOTES    temp
conf          ha.xml           LICENSE   README.html  RUNNING.txt      uninstall
confluence    install.reg      licenses  README.md    synchrony-proxy  webapps
```
_Syntax:_
```bash
$ python3 <path/to/script>/atlassianMonitor.py
``` 

**Configuration**\
Atlassian Support will pre configure the script for you using the 'CONFIG.py' file. 
You are free to continue to use the scripts in the future. The default values should suffice for most scenarios
 however please do not change the config provided by Support straight away as 
 the parameters may be specific for the problem. 

_Config options_
dataCount = How many rounds of thread dumps and CPU stats do you want? Default = 6


sleepTime = How many seconds between thread dumps? Default = 10


utilLength = For how many seconds should the CPU be high before triggering data collection? Default = 5

highCPU = What CPU utilization %'age is the high water mark i.e. where we start paying attention? Default = 95%

lowCPU = What is the low water mark i.e. it was just a spike so reset? Default = 85%

interval = CPU sample interval, seconds. Default = 1

logLoco = Log location to write the collected data. User must have write access. Default = /tmp

monType = Monitor type. S = one time and exit, R = repeat i.e. constantly run in the background. Case sensitive. Beware logging with R!!
