import sys
from happypass import baseparser
from happypass import basecommand


def main(initial_args=None):
    if initial_args is None:
        initial_args = sys.argv[1:]

    parser = baseparser.parser
    if not initial_args or initial_args[0] == '-h' \
       or initial_args[0] == '--help':
        initial_args = ['help']
    basecommand.load_command(initial_args[0])
    if initial_args[0] not in basecommand.command_dict:
        parser.error('bad command, use --help to see what supported')
        sys.exit(1)

    # args = parser.parse_args(initial_args)
    command = basecommand.command_dict[initial_args[0]]
    command.main(initial_args[1:])

if __name__ == '__main__':
    # exit = main()
    # if exit:
    #     sys.exit(exit)
    main()
