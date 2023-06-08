import time
import mmap
from threading import Thread

from modules import command_center

def read_from_memory_mapped_file(filename, size):

    # memory-map the file, size 0 means whole file
    with mmap.mmap(0, size, filename) as mm:
        while True:
            # Read all content
            mm.seek(0)
            content = mm.read().decode("utf-8").strip('\x00')
            print(content)
            mm.flush()

            # sleep a little before the next read
            time.sleep(0.5)


if __name__ == '__main__':

    # Starting data retrieval threads

    # for file in settings.MEMORY_MAPPED_FILES:
    #     thread = Thread(
    #         name=file['name'],
    #         target=read_from_memory_mapped_file,
    #         args=(file['name'], file['size'],),
    #         daemon=True
    #     )

    #     thread.start()

    # Check for commands
    while True:
        command = command_center.wait_for_command()
        command_center.try_execute_command(command)
