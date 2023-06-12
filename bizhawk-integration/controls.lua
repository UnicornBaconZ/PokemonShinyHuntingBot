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
    console.log('Reading...')
    local is_successfull, result = pcall(comm.mmfRead, filename, 4096)

    console.log(is_successfull)
    console.log(result)

    if not is_successfull then
        gui.addmessage('Failed reading the input file')
        return
    end

    return result
end

function controls.read_controls()
    return joypad.get()
end

function controls.write_controls(input)
    if controls_private.is_valid_input(input) then
        joypad.set(input)
    else
        --gui.addmessage('Invalid input passed to the emulator')
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
