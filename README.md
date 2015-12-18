MyShell - Python library for creating shells.
=============================================

MyShell is a small python library for creating basic shells/menus.

Features
========

* Easy to develop with.
* Auto-complete
* Support python 2 and 3.

How to
======

* Basic shell
```python
"""
 This function called in myshell.shell_add_option,
 and will be executed when the user enter the option.

 args - args[0], args[1] etc... the command line arguments,
 passed by the user.

 every function needs (args) !
"""

def print_database(args):
    if args[0] == "--help":
        print("Hey help")
    print("Database!")


"""
    This will create a basic shell interface.
"""
def shell():
    myshell.shell_add_option("list",   "List files", print_database)
    myshell.shell_add_option("get",    "get files", print_database)
    myshell.shell_add_option("dl", "download files", print_database)
    myshell.shell_add_option("upload", "upload files", print_database)
    """
        Starts the shell.
    """
    myshell.shell_shell()
```

* Basic yes/no menu:

```python
"""
 This will create a basic yes/no menu.
"""
def menu():
    """
        0 - for yes/no menu.
        1 - for list menu for example:
            1) red
            2) blue
            3) yellow
    """
    menu = myshell.Menu(0)
    menu.add_entry("Do you want to continue? ", print_database)
    menu.show()
    value = menu.run("> Please select answer")
    print("You selected: %s" %value)
```

That's easy!

Contributing
=============

Contributions are very welcome!

1. fork the repository
2. clone the repo (git clone git@github.com:USERNAME/myshell.git)
3. make your changes
6. Add yourself in contributors.txt
4. push the repository
5. make a pull request

Thank you - and happy contributing!

Copying
========

###### Copyright 2015 (C) Hypsurus <hypsurus@mail.ru>
###### License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.

