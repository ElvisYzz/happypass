"""Key Manager

Usage: python happypass.py [options]

Options:
  help                      show this help
  add                       add a credit
  update                    update a credit
  find                      find the username or/and the password about the specific credit
  delete                    delete a credit

Examples:
  kgp.py                  generates several paragraphs of Kantian philosophy
  kgp.py -g husserl.xml   generates several paragraphs of Husserl
  kpg.py "<xref id='paragraph'/>"  generates a paragraph of Kant
  kgp.py template.xml     reads from template.xml to decide what to generate
"""

__version__ == 0.1
__author__ == 'Elvis'


import sys


def main(argv):
    if len(argv) != 1:
        usage()
        sys.exit(1)

    opt = argv[0]
    if opt == 'help':
        help()
        sys.exit()
    elif opt in ('add', 'update', 'find', 'delete'):
        keymanager = KeyManager()
        getattr(keymanager, opt, None)()

def usage():


if __name__ == '__main__':
    main(sys.argv[1:])
