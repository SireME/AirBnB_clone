#!/usr/bin/python3
'''This repo contains Methods for the Command Interpreter'''
import cmd
import json
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter to manage the airbnb project
    """
    prompt = '(hbnb) '
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, args):
        '''Create a new instance of BaseModel, save it and prints the id
           Usage: create <class name>
        '''
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + '()')
            new_instance.save()
            # models.storage.save() direct save
            print(new_instance.id)

    def do_show(self, args):
        '''Prints the string representation of a specific instance
           Usage: show <class name> <id>
        '''
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        '''Delete an instance
           Usage: destroy <class name> <id>
        '''
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        '''Print a string representation of all instances
           Usage: all <class name>
        '''
        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        '''update an instance
           Usage update <class name> <id> <attribute name> "<attribute value>"
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def precmd(self, line):
        """
        intercept string input and process command to run
        command accordingly ex: User.all()
        """
        try:
            instances = models.storage.all()
            new_line = line[:]
            _class = new_line.split(".")
            cn = _class  # make classname shorter
            if _class[0] in HBNBCommand.__classes:
                if _class[1] == "all()":
                    #  retrieve all instances of class className.all()
                    to_print = []
                    for key, obj in instances.items():
                        if key.split(".")[0] == _class[0]:
                            to_print.append(str(obj))
                    #  format and print all retrieved instances
                    print("[" + ", ".join(to_print) + "]")

                elif _class[1] == "count()":
                    count = 0  # retrieve number of specific instance of class
                    for key in instances.keys():
                        if key.split(".")[0] == _class[0]:
                            count += 1
                    print(count)

                elif cn[1][0:5] + cn[1][-1] == "show()":
                    class_id = cn[1].split("(")[1].split(")")[0][1:-1]
                    class_name = cn[0]
                    s_format = class_name + " " + class_id
                    self.do_show(s_format)

                elif cn[1][0:8] + cn[1][-1] == "destroy()":
                    class_id = cn[1].split("(")[1].split(")")[0][1:-1]
                    class_name = cn[0]
                    s_format = class_name + " " + class_id
                    self.do_destroy(s_format)

                elif cn[1][0:7] + cn[1][-1] == "update()":
                    st = cn[1].split("(")[1].split(")")[0]  # string in ()
                    dic_o = st  # store input for possible dic manipulatxn
                    st = st.split(",")  # string broken at ","
                    st_id = st[0][1:-1]  # string Id extraction
                    st_aname = st[1][2:-1]  # attribute name extraction
                    st_avalue = None  # init value for conditional
                    if st[2][1] == '"' and st[2][-1] == '"':
                        st_avalue = st[2][1:]  # when value is a string
                    else:
                        st_avalue = st[2][1:]  # when value is a number
                    class_name = cn[0]
                    s_format = class_name + " " + st_id + " " + st_aname
                    s_format += " " + st_avalue  # format for do_update method
                    if cn[1][-2] == "}":
                        dic_r = "{" + dic_o.split("{")[1][:-1] + "}"
                        dic_r = dic_r.replace("'", '"')  # fmt inpt str for jsn
                        dic_r = json.loads(dic_r)
                        for key, value in dic_r.items():
                            # format for do_update function
                            s_format = class_name + " " + st_id + " "
                            s_format += str(key) + " " + str(value)
                            # run the do_update method
                            self.do_update(s_format)
                    else:
                        self.do_update(s_format)  # run the do_update method

        except Exception as a:
            print(a)
        return line

    def default(self, line):
        """
        handle error message not displaying it
        when a . parameter is passed ex User.all()
        """
        line_list = line.split(".")[0]
        if line_list in HBNBCommand.__classes:
            pass
        else:
            print(f"*** Unknown syntax: {line}")

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
