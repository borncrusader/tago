#!/usr/bin/python

import utils
import app

if __name__ == "__main__":
  try:
    # check if options are given right and return the switches in a dict
    switches = utils.check_options()
    # display the version and exit, if switch is given
    utils.check_version(switches)
    # display the help and exit, if switch is given
    utils.check_help(switches)
    # manipulate the switches
    app.engine(switches)
  except KeyboardInterrupt:
    print "\nbye"
