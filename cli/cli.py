import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], 'r:a:')

for opt, arg in opts:
    if opt == '-r':
        print('got {} with -r option'.format(arg))
    elif opt == '-a':
        print('got {} with -a option'.format(arg))

 