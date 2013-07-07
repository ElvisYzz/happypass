from happypass.basecommand import Command, command_dict
from happypass.baseparser import parser
from happypass.exceptions import CommandError


class HelpCommand(Command):
    name = 'help'
    summany = 'Show available commands'

    def run(self, args):
        if args:
            command = args[0]
            if command not in command_dict:
                raise CommandError('No command with the name: %s' % command)
            command = command_dict[command]
            command.parser.print_help()
        parser.print_help()

HelpCommand()
