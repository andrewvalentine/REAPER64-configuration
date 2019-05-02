#!/usr/bin/python

import os.path
from ConfigParser import *
 
# Define MyConfigParser class #
# Required to remove whitespace from resulting .ini file
# https://stackoverflow.com/a/32167382

class MyConfigParser(ConfigParser):
    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if self._defaults:
            fp.write("[%s]\n" % ConfigParser.DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s=%s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for (key, value) in self._sections[section].items():
                if key == "__name__":
                    continue
                if (value is not None) or (self._optcre == self.OPTCRE):
                    key = "=".join((key, str(value).replace('\n', '\n\t')))
                fp.write("%s\n" % key)
            fp.write("\n")

# Define functions #

def setReaper64Preferences():
	""" Set REAPER64 preferences """
	config = MyConfigParser()
	config.add_section('REAPER')
	config.set('REAPER','verchk','0')
        config.set('REAPER','titlebarreghide','1')
	with open(prefFile, 'w+') as configfile:
		config.write(configfile)
	
def manageReaper64Preferences():
	""" Manage REAPER64 preferences """
	config = MyConfigParser()
	config.read(prefFile)
	config.set('REAPER','verchk','0')
        config.set('REAPER','titlebarreghide','1')
	with open(prefFile, 'w') as configfile:
		config.write(configfile)

# Get user and REAPER64 preferences file #

home = os.path.expanduser("~")
prefDir = os.path.join(home, "Library/Application Support/REAPER")
prefFile = os.path.join(prefDir, "reaper.ini")

# Check for REAPER preferences directory

if not os.path.exists(prefDir):
    os.mkdir(prefDir)
    print("REAPER preferences directory" , prefDir, "does not exist." , "Creating." )
else:
    print("REAPER preferences directory", prefDir, "exists.")

# Configure REAPER64 preferences as required

if not os.path.exists(prefFile):
    print("REAPER preferences file" , prefFile , "does not exist." , "Creating and configuring." )
    setReaper64Preferences()

else:
	print("REAPER preferences file" , prefFile , "exists" , "Ensuring verchk and titlebarreghide are disabled.")
        manageReaper64Preferences()

raise SystemExit()
