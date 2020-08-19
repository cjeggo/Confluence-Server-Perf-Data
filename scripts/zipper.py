import os
import CONFIG as config
import zipfile

# Static logs to collect:
systemCPUlog = 'AtlassianMonitor-systemCPU.log'
pidCPUlog = 'AtlassianMonitor-pidCPU.log'

def filetest():
    flist = []
    for r, d, f in os.walk(config.logLoco):
        for files in f:
            if 'atlassian_system' in files:
                flist.append(os.path.join(files))
        return flist

def filenames():
    test = []
    for item in filetest():
        test.append(item)
        if 'systemCPUlog' in filetest():
            test.append(systemCPUlog)
        else:
            pass
        if 'pidCPUlog' in filetest():
            test.append(pidCPUlog)
    return test

def zipit():
    os.chdir(config.logLoco)
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile("AtlassianMonitorData.zip", mode="w")

    for item in filenames():
        zf.write(config.logLoco + item, item, compress_type=compression)

    print(os.system('ls -ahl | grep AtlassianMonitorData'))