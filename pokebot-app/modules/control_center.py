#############################################################################
## Imports
#############################################################################

import json
import time

from modules import memory

from core.configs import settings

#############################################################################
## Module - Control Center
#############################################################################

current_input = settings.DEFAULT_INPUT

def wait_frames(frames):
    time.sleep(frames * (1 / settings.FPS))

def hold_button(button):
    global current_input
    current_input[button] = True

    memory.write_to_memory_mapped_file(
        settings.MemoryMappedFiles.INPUT.name,
        settings.MemoryMappedFiles.INPUT.size,
        json.dumps(current_input)
    )

def release_button(button):
    global current_input
    current_input[button] = False
    
    memory.write_to_memory_mapped_file(
        settings.MemoryMappedFiles.INPUT.name,
        settings.MemoryMappedFiles.INPUT.size,
        json.dumps(current_input)
    )

def release_all_buttons():
    global current_input
    current_input = settings.DEFAULT_INPUT

def soft_reset():
    global current_input

    release_all_buttons()

    current_input['L'] = True
    current_input['R'] = True
    current_input['Start'] = True
    current_input['Select'] = True

    memory.write_to_memory_mapped_file(
        settings.MemoryMappedFiles.INPUT.name,
        settings.MemoryMappedFiles.INPUT.size,
        json.dumps(current_input)
    )

def hard_reset():
    hold_button('Power')
    wait_frames()
