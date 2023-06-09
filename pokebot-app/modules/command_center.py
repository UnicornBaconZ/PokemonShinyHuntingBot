
#############################################################################
## Imports
#############################################################################

import commands

#############################################################################
## Module - Command Center
#############################################################################

COMMANDS = {
    'terminate': commands.terminate
}

def wait_for_command():
    command = input().strip().lower()
    return command

def try_execute_command(command):
    if command_exists(command):
        pass
    else:
        print(f'The command "{command}" does not exist')

def command_exists(command):
    return command in COMMANDS.keys()

