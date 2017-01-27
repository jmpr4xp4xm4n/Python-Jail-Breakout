#!/usr/bin/env python

import signal
import re
from sys import stdin, stdout
import threading

def handler(signum, frame):
    pass

def __exit__handler(signum, frame):
   exit()

signal.signal( signal.SIGABRT, handler )
signal.signal( signal.SIGALRM, handler )
signal.signal( signal.SIGBUS, handler )
signal.signal( signal.SIGCHLD, handler )
signal.signal( signal.SIGCLD, handler )
signal.signal( signal.SIGCONT, handler )
signal.signal( signal.SIGFPE, handler )
signal.signal( signal.SIGHUP, __exit__handler )
signal.signal( signal.SIGILL, handler )
signal.signal( signal.SIGINT, handler )
signal.signal( signal.SIGIO, handler )
signal.signal( signal.SIGIOT, handler )
signal.signal( signal.SIGPIPE, handler )
signal.signal( signal.SIGPOLL, handler )
signal.signal( signal.SIGPROF, handler )
signal.signal( signal.SIGPWR, handler )
signal.signal( signal.SIGQUIT, handler )
signal.signal( signal.SIGRTMAX, handler )
signal.signal( signal.SIGRTMIN, handler )
signal.signal( signal.SIGSEGV, handler )
signal.signal( signal.SIGSYS, handler )
signal.signal( signal.SIGTERM, handler )
signal.signal( signal.SIGTRAP, handler )
signal.signal( signal.SIGTSTP, handler )
signal.signal( signal.SIGTTIN, handler )
signal.signal( signal.SIGTTOU, handler )
signal.signal( signal.SIGURG, handler )
signal.signal( signal.SIGUSR1, handler )
signal.signal( signal.SIGUSR2, handler )
signal.signal( signal.SIGVTALRM, handler )
signal.signal( signal.SIGWINCH, handler )
signal.signal( signal.SIGXCPU, handler )
signal.signal( signal.SIGXFSZ, handler )
signal.signal( signal.SIG_IGN, handler )

print 'Get flag from the .key file'

inp = ' '
while inp != '':
 try:
   print "# ",
   inp = stdin.readline()[:100]
   match = re.match( '.*([\[=_\]%;,37\"\'\\\/]+|exec|std|import|module|inp|open).*', inp )
   if not match:
     a = None
     exec "a=" + inp
     print "Result: ", a
   else:
     print "Prohibited"
 except:
   print "Keep trying"
