from modules import command_center, memory


if __name__ == '__main__':

    memory.start_reading_files()

    # Check for commands
    while True:
        command = command_center.wait_for_command()
        command_center.try_execute_command(command)
