#!/usr/bin/python3
"""
Entry point class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter

    Args:
    cmd (Cmd): class cmd.

    Returns:
    nothing.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit
        """
        return True

    def do_EOF(self, line):
        """Exit from command line
        """
        print("")
        return True

    def emptyline(self):
        """Deactivate emptyline method from super   class.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
