import argparse

parser = argparse.ArgumentParser(description="This is happypass")

parser.add_argument('command', action='store', default='add',
                    help='following commands are supported\n \
                    add\nupdate\nfind\ndelete')
