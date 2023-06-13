
#############################################################################
## Imports
#############################################################################

from cprint import *

from core.configs import settings

#############################################################################
## Module - Command Center
#############################################################################

def wait_for_command():
    cprint.ok('\nEnter a command:')
    command = input().strip().lower()
    return command

def try_execute_command(command):
    if command_exists(command):
        settings.COMMANDS[command]()
    else:
        cprint.err(f'\nThe command "{command}" does not exist')

def command_exists(command):
    return command in settings.COMMANDS.keys()

