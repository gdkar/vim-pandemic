from __future__ import print_function

class Printer:

    RED = "\033[1;31m";
    YLW = "\033[1;33m";
    CLR = "\033[0m";
    stderr = __import__('sys').stderr
    stdout = __import__('sys').stdout

    def __init__(self): pass;

    def message(self, msg): print ( msg, file = self.stdout )

    def error(self, msg): print ( "{}ERR: {}{}" .format(self.RED, msg, self.CLR),file=self.stderr)

    def warn(self, msg): print ( "{}WRN: {}{}" .format(self.YLW, msg, self.CLR),file=self.stderr)
