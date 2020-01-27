import sys
from cli import CLI

if __name__ == '__main__':
  if (len(sys.argv) != 1):
    if (sys.argv[1] == 'api'):
      # run the api
      print('api')
    elif (sys.argv[1] == 'cli'):
      CLI.run()
      
    elif (sys.argv[1] == '--help'):
      print('-api :: runs the local api server')
      print('-cli :: runs the local cli')
      print('--help :: prints command line options')
    else:
      print('Please specify the api or cli')
  else:
    print('Please specify the api or cli')
