import time, random, subprocess, math
def banner():
    print(r"""

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
                                    _                         
     _/\_  _ __ _ _ ___ ___ ___ _ _| |_ ___  __ _ _ _  ___ __ 
     >  < | '_ \ '_/ -_|_-</ -_) ' \  _(_-< / _| '_| || \ \ / 
      \/  | .__/_| \___/__/\___|_||_\__/__/ \__|_|  \_,_/_\_\ 
          |_|                                                 """)
class Spam:
    @staticmethod
    def cli_spam(length, timer, message, antiprint="False"):
        try: 
            str(antiprint)
        except (TypeError, NameError, ValueError) as ex:
            return f"antiprint is a nonstr; {ex}"
        try:
            message = str(message)
            length = int(length)
            timer = float(timer) / 1000
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        for i in range(length):
            if antiprint == "False":
                    time.sleep(timer)
                    print(message)
            else:
                for i in range(length):
                    return message
    @staticmethod
    def c_spam(length, timer, operation, seedval, step):
        try:
            length = int(length)
            timer = float(timer) / 1000
            seedval = float(seedval)
            step = float(step)
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        operation = operation.replace("n!", "factorial(n)")
        n = seedval
        q = math.pi
        e = math.e
        for i in range(1, length + 1):
            safe_env = {
                "__builtins__": {},
                "factorial": math.factorial,
                "n": n,
                "π": q,
                "e": e
            } 
            try:
                result = eval(operation, safe_env)
                print(result)
            except Exception as ex:
                print(f"Math error on loop {n}: {ex}")
                break
            n = n + step
            time.sleep(timer)
    @staticmethod
    def r_spam(length, timer, chunk_size, typew, antiprint="False"):
        try: 
            str(antiprint)
        except (TypeError, NameError, ValueError) as ex:
            return f"antiprint is a nonstr; {ex}"
        if typew == "bin":
            try:
                length = int(length)
                timer = float(timer) / 1000
                chunk_size = int(chunk_size)
            except (TypeError, NameError, ValueError) as ex:
                print(f"spam requirements not met, please retry. ERROR == {ex}")
                return "error :/"
            for i in range(length):
                char_list_bin = []
                for ix in range(chunk_size):
                    char_list_bin.append(str(random.randint(0, 1)))
                binstr = "".join(char_list_bin)
                if antiprint == "True":
                    return binstr
                else:
                    print(binstr)
                    time.sleep(timer)
        elif typew == "char":
            try:
                length = int(length)
                timer = float(timer) / 1000
                chunk_size = int(chunk_size)
            except (TypeError, NameError, ValueError) as ex:
                print(f"spam requirements not met, please retry. ERROR == {ex}")
                return "error :/"
            pool = [chr(i) for i in range(33, 127)]
            for i in range(length):
                char_list = []
                for _ in range(chunk_size):
                    char_list.append(random.choice(pool))
                message = "".join(char_list)
                if antiprint == "True":
                    return message
                else:
                    print(message)
                    time.sleep(timer)
    @staticmethod
    def fakeip_spam_four(length, timer):
        try:
            length = int(length)
            timer = float(timer) / 1000
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        for i in range(length):
            a = random.randint(0, 255)
            b = random.randint(0, 255)
            c = random.randint(0, 255)
            d = random.randint(0, 255)
            print(f"IPV4: {a}.{b}.{c}.{d}")
            time.sleep(timer)
    @staticmethod
    def fakeip_spam_six(length, timer):
        try:
            length = int(length)
            timer = float(timer) / 1000
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        for i in range(length):
            groups = [f"{random.randint(0, 65535):04x}" for _ in range(8)]
            ipv6_address = ":".join(groups)
            print(f"IPV6: {ipv6_address}")
            time.sleep(timer)
    @staticmethod
    def v_spam(length, timer, message):
        try:
            message = str(message)
            length = int(length)
            timer = float(timer)
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        formal_letter = f"say {message}"
        for i in range(length):
            time.sleep(timer)
            subprocess.run(formal_letter, shell=True)
    @staticmethod
    def variation_spam(variations, length, timer, method):
        try:
            variations = int(variations)
            length = int(length)
            timer = float(timer) / 1000
            method = str(method)
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        nxyx = []
        for i in range(variations):
            yxnx = input(f"What is your variation? ({i}) ")
            nxyx.append(yxnx)
        if method == "simple":
            for i in range(length):
                time.sleep(timer)
                print(*nxyx, sep='\n')
        elif method == "complex":
            n = 0
            while length > n:
                time.sleep(timer)
                print(*nxyx, sep ='\n')
                n = n + length
    @staticmethod
    def py_spam(length, timer, code, antiprint="False"):
        try: 
            str(antiprint)
        except (TypeError, NameError, ValueError) as ex:
            return f"antiprint is a nonstr; {ex}"
        try:
            code = str(code)
            length = int(length)
            timer = float(timer) / 1000
        except (TypeError, NameError, ValueError) as ex:
            print(f"spam requirements not met, please retry. ERROR == {ex}")
            return "error :/"
        code.strip("rm -rf /")
        code = rf"{code}"
        if antiprint == "False":
            for i in range(length):
                time.sleep(timer)
                exec(code)
        else:
            for i in range(length):
                return exec(code)
class Detailer:
    @staticmethod
    def detailer():
        print("""
cli_spam(length, timer, message)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
message = str()\n
""")  
    @staticmethod
    def xdetailer():
        print("""
c_spam(length, timer, operation)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
operation = exp()\n
seedval = val()\n
step = +step()\n
""")
    @staticmethod
    def ydetailer():
        print("""
r_spam(length, timer, chunk_size)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
chunk = char_length()\n
spamType™ = bin or char (01 or UTF)\n
""")
    @staticmethod
    def fakeipdetailer():
        print("""
ip_spam(length, timer, ips)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
ips = amount() (+ = ipv4, * = ipv6)\n
""")
    @staticmethod
    def vdetailer():
        print("""
v_spam(length, timer, message)\n
length = range() (KEEP THIS LOW BECAUSE THE WORDS WILL BE SPOKEN OUT LOUD BY THE TERMINAL)\n
timer = time.sleep(timer * seconds)\n
message = str()\n
""")
    @staticmethod
    def vardetailer():
        print("""
variation_spam(variation, length, timer, count_dracula)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
chunk = char_length()\n
type™ = str() = count_dracula\n
""")
    @staticmethod
    def pydetailer(): 
        print("""
py_spam(code, timer, message)\n
length = range()\n
timer = time.sleep(timer * milliseconds)\n
code = str() (this can be multiple lines, unlike the other ones, this payload is better. For the sake of it being easier to do, the code has to be in python3\n
""")
class Caller:
    @staticmethod
    def caller():
        while True:
            Detailer.detailer()
            x = input("lines? ")
            y = input("delay (ms)? ")
            z = input("message? ")
            if z == "quit(quit)":
                break
            Spam.cli_spam(x, y, z)
    @staticmethod
    def xcaller():
        while True:
            Detailer.xdetailer()
            x = input("lines? ")
            y = input("delay (ms)? ")
            z = input("operation? ")
            zz = input("seed value? ")
            zzz = input("step? ")
            if z == "quit":
                break
            Spam.c_spam(x, y, z, zz, zzz)
    @staticmethod
    def ycaller():
        while True:
            Detailer.ydetailer()
            x = input("lines? ")
            y = input("delay (ms)? ")
            z = input("length? ")
            zz = input("what is your spamType™? ")
            if zz == "quit":
                break
            Spam.r_spam(x, y, z, zz)
    @staticmethod
    def fakeipcaller():
        while True:
            Detailer.fakeipdetailer()
            x = input("lines? ")
            y = input("delay (ms)? ")
            z = input("ipv4 or ipv6 or dip? (+ / * / y) ")
            if z == "+":
                Spam.fakeip_spam_four(x, y)
            elif z == "*":
                Spam.fakeip_spam_six(x, y)
            elif z == "y":
                break
    @staticmethod
    def vcaller():
        while True:
            Detailer.vdetailer()
            x = input("length (times spoken)? ")
            y = input("delay (sec? ")
            z = input("message? ")
            print("If it goes haywire, you can call killer()")
            if z == "quit":
                break
            Spam.v_spam(x, y, z)
    @staticmethod
    def varcaller():
        while True:
            Detailer.vardetailer()
            print("this feature requires a lot of typing")
            w = input("variations? ")
            x = input("lines? ")
            y = input("delay? (ms) ")
            z = input("type? ")
            Spam.variation_spam(w, x, y, z)
    def pycaller():
        while True:
            Detailer.pydetailer()
            x = input("lines? ")
            y = input("delay? (ms) ")
            print("Paste your code below. Press Enter on a blank line to execute:")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            z = "\n".join(lines)
            Spam.py_spam(x, y, z)
class Subx:
    @staticmethod
    def clearer():
        subprocess.run(["clear"])
    @staticmethod
    def gitxploit(commit_amount_display_and_this_variable_is_going_to_be_reallly_really_big):
        subprocess.run(["git", "status"])
        subprocess.run(["git", "log", "-n", commit_amount_display_and_this_variable_is_going_to_be_reallly_really_big])
    @staticmethod
    def gitwcommiter():
        x = input("Commit message? ")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", x])
    @staticmethod
    def killer():
        subprocess.run(["killall", "say"])
