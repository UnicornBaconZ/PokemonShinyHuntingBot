-----------------------------------------------------------------------------
-- Module declaration
-----------------------------------------------------------------------------

local mem = {}
local mem_private = {}

-----------------------------------------------------------------------------
-- Public functions
-----------------------------------------------------------------------------

-- "0": "Main RAM"
-- "1": "Shared WRAM"
-- "2": "ARM7 WRAM"
-- "3": "Instruction TCM"
-- "4": "Data TCM"
-- "5": "ARM9 BIOS"
-- "6": "ARM7 BIOS"
-- "7": "ARM9 System Bus"
-- "8": "ARM7 System Bus"
-- "9": "Waterbox PageData"

function mem.readdword(addr)
	return mem_private.read(addr, 4)
end

function mem.readword(addr)
	return mem_private.read(addr, 2)
end

function mem.readbyte(addr)
	return mem_private.read(addr, 1)
end

-----------------------------------------------------------------------------
-- Internal and private functions.
-----------------------------------------------------------------------------

function mem_private.read(addr, size)

	local memtype = 'Main RAM'

	addr = addr & 0xFFFFFF

	if size == 1 then
		return memory.read_u8(addr, memtype)
	elseif size == 2 then
		return memory.read_u16_le(addr, memtype)
	elseif size == 3 then
		return memory.read_u24_le(addr, memtype)
	else
		return memory.read_u32_le(addr, memtype)
	end 
end

-----------------------------------------------------------------------------
-- Export module
-----------------------------------------------------------------------------

return mem