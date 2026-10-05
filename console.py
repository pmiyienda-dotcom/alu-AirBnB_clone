#!/usr/bin/python3
"""Defines HBNBCommand, the entry point of the command interpreter."""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place,
        "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance, save it and print its id
        Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance and save the change
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all instances, optionally filtered by class name
        Usage: all or all <class name>
        """
        args = arg.split()
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        result = []
        for obj in models.storage.all().values():
            if not args or obj.__class__.__name__ == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance by adding or changing one attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = models.storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                name = args[2]
                value = args[3]
                if hasattr(obj, name):
                    try:
                        value = type(getattr(obj, name))(value)
                    except ValueError:
                        pass
                else:
                    for cast in (int, float):
                        try:
                            value = cast(value)
                            break
                        except ValueError:
                            pass
                setattr(obj, name, value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
