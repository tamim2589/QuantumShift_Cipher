# QuantumShift_Cipher
# 🔐 QuantumShift Cipher

A simplified, reversible encryption algorithm written in Python. The **QuantumShift Cipher** applies a position-aware transformation with XOR masking, ensuring lightweight and perfectly reversible encryption—ideal for educational, demonstrative, or obfuscation purposes.

## 🚀 Features

- Easy to understand and implement
- Perfectly reversible (lossless decryption)
- Byte-safe (works with all 256 ASCII values)
- No external dependencies

## 📜 Algorithm Description

### QuantumShift Encrypt

**Input:** `plaintext` (string), `key` (integer 0-255)  
**Output:** `ciphertext` (hexadecimal string)

**Steps:**
1. For each character at position `i` in the plaintext:
    - Convert character to ASCII value: `val`
    - Apply rotation: `rotated = (val + key + i) % 256`
    - Derive mask: `mask = (key + i) % 256`
    - Encrypt with XOR: `encrypted = rotated ^ mask`
    - Convert to 2-digit hex and append to output

### QuantumShift Decrypt

**Input:** `ciphertext` (hex string), `key` (integer 0-255)  
**Output:** `plaintext` (original string)

**Steps:**
1. Split the hex string into byte values
2. For each byte at position `i`:
    - Convert from hex to integer: `encrypted`
    - Revert XOR: `rotated = encrypted ^ ((key + i) % 256)`
    - Undo rotation: `val = (rotated - key - i) % 256`
    - Convert back to character

## 🧪 Example

```python
def quantum_shift_encrypt(plaintext: str, key: int) -> str:
    ciphertext = []
    for i, char in enumerate(plaintext):
        val = ord(char)
        rotated = (val + key + i) % 256
        encrypted = rotated ^ ((key + i) % 256)
        ciphertext.append(f"{encrypted:02x}")
    return ' '.join(ciphertext)

def quantum_shift_decrypt(ciphertext_hex: str, key: int) -> str:
    plaintext = []
    hex_values = ciphertext_hex.split()
    
    for i, hex_val in enumerate(hex_values):
        encrypted = int(hex_val, 16)
        rotated = encrypted ^ ((key + i) % 256)
        val = (rotated - key - i) % 256
        plaintext.append(chr(val))
    return ''.join(plaintext)

# Test the cipher
if __name__ == "__main__":
    key = 42
    plaintext = "Hello, QuantumShift!"
    ciphertext = quantum_shift_encrypt(plaintext, key)
    decrypted = quantum_shift_decrypt(ciphertext, key)

    print("Original:", plaintext)
    print("Encrypted (hex):", ciphertext)
    print("Decrypted:", decrypted)
    print("Decryption correct:", decrypted == plaintext)
