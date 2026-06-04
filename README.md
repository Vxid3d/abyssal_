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
```bash
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
```Python
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
```Python
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
Guide.md link: https://github.com/Vxid3d/abyssal_/blob/main/GUIDE.md
proud to be made 100% in





![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=black)
