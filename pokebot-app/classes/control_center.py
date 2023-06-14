#############################################################################
## Imports
#############################################################################

import json
import time

from modules import memory
from core.configs import settings

#############################################################################
## Class
#############################################################################

class ControlCenter:

    def __init__(self):
        self.current_input = settings.DEFAULT_INPUT

    #########################################################
    ## Public methods
    #########################################################

    def wait_frames(self, frames):
        time.sleep(frames * (1 / settings.FPS))

    def hold_button(self, button):
        self.current_input[button] = True

        memory.write_to_memory_mapped_file(
            settings.MemoryMappedFiles.INPUT.name,
            settings.MemoryMappedFiles.INPUT.size,
            json.dumps(self.current_input)
        )

    def release_button(self, button):
        self.current_input[button] = False
        
        memory.write_to_memory_mapped_file(
            settings.MemoryMappedFiles.INPUT.name,
            settings.MemoryMappedFiles.INPUT.size,
            json.dumps(self.current_input)
        )

    def release_all_buttons(self):
        self.current_input = settings.DEFAULT_INPUT

    def soft_reset(self):

        self.release_all_buttons()

        self.current_input['L'] = True
        self.current_input['R'] = True
        self.current_input['Start'] = True
        self.current_input['Select'] = True

        memory.write_to_memory_mapped_file(
            settings.MemoryMappedFiles.INPUT.name,
            settings.MemoryMappedFiles.INPUT.size,
            json.dumps(self.current_input)
        )

    def hard_reset(self):
        self.hold_button('Power')
        self.wait_frames(60)
        self.release_button('Power')
