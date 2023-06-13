#############################################################################
## Imports
#############################################################################

from enum import Enum

from core.models import MemoryMappedFile

from modules import commands
from modules import hunting

#############################################################################
## Module - Settings
## ---
## This file contains various configuration parameters and constants that are used 
## across different components of the program. 
##
## Changes to this file can affect the behavior of the entire application, 
## so please handle with care.
#############################################################################

class MemoryMappedFiles(Enum):
    SCREEN = MemoryMappedFile('screen', 24576)
    OPPONENT = MemoryMappedFile('opponent_info', 4096)
    INPUT = MemoryMappedFile('input_info', 4096)
    PARTY = MemoryMappedFile('party_info', 8192)

#############################################################################
## Terminal
#############################################################################

COMMANDS = {
    'help': commands.help,
    'terminate': commands.terminate,
    'hunt': commands.hunt
}

HUNTING_MODES = {
    'starter': hunting.starter
}

#############################################################################
## Game
#############################################################################

DEFAULT_INPUT = {
    'A': False,
    'B': False,
    'Down': False,
    'GBA Light Sensor': 0,
    'L': False,
    'Left': False,
    'LidClose': False,
    'LidOpen': False,
    'Mic Volume': 0,
    'Power': False,
    'R': False,
    'Right': False,
    'Select': False,
    'Start': False,
    'Touch X': 255,
    'Touch Y': 0,
    'Touch': True,
    'Up': False,
    'X': False,
    'Y': False,
}

FPS = 60

# STARTER = 'turtwig'
# STARTER = 'chimchar'
STARTER = 'pipup'