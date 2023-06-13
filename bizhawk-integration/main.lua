-----------------------------------------------------------------------------
-- Imports and dependencies
-----------------------------------------------------------------------------

local json = require('json')

local pokedata = require('pokedata')
local controls = require('controls')

-----------------------------------------------------------------------------
-- Setup
-----------------------------------------------------------------------------

console.log('Starting pokébot...\n')

-- Create memory mapped files with a predefined size
-- e.g. 4096 byte
comm.mmfWrite("screen", string.rep("\x00", 24576))
comm.mmfSetFilename("screen")
comm.mmfScreenshot()

comm.mmfWrite('input_info', string.rep("\x00", 4096))
comm.mmfWrite('opponent_info', string.rep("\x00", 4096))
comm.mmfWrite('party_info', string.rep("\x00", 8192))

-----------------------------------------------------------------------------
-- Main loop
-----------------------------------------------------------------------------

console.log('Main loop started')

while true do
  -- Read data from memory
  local opponent = pokedata.pokemon_data(0x002C5810)

  -- Write data to memory mapped files
  comm.mmfScreenshot()

  comm.mmfWrite('opponent_info', json.encode({ ['opponent'] = opponent }) .. "\x00")

  -- Read data from memory mapped files
  local input = controls.read_controls_file('input_info')
  controls.write_controls(input)

  emu.frameadvance()
end
