"""This module exports the Perl -c util."""

from cuda_lint import Linter, util
from cudatext import * 


class Puppet(Linter):

    """Provides an interface to perl -c"""
    cmd = None
    executable = 'puppet'
    multiline = False
    syntax = ('Ruby')
    regex = r'.*Error:(?P<message>.*):(?P<stdin>.*)line: (?P<line>\d+), column: (?P<column>\d+)'
    base_cmd = ('parser '
    ' validate'
    ' --color=false ')
    tempfile_suffix = 'rb'


    def split_match(self, match):
        print('plit_match')
        print(match)
   
        """Return the components of the error."""
        split_match = super(Puppet, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        print('cmd')
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
