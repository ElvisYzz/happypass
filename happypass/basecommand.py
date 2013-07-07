import argparse
import sys


from pkgutil import walk_packages
from happypass import commands

command_dict = {}


class Command(object):
    name = None
    usage = None

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        command_dict[self.name] = self

    def main(self, args):
        print args
        args = self.parser.parse_args(args)
        try:
            self.run(args)
        except:
            pass


def load_command(command):
    full_name = 'happypass.commands.%s' % command
    if full_name in sys.modules:
        return
    try:
        __import__(full_name)
    except ImportError:
        pass


def load_all_commands():
    for command in command_names():
        load_command(command)


def command_names():
    names = set([pkg[1] for pkg in walk_packages(path=commands.__path__)])
    return list(names)
