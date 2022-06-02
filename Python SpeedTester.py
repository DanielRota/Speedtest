import os
import sys
import speedtest
import socket

class NetTrend:
  def __init__(self):
    pass
  
  def Define(self, id, download, upload, ip, ping):
    self.id = id
    self.download = download
    self.upload = upload
    self.ip = ip
    self.ping = ping
    
def SingleTest(net):
    value = NetTrend()
    download = net.download()
    upload = net.upload()
    net.get_best_server()
    hostname = socket.gethostname()
    download_mbps = round(download / (10**7), 2)
    upload_mbps = round(upload / (10**7), 2)
    ip_address = socket.gethostbyname(hostname)
    ping = net.results.ping
    value.Define(len(Tests), download_mbps, upload_mbps, ip_address, ping)
    print('Download speed-rate: ' + str(download_mbps) + ' Mbps')
    print('Upload speed-rate: ' + str(upload_mbps) + ' Mbps')
    print('This Hostname: ' + str(hostname))
    print('Current address: ' + str(ip_address))
    print('Ping result: ' + str(ping))
    return value
  
def RefreshProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

print('##############################')
print('# Speedtester by Daniel Rota #')
print('##############################')

Tests = []

def Main():
  if speedtest.Speedtest():
    net = speedtest.Speedtest()
  else:
    sys.exit('Internet is actually unavaible...')

  choise = int(input('''
1) Make a test and ping to server
2) View trend of recent tests
3) Average of download-speed and upload-speed
                     
'''))
    
  if choise == 1:
    value = NetTrend()
    print('')
    print('Performing connection...')
    print('')        
    value = SingleTest(net)
    Tests.append(value)
  elif choise == 2:
    print('')
    for i in Tests:
      print('N°', i.id, ':', i.download, 'Mbps -', i.upload, 'Mbps -', i.ip, '-' , i.ping)
      print('')
    print('Do you want to restart this program? [y/n]')
    answer = str(input())
    if answer.lower().strip() == 'y':
      print('')
      print('--------------------------------------------------')
      Main()
    else:
      print('')
      sys.exit('Exiting program...')
  elif choise == 3:
    if len(Tests) == 0:
      print('')
      print('Actually any value has been registered... make some tests first!')
      print('')
    else:
      sd = 0
      su = 0
      for a in Tests:
        sd = sd + float(a.download)
        su = su + float(a.upload)
      print('')
      print('Average download-speed:', sd / len(Tests)) 
      print('Average upload-speed:', su / len(Tests)) 
  else:
    print('Make another choise please! Restarting program...')
    Main()

Main()
GoOn = True

while(GoOn):
  print('')
  print('Do you want to restart this program? [y/n]')
  answer = str(input())
  if answer.lower().strip() == 'y':
    print('')
    print('--------------------------------------------------')
    Main()  
  else:
    print('')
    sys.exit('Exiting program...')
