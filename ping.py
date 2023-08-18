#ping servers with python

import subprocess
import platform
import cgi

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command)

host_element = 

print(ping(host))