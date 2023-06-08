-----------------------------------------------------------------------------
-- Imports and dependencies
-----------------------------------------------------------------------------
local mem = require('mem')

-----------------------------------------------------------------------------
-- Module declaration
-----------------------------------------------------------------------------

local pokedata = {}
local pokedata_private = {}

-----------------------------------------------------------------------------
-- Public functions
-----------------------------------------------------------------------------

function pokedata.pokemon_data(address)

  local pokemon = {}

  pokemon.pokedexNumber = mem.readword(address)

  pokemon.attack = mem.readword(address + 2)
  pokemon.defense = mem.readword(address + 4)
  pokemon.speed = mem.readword(address + 6)
  pokemon.spAttack = mem.readword(address + 8)
  pokemon.spDefense = mem.readword(address + 10)

  pokemon.ability = mem.readbyte(address + 39)

  pokemon.currentLvl = mem.readbyte(address + 52)
  pokemon.happiness = mem.readbyte(address + 56)
  
  pokemon.currentHP = mem.readword(address + 76)
  pokemon.maxHP = mem.readword(address + 80)

  pokemon.currentEXP = mem.readdword(address + 100)

  pokemon.pid = mem.readdword(address + 104)

  pokemon.trainerID = mem.readword(address + 116)
  pokemon.secretID = mem.readword(address + 118)
  
  pokemon.itemHolding = mem.readword(address + 120)

  pokemon.gender = mem.readbyte(address + 126)
  pokemon.pokeball = mem.readbyte(address + 127)

  return pokemon

end


-----------------------------------------------------------------------------
-- Internal and private functions.
-----------------------------------------------------------------------------

function calculate_shiny_value(trainerID, secretID, personalityID)



end

-----------------------------------------------------------------------------
-- Export module
-----------------------------------------------------------------------------

return pokedata