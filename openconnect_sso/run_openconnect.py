#!/usr/bin/env python3
"""Just a wrapper script to run openconnect in elevated mode"""
import sys
import subprocess
from elevate import elevate

elevate()
command_line = ['openconnect'] + sys.argv[1:]
subprocess.run(command_line)