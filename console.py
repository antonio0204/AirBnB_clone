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
