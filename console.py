#!/usr/bin/python3
"""Entry point module for the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Console commande class"""

    prompt = "(hbnb) "
    classes = ['BaseModel']
    cmnd = ['create', 'show', 'destroy', 'all', 'update']

    def do_create(self, cls):
        """Create new instance of cls and saves it"""
        if not cls:
            print("** class name missing **")
        elif cls not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dic = {'BaseModel': BaseModel}
            model = dic[cls]()
            print(model.id)
            model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.classes:
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
        """ Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        if args[0] not in HBNBCommand.classes:
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
        or not on the class name"""
        all_objs = storage.all()
        list_inst = []

        if not arg:
            for (k, v) in all_objs.items():
                list_inst.append(v.__str__())
            print(list_inst)
        else:
            args = arg.split(' ')
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for (k, v) in all_objs.items():
                    cls_name = v.__class__.__name__
                    if cls_name == args[0]:
                        list_inst.append(v.__str__())
                print(list_inst)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return
        argv = ""
        for ar in arg.split(','):
            argv += ar
        args = shlex.split(argv)

        if args[0] not in HBNBCommand.classes:
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
                        print("** value missing **")
                    else:
                        setattr(v, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """Exit the program: Quit"""
        return True

    def do_EOF(self, line):
        """Exit the program: EOF or ^D"""
        return True

    def emptyline(self):
        """empty line command: do nothing"""
        pass

    def help_help(self):
        """Docummentation for help command"""
        print("Command descriptor")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
