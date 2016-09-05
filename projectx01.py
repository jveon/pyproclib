"""This is a functional file."""
import procfinder

proc = procfinder.Proc()
print('{0:<8s}\t{1:<20s}\t{2:8<s}\t{3:<20s}'.format('PID','Process Name','PPID','Parrent Name'))
for x in proc.getPids():
#   print('{:<{1}s}'.format(x, 8, proc.getProcName(x), proc.getParrent(x), proc.getParrentName(x)))
    x=int(x)
    print('{0:<8d}\t{1:<20s}\t{2:8<d}\t{3:<20s}'.format(x, proc.getProcName(x), int(proc.getParrent(x)), proc.getParrentName(x)))
