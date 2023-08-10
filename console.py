#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles Ctrl+D"""
        print()
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        instances = models.storage.all()
        if not arg:
            print([str(v) for v in instances.values()])
        elif args[0] in models.classes:
            print([str(v) for k, v in instances.items() if args[0] in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = models.storage.all()[key]
                setattr(obj, args[2], args[3])
                models.storage.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            instances = models.storage.all()
            count = len([v for k, v in instances.items() if args[0] in k])
            print(count)

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self
        """Exits the program"""
        return True

    def do_help(self, arg):
        """Provides help information for commands"""
        cmd.Cmd.do_help(self, arg)

    def default(self, line):
        """Handles default behavior for unknown commands"""
        args = line.split(".")
        if len(args) > 1 and args[1] == "all()":
            self.do_all(args[0])
        elif len(args) > 1 and args[1] == "count()":
            self.do_count(args[0])
        elif len(args) > 1 and args[1].startswith("show("):
            id_start = args[1].index("(") + 2
            id_end = args[1].index(")") - 1
            obj_id = args[1][id_start:id_end]
            self.do_show(args[0] + " " + obj_id)
        elif len(args) > 1 and args[1].startswith("destroy("):
            id_start = args[1].index("(") + 2
            id_end = args[1].index(")") - 1
            obj_id = args[1][id_start:id_end]
            self.do_destroy(args[0] + " " + obj_id)
        elif len(args) > 1 and args[1].startswith("update("):
            parts = args[1].split(", ")
            id_start = parts[0].index("(") + 2
            id_end = parts[0].index(")") - 1
            obj_id = parts[0][id_start:id_end]
            attr_name = parts[1][1:-1]
            attr_value = parts[2][1:-1]
            self.do_update(args[0] + " " + obj_id + " " + attr_name + " " + attr_value)

    def precmd(self, line):
        """Pre-processes command line"""
        parts = line.split(".")
        if len(parts) > 1 and parts[1].startswith("update("):
            new_line = parts[1].replace(", ", ",")
            return "{}.{}".format(parts[0], new_line)
        return line

if __name__ == "__main__":
    HBNBCommand().cmdloop()

