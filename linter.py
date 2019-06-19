"""This module exports the puppet parser validate --color=false."""

from cuda_lint import Linter, util

class Puppet(Linter):

    """Provides an interface to puppet parser validate --color=false"""
    cmd = None
    executable = 'puppet'
    multiline = False
    syntax = ('Puppet')
    regex = r'.*Error:(?P<message>.*):(?P<stdin>.*)line: (?P<line>\d+), column: (?P<column>\d+)'
    base_cmd = ('parser '
    ' validate'
    ' --color=false ')
    tempfile_suffix = 'rb'


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(Puppet, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
