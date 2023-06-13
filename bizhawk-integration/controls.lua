-----------------------------------------------------------------------------
-- Imports and dependencies
-----------------------------------------------------------------------------

local json = require('json')

-----------------------------------------------------------------------------
-- Module declaration
-----------------------------------------------------------------------------

local controls = {}
local controls_private = {}

local ALLOWED_INPUT = {
    ['A'] = 'boolean',
    ['B'] = 'boolean',
    ['Down'] = 'boolean',
    ['GBA Light Sensor'] = 'number',
    ['L'] = 'boolean',
    ['Left'] = 'boolean',
    ['LidClose'] = 'boolean',
    ['LidOpen'] = 'boolean',
    ['Mic Volume'] = 'number',
    ['Power'] = 'boolean',
    ['R'] = 'boolean',
    ['Right'] = 'boolean',
    ['Select'] = 'boolean',
    ['Start'] = 'boolean',
    ['Touch X'] = 'number',
    ['Touch Y'] = 'number',
    ['Touch'] = 'boolean',
    ['Up'] = 'boolean',
    ['X'] = 'boolean',
    ['Y'] = 'boolean',
}

-----------------------------------------------------------------------------
-- Public functions
-----------------------------------------------------------------------------

function controls.read_controls_file(filename)
    local is_success_read, result_read = pcall(comm.mmfRead, filename, 4096)

    if not is_success_read then
        gui.addmessage('Failed reading the input file')
        return
    end

    local is_succes_convert, result_convert = pcall(json.decode, result_read)

    if is_succes_convert then
        return result_convert
    end

    return { B = false }
end

function controls.read_controls()
    return joypad.get()
end

function controls.write_controls(input)
    if controls_private.is_valid_input(input) then
        joypad.set(input)
    else
        gui.addmessage('Invalid input passed to the emulator')
    end
end

-----------------------------------------------------------------------------
-- Internal and private functions.
-----------------------------------------------------------------------------

function controls_private.is_valid_input(input)
    if type(input) ~= "table" then
        return false
    end

    for key, value in pairs(input) do
        if ALLOWED_INPUT[key] == nil or (type(value) ~= ALLOWED_INPUT[key]) then
            return false
        end
    end
    return true
end

-----------------------------------------------------------------------------
-- Export module
-----------------------------------------------------------------------------

return controls
