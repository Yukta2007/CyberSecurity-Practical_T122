import hmac
import hashlib

# Function to generate MAC
def generate_mac(message, secret_key):
    mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return mac

# Function to verify MAC
def verify_mac(message, secret_key, received_mac):
    generated_mac = generate_mac(message, secret_key)

    # Secure comparison
    if hmac.compare_digest(generated_mac, received_mac):
        return True
    else:
        return False


# ---------------- MAIN PROGRAM ----------------

message = input("Enter the message: ")
secret_key = input("Enter the secret key: ")

# Generate MAC
mac = generate_mac(message, secret_key)

print("\nGenerated MAC:")
print(mac)

# Verification
print("\n--- MAC Verification ---")
received_mac = input("Enter the MAC to verify: ")

if verify_mac(message, secret_key, received_mac):
    print(" MAC Verified Successfully!")
    print("Data Integrity and Authenticity are Confirmed.")
else:
    print(" MAC Verification Failed!")
    print("Message may have been modified or the key is incorrect.")
