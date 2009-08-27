#!/usr/bin/env python

import os
import subprocess
import sys
import tempfile
import time
import uzblctrl

# Start uzbl

sdir = tempfile.mkdtemp()
subprocess.Popen(['sh', '-c', 'echo set socket_dir = %s | uzbl -c -'%sdir])

time.sleep(0.5)
# Could also use -v | grep ^init_socket
socket = os.path.join(sdir,os.listdir(sdir)[0])

ufile = os.path.join(sdir,'pingback')

def u(cmd):
    return uzblctrl.uzblctrl(socket, cmd)

try:
    assert u('js 123') == '123'

finally:
    u('exit')
