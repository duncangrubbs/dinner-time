import sys
from cli.cli import CLI
from api import api as API

if __name__ == '__main__':
    if (len(sys.argv) != 1):
        if (sys.argv[1] == 'api'):
            API.run()
        elif (sys.argv[1] == 'cli'):
            CLI.run()

        elif (sys.argv[1] == '--help'):
            print('api :: runs the local api server')
            print('cli :: runs the local cli')
            print('--help :: prints command line options')
        else:
            print('Please specify the api or cli')
    else:
        print('Please specify the api or cli')
