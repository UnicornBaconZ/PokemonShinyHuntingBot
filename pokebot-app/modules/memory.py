#############################################################################
## Imports
#############################################################################

import json
import time
import mmap

#############################################################################
## Module - Memory
#############################################################################

## TODO: Update to an infinate loop and pull from a queue
def send_to_memory_mapped_file(filename, size, command):
    with open(filename, "w+b") as file:
        file.truncate(size)
        with mmap.mmap(file.fileno(), size) as memory:
            memory.seek(0)
            memory.write(command.encode("utf-8"))

def read_from_memory_mapped_file(filename, size):
    with open(filename, "r+b") as file:
        with mmap.mmap(file.fileno(), size) as memory:
            while True:
                memory.seek(0)
                content = memory.read().decode("utf-8").strip('\x00')
                print(content)
                memory.flush()
                time.sleep(1)

#############################################################################
## Testing
#############################################################################

INPUT_FILE = "input_info"
SIZE = 4096

if __name__ == '__main__':
    send_to_memory_mapped_file(INPUT_FILE, SIZE, json.dumps({'B': True, 'Left': True}))
    time.sleep(2)
    read_from_memory_mapped_file(INPUT_FILE, SIZE)