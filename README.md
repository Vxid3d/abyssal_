```text
                                                                       $$$$$             $$$$$                                                                        
                      bbbbbbbb                                         $:::$             $:::$                                                                        
                      b::::::b                                     $$$$$:::$$$$$$    $$$$$:::$$$$$$                   LLLLLLLLLLL                                     
         @@@@@@@@@    b::::::b                                   $$::::::::::::::$ $$::::::::::::::$     @@@@@@@@@    L:::::::::L                                     
       @@:::::::::@@  b::::::b                                  $:::::$$$$$$$::::$$:::::$$$$$$$::::$   @@:::::::::@@  L:::::::::L                                     
     @@:::::::::::::@@ b:::::b                                  $::::$       $$$$$$::::$       $$$$$ @@:::::::::::::@@LL:::::::LL                                     
    @:::::::@@@:::::::@b:::::bbbbbbbbb yyyyyyy           yyyyyyy$::::$            $::::$            @:::::::@@@:::::::@ L:::::L                                       
    @::::::@   @::::::@b::::::::::::::bby:::::y         y:::::y $::::$            $::::$            @::::::@   @::::::@ L:::::L                                       
    @:::::@  @@@@:::::@b::::::::::::::::by:::::y       y:::::y  $:::::$$$$$$$$$   $:::::$$$$$$$$$   @:::::@  @@@@:::::@ L:::::L                                       
    @:::::@  @::::::::@b:::::bbbbb:::::::by:::::y     y:::::y    $$::::::::::::$$  $$::::::::::::$$ @:::::@  @::::::::@ L:::::L                                       
    @:::::@  @::::::::@b:::::b    b::::::b y:::::y   y:::::y       $$$$$$$$$:::::$   $$$$$$$$$:::::$@:::::@  @::::::::@ L:::::L                                       
    @:::::@  @:::::::@@b:::::b     b:::::b  y:::::y y:::::y                 $::::$            $::::$@:::::@  @:::::::@@ L:::::L                                       
    @:::::@  @@@@@@@@  b:::::b     b:::::b   y:::::y:::::y                  $::::$            $::::$@:::::@  @@@@@@@@   L:::::L                                       
    @::::::@           b:::::b     b:::::b    y:::::::::y       $$$$$       $::::$$$$$$       $::::$@::::::@            L:::::L         LLLLLL                        
    @:::::::@@@@@@@@   b:::::bbbbbb::::::b     y:::::::y        $::::$$$$$$$:::::$$::::$$$$$$$:::::$@:::::::@@@@@@@@  LL:::::::LLLLLLLLL:::::L                        
     @@:::::::::::::@  b::::::::::::::::b       y:::::y         $::::::::::::::$$ $::::::::::::::$$  @@:::::::::::::@ L::::::::::::::::::::::L                        
       @@:::::::::::@  b:::::::::::::::b       y:::::y           $$$$$$:::$$$$$    $$$$$$:::$$$$$      @@:::::::::::@ L::::::::::::::::::::::L                        
         @@@@@@@@@@@   bbbbbbbbbbbbbbbb       y:::::y                 $:::$             $:::$            @@@@@@@@@@@  LLLLLLLLLLLLLLLLLLLLLLLL                        
                                             y:::::y                  $$$$$             $$$$$                                                 ________________________
                                            y:::::y                                                                                           _::::::::::::::::::::::_
                                           y:::::y                                                                                            ________________________
                                          y:::::y                                                                                                                     
                                         yyyyyyy 
```
a python framework (unorganized) for make python easier to work with.
# Setup
## this is the format you want to format your code (from the repo) in.
```text
.
├── pytooler
│   ├── __init__.py
│   ├── __utility__.py
│   └── color.py
└── verse
    ├── __init__.py
    ├── crux.py
    └── test.py
  ^ folder name: abyssal, path = /Users/_______/abyssal
  _______ = your username
  ## read the GUIDE.md to find out how to use this.
```
### sample code: (if path not in /abyssal/___)
```text
from abyssal.pytooler import __utility__ as u,  color as c
from abyssal.verse import crux
crux.Spam.cli_spam(
    100,
    100,
    "hi"
    )
listx = [1,2,3,4,5,6,7,8,9,10]
u.binary_search(listx, 7)
print(f"{c.RED} hi {c.RESET}")
```
### sample code: (if path in /abyssal/__)
```text
import getpass, sys
username = getpass.getuser()
sys.path.append(f"/Users/{username}/abyssal/")
from pytooler import __utility__ as u,  color as c
from verse import crux
crux.Spam.cli_spam(
    100,
    100,
    "hi"
    )
listx = [1,2,3,4,5,6,7,8,9,10]
u.binary_search(listx, 7)
print(f"{c.RED} hi {c.RESET}")
```
