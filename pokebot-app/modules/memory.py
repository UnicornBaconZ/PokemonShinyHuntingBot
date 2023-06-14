#############################################################################
## Imports
#############################################################################

import json
import time
import mmap

from threading import Thread

from core.configs import settings

#############################################################################
## Module - Memory
#############################################################################

## TODO: Update to an infinate loop and pull from a queue
def write_to_memory_mapped_file(filename, size, data):
    with mmap.mmap(-1, size, filename, access=mmap.ACCESS_WRITE) as memory:
        memory.seek(0)
        memory.write(data.encode("utf-8"))

def read_from_memory_mapped_file(filename, size):
    with mmap.mmap(0, size, filename) as memory:
        while True:
            memory.seek(0)
            content = memory.read().decode("utf-8").strip('\x00')
            memory.flush()
            time.sleep(10)

def start_reading_files():
    for file in settings.MemoryMappedFiles:
        thread = Thread(
            name=file.value.name,
            target=read_from_memory_mapped_file,
            args=(file.value.name, file.value.size,),
            daemon=True
        )

        thread.start()

#############################################################################
## Testing
#############################################################################

INPUT_FILE = "input_info"
SIZE = 4096

if __name__ == '__main__':
    while True:
        write_to_memory_mapped_file(INPUT_FILE, SIZE, json.dumps({'B': True, 'Left': True}))
        time.sleep(2)
        read_from_memory_mapped_file(INPUT_FILE, SIZE)