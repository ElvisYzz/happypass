from happypass.basecommand import Command


class UpdateCommand(Command):
    name = 'update'
    summary = 'Update the credit infomation'

    def __init__(self):
        super(UpdateCommand, self).__init__()
        self.parser.add_argument(
            '--name', '-n',
            action='store',
            dest='name',
            help='The name of the credit')
        self.parser.add_argument(
            '--username', '-u',
            action='store',
            dest='username',
            help='The username of the credit')
        self.parser.add_argument(
            '--password', '-p',
            action='store',
            dest='password',
            help='The password to the username')
        self.parser.add_argument(
            '--website', '-w',
            action='store',
            dest='website',
            help='The website correspond to this credit')


    def run(self, args):
        if not args.name:
            args.name = raw_input("The name of the credit: ")
        if not args.username:
            args.username = raw_input("The username of the credit: ")
        if not args.password:
            if not args.website:
                

