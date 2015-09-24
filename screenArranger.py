#list screens
#need wmctrl installed
from subprocess import Popen,PIPE


class windowArranger():
  def __init__(self):
    self.updateWindowInfo() 
  def updateWindowInfo(self):
    cmd = ['wmctrl','-l'] #call window cotrol list
    proc = Popen(cmd,stdout = PIPE)
    rawWindowsList = proc.communicate()[0]#returns string of all open windows
    entries = rawWindowsList.split('\n')#split on new line 
    self.names = [''.join(x.split(' ')[4:]) for x in entries]
    self.windowIds = [x.split(' ')[0] for x in entries]
    
def main():
  wa = windowArranger()
  print wa.names
  print wa.windowIds
main()

#arrange screens

