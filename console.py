#!/usr/bin/env python3
"""
This module defines the command interpreter for the Airbnb clone project.
"""

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line handling
        """
        pass

    def do_create(self, args):
        """
        Create a new instance of a class
        """
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show string representation of an instance
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = models.storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Delete an instance based on its ID
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = models.storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
            del models.storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Print string representation of all instances or of instances of a class
        """
        arg_list = args.split()
        obj_list = []
        if not args:
            for obj in models.storage.all().values():
                obj_list.append(str(obj))
        else:
            try:
                eval(arg_list[0])
                for obj in models.storage.all().values():
                    if type(obj) == eval(arg_list[0]):
                        obj_list.append(str(obj))
            except Exception:
                print("** class doesn't exist **")
                return
        print(obj_list)

    def do_update(self, args):
        """
        Update an instance based on its ID
        """
        arg_list = args.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = models.storage.all()[f"{arg_list[0]}.{arg_list[1]}"]
        except KeyError:
            print("** no instance found **")
            return
        except IndexError:
            print("** instance id missing **")
            return
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            setattr(obj, arg_list[2], arg_list[3])
            models.storage.save()

    def do_count(self, args):
        """
        Count instances of a class
        """
        try:
            eval(args)
            count = 0
            for obj in models.storage.all().values():
                if type(obj) == eval(args):
                    count += 1
            print(count)
        except Exception:
            print("** class doesn't exist **")

    def default(self, args):
        """
        Default behavior for non-existing commands
        """
        cmd_list = args.split('.')
        if cmd_list[1] == "all()":
            self.do_all(cmd_list[0])
        elif cmd_list[1] == "count()":
            self.do_count(cmd_list[0])
        elif cmd_list[1][:4] == "show":
            self.do_show(f"{cmd_list[0]} {cmd_list[1][7:-2]}")
        elif cmd_list[1][:7] == "destroy":
            self.do_destroy(f"{cmd_list[0]} {cmd_list[1][10:-2]}")
        elif cmd_list[1][:6] == "update":
            cmd = cmd_list[1][8:-1]
            cmd = cmd.split(", ", 2)
            cmd[2] = cmd[2][1:-1]
            self.do_update(f"{cmd_list[0]} {cmd[0]} {cmd[1]} {cmd[2]}")

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")

    def help_create(self):
        print("Create a new instance of a class")

    def help_show(self):
        print("Show string representation of an instance")

    def help_destroy(self):
        print("Delete an instance based on its ID")

    def help_all(self):
        print("Print string representation of all instances or of instances of a class")

    def help_update(self):
        print("Update an instance based on its ID")

    def help_count(self):
        print("Count instances of a class")

    def help_help(self):
        print("Display help about commands")

    def emptyline(self):
        """
        Empty line handling
        """
        pass

    def help_emptyline(self):
        print("Empty line handling")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

