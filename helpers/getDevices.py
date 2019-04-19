import sys

def getDevices(args): 
  devices = []
  for index, elem in enumerate(args):
    if elem == 'Name:':
      devices.append(str(args[ index + 1 ]))
  return devices

args = sys.argv

if args[1] == 'show-devices':
  for device in getDevices(args):
    print('- ' + device)
elif args[1] == 'get-devices':
  sys.stdout.write(','.join(getDevices(args)))