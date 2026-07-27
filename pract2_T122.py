import math
print("Yukta Sonawane T122")
# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Modular Inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Encryption
def encrypt(message, e, n):
    return [pow(ord(ch), e, n) for ch in message]

# Decryption
def decrypt(cipher, d, n):
    return ''.join(chr(pow(c, d, n)) for c in cipher)


print("====== RSA Algorithm ======\n")

p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime.")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

e = int(input(f"Enter Public Key (e) (1 < e < {phi}): "))

if gcd(e, phi) != 1:
    print("e must be coprime with φ(n).")
    exit()

d = mod_inverse(e, phi)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

message = input("\nEnter Message: ")

cipher = encrypt(message, e, n)

print("\nEncrypted Message:")
print(cipher)

plain = decrypt(cipher, d, n)

print("\nDecrypted Message:")
print(plain)
