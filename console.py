#!/usr/bin/python3
"""Entry point module for the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Console commande class"""

    prompt = "(hbnb) "
    dic = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }
    cmnd = ['create', 'show', 'destroy', 'all', 'update', 'count']

    def precmd(self, arg):
        """ Parse imput and returns cmd with arg"""
        if '.' in arg and '(' in arg and ')' in arg:
            clas = arg.split('.')
            cmand = clas[1].split('(')
            args = cmand[1].split(')')
            if clas[0] in HBNBCommand.dic.keys() and \
               cmand[0] in HBNBCommand.cmnd:
                arg = cmand[0] + ' ' + clas[0] + ' ' + args[0]
        return arg

    def do_create(self, cls):
        """Create new instance of cls and saves it
        (type create <class_name>)
        """
        if not cls:
            print("** class name missing **")
        elif cls not in HBNBCommand.dic.keys():
            print("** class doesn't exist **")
        else:
            model = HBNBCommand.dic[cls]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name
        (type show <class_name> <obj_id>)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.dic.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for (k, v) in all_objs.items():
                cls_name = v.__class__.__name__
                obj_id = v.id
                if cls_name == args[0] and obj_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (type destroy <class_name> <obj_id>)
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.dic.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for (k, v) in all_objs.items():
                cls_name = v.__class__.__name__
                obj_id = v.id
                if cls_name == args[0] and obj_id == args[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("**no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name
        (type all or all <class_name>)
        """
        all_objs = storage.all()
        list_inst = []

        if not arg:
            for (k, v) in all_objs.items():
                list_inst.append(v.__str__())
            print(list_inst)
        else:
            args = arg.split(' ')
            if args[0] not in HBNBCommand.dic.keys():
                print("** class doesn't exist **")
            else:
                for (k, v) in all_objs.items():
                    cls_name = v.__class__.__name__
                    if cls_name == args[0]:
                        list_inst.append(v.__str__())
                print(list_inst)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (type update <class_name> <obj_id> <attribute> <attribute_value>)
        """
        if not arg:
            print("** class name missing **")
            return
        argv = ""
        for ar in arg.split(','):
            argv += ar
        args = shlex.split(argv)
        if args[0] not in HBNBCommand.dic.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for (k, v) in all_objs.items():
                cls_name = v.__class__.__name__
                obj_id = v.id
                if cls_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        if isinstance(args[2], dict):
                            for (ke, va) in args[2].items():
                                setattr(v, ke, va)
                                v.save()
                        else:
                            print("** value missing **")
                    else:
                        setattr(v, args[2], args[3])
                        v.save()
                    return
            print("** no instance found **")

    def do_count(self, arg):
        """ Counts and prints the number of instances of a class
        (type count <class_name>)
        """
        all_objs = storage.all()

        count = 0
        for k, v in all_objs.items():
            cls_name = v.__class__.__name__
            if cls_name == arg:
                count += 1
        print(count)

    def do_quit(self, line):
        """Exit the program: (type quit)"""
        return True

    def do_EOF(self, line):
        """Exit the program: (type EOF or ^D)"""
        return True

    def emptyline(self):
        """empty line command: do nothing"""
        pass

    def help_help(self):
        """Docummentation for help command"""
        print("Command descriptor")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
