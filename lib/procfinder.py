"""Provides methods to work wiht proc fs."""
import glob
import re


class Proc():
    """Provides methods to obtain data from proc FS."""

    def getPids(self):
        """Return list of PIDs in proc fs."""
        pids = []
        for x in glob.glob("/proc/[0-9]*"):
            pids.append(x.rsplit('/', 2)[2])
        return pids

    def getProcName(self, pid):
        """Return proces name for provided PID."""
        self.pid = pid
        try:
            fPath = '/proc/' + str(self.pid) + '/status'
            f = open(fPath)
        except:
            return "NameUnknown"
        name = f.readline().split()[1]
        f.close()
        return name

    def getParrent(self, chpid):
        """"Return pid of parrent for the given process."""
        self.chpid = chpid
        fPath = '/proc/' + str(self.chpid) + '/status'
        try:
            f = open(fPath)
        except:
            return "N/A"
        for x in f.readlines():
            if re.match('^PPid:\s+[0-9]+', x):
                pPid = x.split()[1]
                break
        return pPid

    def getParrentName(self, pPid):
        """Return parrent process name base id parrent pid."""
        self.pPid = pPid
        return self.getProcName(self.pPid)
