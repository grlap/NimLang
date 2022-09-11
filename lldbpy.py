#!/usr/bin/env python3
import sys
import lldb
import optparse
import shlex
import platform

# https://lldb.llvm.org/use/python-reference.html
#
# command:
# script lldbpy.info_nim()

#
#script print(lldb.debugger)
#Debugger (instance: "debugger_1", id: 1)
#script print(lldb.target)
#main
#
#
#

def ls(debugger, command, result, internal_dict):
    print("ls")

# And the initialization code to add your commands
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ls.ls ls')
    print('The "ls" python command has been installed and is ready for use.')

def info_nim():
    print("Python version")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)
    print(platform.python_version())
    print(platform.python_version_tuple())
    print(type(platform.python_version_tuple()))

def nim_lldb():
    print("Python version")
    print (sys.version)

info_nim()