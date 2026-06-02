# a wrapper for crux.py
import crux
while True:
    x = input("vort3n: What test? >>>>> ")
    if x == "spamer":
        crux.Caller.caller()
    elif x == "calcspamer":
        crux.Caller.xcaller()
    elif x == "randspamer":
        crux.Caller.ycaller()
    elif x == "IPspamer":
        crux.Caller.fakeipcaller()
    elif x == "voicespamer":
        crux.Caller.vcaller()
    elif x == "varspamer":
        crux.Caller.varcaller()
    elif x == "pyspamer":
        crux.Caller.pycaller()
    elif x == "clear":
        crux.Subx.clearer()
    elif x == "info":
        crux.Subx.gitxploit()
    elif x == "commit":
        try:
            t = int(input("Enter the amount of commits you want to display: "))
        except (ValueError) as e:
            print(f"Here is where you went wrong: {e}")
        crux.Subx.gitwcommiter(t)
    elif x == "killer":
        crux.Subx.killer()
    elif x == "banner":
        crux.banner()
    elif x == "quit":
        break
