#!/usr/bin/env python2
#
# MyShell.py - library for creating text interfaces.
#
#  MyShell is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  MyShell is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import readline
import sys
import os

__version__ = "0.1"
__author__ = "Hypsurus <hypsurus@mail.ru>"

words = ["exit", "clear",
         "help"]

try:
    raw_input
except NameError:
    raw_input = input

class MyShellException(Exception):
    def __init__(self):
        pass

class auto(object):
    """ auto(objects)
        Auto complete words from an array using :TAB """

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

class Menu(object):
    """ Create menu inside the shell """
    def __init__(self, Type=1):
        """ Type=1 - numbers menu.
            Type=0 - yes/no menu.
        """
        self.options = {}
        self.type = Type
        self.counter = 0

    def add_entry(self, help, fun):
        if self.type == 1:
            self.counter += 1
            pattern = "(%d) %s" % (self.counter, help)
        elif self.type == 0:
            pattern = "> %s" % (help)
        else:
            raise MyShellException("No type given")

        self.options.update( { pattern : fun } )

    def show(self):
        for help, fun in self.options.items():
            print("%s" % (help) )

    def run(self, prompt="> "):
        if self.type == 1:
            try:
                shell = int(raw_input(prompt))
                return int(shell)
            except ValueError:
                print("Please select a number.")
        elif self.type == 0:
            try:
                shell = str(raw_input(prompt+" (y/N) : "))
            except ValueError:
                print("Please select answer yes/no.")

            if shell == "y" or shell == "Y" or shell == "yes" or shell == "YES":
                return True
            else:
                return False
        else:
            raise MyShellException("No type given")

def shell_complete(array):
    completer = auto(array)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab:complete')

def shell_add_option(option, help, fun):
    """ mymenu_add_entry(help=None, color=None.

    Add new entry to the menu

    """
    entrys.update( {option : fun } )
    helps.update( {option : help } )
    words.append(option)

def shell_display_help(args):
    """ myshell_display_help().
        display MyShell help
    """
    for option, help in helps.items():
        print("\t%s \t<=>\t %s" % ( option, help ) )

"""
    User functions
"""
def myshell_quit(args):
    sys.exit(0)

def myshell_clear(args):
    if 1 == 2:
        os.system("cls")
    else:
        print("\033[H\033[J")

"""
 Define here the start values for MyShell
"""
entrys = { "exit"  : myshell_quit,
           "help"  : shell_display_help,
           "clear" : myshell_clear }
helps  = { "exit"  : "quit.",
           "clear" : "clear the screen"}


def shell_shell(prompt=">>> "):
    """ myshell_shell(prompt=">>> ")
        
        Serve the shell
    """

    shell_complete(words)

    while True:
        try:
            shell = str(raw_input(prompt))
            args = shell.split()
            for option, fun in entrys.items():
                if args[0] == option:
                    if len(args) > 1:
                        args.pop(0)
                    fun(args)
        except IndexError:
            pass
