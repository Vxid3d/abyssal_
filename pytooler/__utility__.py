import math, time, sys, getpass, json; from pathlib import Path
username = getpass.getuser()
sys.path.append(f"/Users/{username}/abyssal/")
from verse import crux
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
def convert_temp(val, unit):
    if unit.upper() == 'C':
        return (val * 9/5) + 32
    elif unit.upper() == 'F':
        return (val - 32) * 5/9
    return None
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    return True
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
def password_gen(length):
    crux.Spam.r_spam(1, 0, length, "char")
def change(text, delay, amount):
    for i in range(amount):
        print(f"Counter: {i}", end="\r", flush=True)
        time.sleep(delay / 1000)
def tr(num):
    return num * (num + 1) // 2
def term(start, terms, diff):
    return start + (terms-1) * diff
def sq_repeat(times):
    return [i * i for i in range(1, times + 1)]
def cu_repeat(times):
    return [i * i * i for i in range(1, times + 1)]
def sum_term(start, terms, diff):
    return terms * (2 * start + (terms - 1) * diff) // 2
def fact(num):
    return math.factorial(num)
def fib(numbers):
    a, b = 0, 1
    result = []
    for _ in range(numbers + 1):
        result.append(a)
        a, b = b, a + b
    return result
def sqrt_repeat(times):
    if times < 0: return ""
    return [math.sqrt(i) for i in range(times)]
def cbrt_repeat(times):
    if times < 0: return ""
    return [math.cbrt(i) for i in range(times)]
def sq(num):
    return num * num
def cu(num):
    return num * num * num
def sqrt(num):
    if num < 0: return ""
    return math.sqrt(num)
def cbrt(num):
    if num < 0: return ""
    return math.cbrt(num)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def bin_calc(a, b, op: str):
    a, b = int(a, 2), int(b, 2)
    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a // b if b != 0 else None
    }
    if op not in ops:
        raise ValueError("Invalid operator")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Division by zero")
    r = ops[op]
    return bin(r)[2:], r
def bincon(x, priority="dec"):
    if priority == "dec":
        return int(str(x), 2)
    if priority == "bin":
        n = int(x)
        return bin(n)[2:], n
    raise ValueError("priority must be 'bin' or 'dec'")
class Json:
    def _resolve_path(filename, folder_path):
        module_dir = Path(__file__).resolve().parent
        cwd = Path.cwd()
        filename = Path(filename).name.replace("/", "_").replace("\\", "_")
        folder_path = folder_path.strip()
        if folder_path == "":
            base = cwd
        elif folder_path == "-":
            base = module_dir
        else:
            base = Path(folder_path)
        if str(base) == "/":
            base = cwd
        return base / f"{filename}.json"
    def init_save(user_input, filename="savefile", folder_path=""):
        path = Json._resolve_path(filename, folder_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = [{"input": user_input}]
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"[INIT] Saved to: {path.resolve()}")
    def append_save(user_input, filename="savefile", folder_path=""):
        path = Json._resolve_path(filename, folder_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            try:
                with open(path, "r") as file:
                    data = json.load(file)
                    if not isinstance(data, list):
                        data = [data]
            except json.JSONDecodeError:
                data = []
        else:
            data = []
        data.append({"input": user_input})
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"[APPEND] Saved to: {path.resolve()}")
