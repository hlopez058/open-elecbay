import argparse
import os
import subprocess
import time
process = subprocess.Popen(['/usr/sbin/mosquitto', '-c', '/etc/mosquitto/mosquitto.conf'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
time.sleep(5)
