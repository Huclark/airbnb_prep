#!/usr/bin/python3
"""Entry point of the command interpreter
"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class
    """
    # custom prompt for program
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Use ctrl+D to exit as keyboard shortcut to exit program
        """
        print()
        return True

    def do_help(self, arg):
        """Shows help message"""
        super().do_help(arg)

    def emptyline(self):
        """Does nothing on an empty line so as to handle
        the case where emptyline + ENTER key is used"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
