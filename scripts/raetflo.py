#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
raet floscript runner CLI

Runs floscript plan from command line shell

example:
raetflo -v concise -n raet -r -f ../raet/flo/plan/raet.flo -b raet.flo.behaving
raetflo -v verbose -n raet -r -p 0.0625 ../raet/flo/plan/raet.flo -b raet.flo

'''

# Import python libs
import sys

# Import ioflo libs
import ioflo.app.run


def main():
    '''
    Main entry point for ioflo CLI
    '''
    args = ioflo.app.run.parseArgs()

    if args.version:
        print 'ioflo version {0}'.format(ioflo.__version__)
        sys.exit(0)

    ioflo.app.run.run(name=args.name,
                      filename=args.filename,
                      period=float(args.period),
                      verbose=args.verbose,
                      realtime=args.realtime,
                      behaviors=args.behaviors,
                      username=args.username,
                      password=args.password,)

if __name__ == '__main__':
    main()