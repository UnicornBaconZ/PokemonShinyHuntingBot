
#############################################################################
## Imports
#############################################################################

import sys

from cprint import *

from core.configs import settings

#############################################################################
## Module - Command Center
#############################################################################

def help():
    print(f'Commands: [{", ".join(settings.COMMANDS.keys())}]')

def terminate():
    sys.exit(0)

def hunt():
    # Ask for additional info
    while True:
        cprint.ok(f'Mode [{", ".join(settings.HUNTING_MODES.keys())}]:')
        mode = input().strip().lower()
        if mode in settings.HUNTING_MODES.keys():
            settings.HUNTING_MODES[mode]()
            break
