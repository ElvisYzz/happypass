from happypass.credit import Credit
from happypass.basecommand import Command


class AddCommand(Command):
    name = 'add'
    summary = 'Add a credit'

    def __init__(self):
        super(AddCommand, self).__init__()
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
            args.username = raw_input("username: ")
        if not args.password:
            args.password = raw_input("password: ")
        credit = Credit(args.name, args.username, args.password)
        if not args.website:
            args.website = raw_input("website(default is None):")
            if args.website:
                credit.setWebsite(args.website)

AddCommand()
