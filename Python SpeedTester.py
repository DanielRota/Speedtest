import os
import sys
import math
import speedtest

def BytesToMbps(size_bytes):
    l = int(math.log(size_bytes, 1024))
    fl = math.floor(l)
    i = int(fl)
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f'{size} Mbps'
  
def Informations(net):
    print('Download speed-rate: ' + (str(BytesToMbps(net.download))))
    print('Upload speed-rate: ' + (str(BytesToMbps(net.upload))))
    #print('Current Address: ' + net.)

def RefreshProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Pings Array
servernames = []

# This Network
net = speedtest.Speedtest()

choise = int(input('''

#1 Get data about local network
#2 Make a ping to server

'''))

if choise == 1:
    print('')
    print('Performing connection...')
    print('')
    Informations(net)

elif choise == 2:
    print('Pinging to server...')
    net.get_servers(servernames)
    print(str(net.results.ping))
    print(net.best.values())

else:
    print('Make another choise please...')
    print("Program is getting refreshed")
    RefreshProgram()

answer = str('Do you want to restart this program? [ y / n ]')

if answer.lower().strip() == 'y':
    RefreshProgram()
  
else:
    print('')
    sys.exit('Exiting program...')