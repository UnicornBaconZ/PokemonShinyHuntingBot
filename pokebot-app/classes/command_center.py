#############################################################################
## Imports
#############################################################################

from threading import Thread

from cprint import *

#############################################################################
## Class
#############################################################################

class CommandCenter:

    def __init__(self, mode_queue):
        self.mode_queue = mode_queue

        self.COMMANDS = {
            'help': self._help,
            'terminate': self._terminate,
            'idle': self._idle,
            'hunt': self._hunt,
        }

        self.thread = Thread(
            name='command_center',
            target=self._thread,
            daemon=True
        )

    #########################################################
    ## Public methods
    #########################################################

    def start(self):
        if not self.thread.is_alive():
            self.thread.start()
        else:
            cprint.err('The thread is already running')


    #########################################################
    ## Private methods
    #########################################################

    def _thread(self):
        while True:
            command = self._wait_for_command()
            self._try_execute_command(command)


    def _wait_for_command(self):
        cprint.ok('\nEnter a command:')
        command = input().strip().lower()
        return command

    def _try_execute_command(self, command):
        if self._command_exists(command):
            self.COMMANDS[command]()
        else:
            cprint.err(f'\nThe command "{command}" does not exist')

    def _command_exists(self, command):
        return command in self.COMMANDS.keys()

    #########################################################
    ## Commands
    #########################################################

    def _help(self):
        cprint.info('Available commands:')
        for command in self.COMMANDS.keys():
            cprint(f'- {command}')

    def _terminate(self):
        self.mode_queue.put('terminate')

    def _idle(self):
        self.mode_queue.put('idle')

    def _hunt(self):
        # # Ask for additional info
        # while True:
        #     cprint.ok(f'Mode [{", ".join(HUNTING_MODES.keys())}]:')
        #     mode = input().strip().lower()
        #     if mode in HUNTING_MODES.keys():
        #         HUNTING_MODES[mode]()
        #         break
        pass
