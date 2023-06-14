import io
import mmap
import time
from PIL import Image


def read_from_memory_mapped_file(filename, size):
    with mmap.mmap(0, size, filename) as memory:
        content = Image.open(io.BytesIO(memory))
        content.show()
        content.save(r'C:\Users\kirsten.vermeulen\Downloads\BattleScreen.png')

read_from_memory_mapped_file('screen', 24576)
time.sleep(5)