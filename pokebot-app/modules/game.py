#############################################################################
## Imports
#############################################################################

from queue import Queue

from cprint import *

from modules import modes
from classes.command_center import CommandCenter
from classes.control_center import ControlCenter

#############################################################################
## Module - Game
#############################################################################

def main_loop():

    current_mode = 'idle'
    mode_queue = Queue()

    command_center = CommandCenter(mode_queue)
    command_center.start()

    control_center = ControlCenter()


    while True:
        
        # Switch the mode if the queue is not empty
        if not mode_queue.empty():
            current_mode = mode_queue.get()

            if current_mode == 'terminate':
                sys.exit(0)

        MODES[current_mode](control_center)
        
#############################################################################
## Modes
#############################################################################

MODES = {
    'idle': modes.idle,
    'starter': modes.starter,
    'route_201': modes.route_201,
    'route_202': modes.route_202,
    'gym_1': modes.gym_1
}