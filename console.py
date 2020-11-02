#!/usr/bin/python3
"""
Entry point class
"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter.

    Args:
    cmd (Cmd): class cmd.

    Returns:
        nothing.
    """
    use_rawinput = False
    prompt = '(hbnb) '

    def do_create(self, cls_name):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id

        Args:
            cls_name (BaseModel): BaseModel class to create the instance.
        """
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in globals():
            print("** class doesn't exist **")
        else:
            obj = eval(cls_name)()
            print(obj.id)
            obj.save()

    def do_show(self, cls_name_id):
        """Prints the string representation of an instance based on the class
        name and id
        Args:
            cls_name_id (str): str containing BaseModel and id.
        """
        line = cls_name_id.split()
        key = ".".join(line)
        if not line:
            print("** class name missing ** ")
        elif line[0] not in globals():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, cls_name_id):
        """Deletes an instance based on the class name and id

        Args:
            cls_name_id (str): String containing BaseModel and id substring
            separated by whitespace.
        """
        line = cls_name_id.split()
        key = ".".join(line)
        if not line:
            print("** class name missing ** ")
        elif line[0] not in globals():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_all(self, cls_name):
        """ Prints all string representation of all instances based or not on
        the class name

        Args:
            cls_name (str): class name to print all string representation.
        """
        if not cls_name or cls_name in globals():
            print([str(value) for value in models.storage.all().values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, to_update):
        """Updates an instance based on the class name and id by adding
        or updating attribute

        Args:
            line (str): string containing
            <class name> <id> <attribute name> "<attribute value>"
        """
        line = to_update.split()
        if not line:
            print("** class name missing **")
        elif line[0] not in globals():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif '.'.join(line[:2]) not in models.storage.all():
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            obj_id, attr, value = '.'.join(line[:2]), line[2], line[3]
            _dict = models.storage.all()[obj_id].__dict__
            _dict[attr] = value
            models.storage.save()

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
