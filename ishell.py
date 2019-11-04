#!/usr/bin/env python3
import os 
import getpass

uid = os.getuid()
sign = '#' if uid == 0 else '$'

while(1):
    is_background = False
    my_input = input('ishell' + sign + getpass.getuser() + ': ')

    arguments = my_input.split()
    if not arguments:
        continue
    elif arguments[0] == 'exit':
        print("Bye, have a great day!")
        break
    if arguments[-1] == '&':
        is_background = True
        del arguments[-1] 
    pid = os.fork()
    
    if (pid == 0):
        try:
            exit_code = os.execvp(arguments[0], arguments)
        except FileNotFoundError:
            print("ERROR: command not found")
            continue
        if exit_code !=0:
            print("Something went wrong")
    elif pid < 0:
        print("Forking has failed")
        break
    print(pid)
    if (is_background == True):
        continue
    while True:
        os.waitpid(pid, 0)
        if os.WIFEXITED(0):
            break