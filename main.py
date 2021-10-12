import math

global verbose
verbose = False

def isPrime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, n):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False


def encrypt():
    n = 0
    e = 0
    print("[1] Calculate\n[2] Manually enter n & e")
    ch = int(input())
    if ch == 1:
        while True:
            print("Select p: ")
            p = int(input())
            if isPrime(p):
                break
            print("p has to be Prime")
        while True:
            print("Select q: ")
            q = int(input())
            if isPrime(q):
                break
            print("p has to be Prime")

        n = p * q
        phin = math.lcm(p-1, q-1)

        while True:
            print("Choose e:")
            e = int(input())
            if math.gcd(n, e) != 1:
                print(f"{e} is not coprime with {n}")
                continue
            elif not isPrime(e):
                print(f"{e} is not a prime")
                continue
            break
             
        d = pow(e, -1, phin)

        if verbose:
            print(f"n => p * q => {p} * {q} = {n}\nphi(n) => lcm(p-1, q-1) => lcm({p-1}, {q-1}) => {phin}\ne => {e}\nd => e^-1 mod phi(n) => {e}^-1 mod {phin} => {d}\n")
    elif ch == 2:
        print("n:")
        n = int(input())
        print("e:")
        e = int(input())
    else:
        print("Unrecognized input (Use either 1 or 2)")
        return
    print("Message you wish to encrypt:")
    msg = input()

    cm = list()

    for ch in msg:
        cm.append(pow(ord(ch), e) % n)
        if verbose:
            print(f"{ch} in ascii is: {ord(ch)}")

    print("Complete encrypted message string:")
    for i in cm:
        print(f"|{i}", end="")
    print("|")
    print(f"n: [{n}]\ne: [{e}]", end="")
    if ch == 1:
        print(f"\nd: [{d}]")
    else:
        print("")


def decrypt():
    print("d:")
    d = int(input())
    print("n:")
    n = int(input())
    print("Input encrypted message(split by \'|\'):")
    cm = list(map(int, input().split('|')))
    
    m = list()
    for c in cm:
        m.append(pow(c, d) % n)
        if verbose:
            print(f"Encoded: [{c}] to decoded: [{pow(c, d) % n}] aka character: {chr(pow(c, d) % n)}")
    
    print("Completely decoded: ", end="")
    for i in m:
        print(chr(i), end="")
    print("")


while True:
    print(f"[E]ncrypt or [D]ecrypt? [v: {verbose}]")
    choice = input()
    if choice.lower() == 'e':
        encrypt()
        #break
    elif choice.lower() == 'd':
        decrypt()
        #break
    elif choice.lower() == 'q' or choice.lower() == 'quit':
        break
    elif choice.lower() == 'v' or choice.lower() == 'verbose':
        if verbose:
            print("Verbose output has been turned off")
            verbose = False
        else:
            print("Verbose output has been turned on")
            verbose = True
    else:
        print("Unrecognized input. (Use e or d, q to quit)")