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
        elif cls_name.strip() not in globals():
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
        key = ".".join(line).strip()
        if not line:
            print("** class name missing ** ")
        elif line[0].strip() not in globals():
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
        key = ".".join(line).strip()
        if not line:
            print("** class name missing ** ")
        elif line[0].strip() not in globals():
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
        if not cls_name:
            print([str(obj) for obj in models.storage.all().values()])
        elif cls_name.strip() in globals():
            print([str(obj) for obj in models.storage.all().values()
                   if obj.__class__.__name__ == cls_name.strip()])
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
        elif line[0].strip() not in globals():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif '.'.join(line[:2]).strip() not in models.storage.all():
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            obj_id = '.'.join(line[:2]).strip()
            attr = line[2].strip()
            value = line[3].strip(' "')
            if value.isdigit():
                value = int(value)
            elif '.' in value:
                value = float(value)
            _dict = models.storage.all()[obj_id].__dict__
            _dict[attr] = value
            models.storage.all()[obj_id].save()

    def do_count(self, cls_name):
        """retrieve the number of instances of a class.

        Args:
            cls_name (str): class name to retrive its instancces.
        """
        if cls_name.strip() in globals():
            num_instances = 0
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == cls_name.strip():
                    num_instances += 1
            print(num_instances)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.

        Args:
            line (str): string with class name and method to execute.
        """
        methods = {
            'all': self.do_all, 'count': self.do_count,
            'show': self.do_show, 'destroy': self.do_destroy,
            'update': self.do_update
        }
        params = line[line.find('(')+1:line.find(')')].split(',')
        cls_name, func = line[:line.find('(')].split('.')
        params.insert(0, cls_name)
        if cls_name.strip() in globals() and func.strip() in methods:
            string = ' '.join([i.strip(' "') for i in params])
            methods[func](string)

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
