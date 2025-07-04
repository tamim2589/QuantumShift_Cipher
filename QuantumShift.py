def quantum_shift_encrypt(plaintext: str, key: int) -> str:
    """
    Simplified and reliable encryption algorithm
    """
    ciphertext = []
    for i, char in enumerate(plaintext):
        # Simple operations that can be perfectly reversed
        val = ord(char)
        # Position-dependent rotation
        rotated = (val + key + i) % 256
        # XOR with key-derived value
        encrypted = rotated ^ ((key + i) % 256)
        ciphertext.append(f"{encrypted:02x}")
    return ' '.join(ciphertext)

def quantum_shift_decrypt(ciphertext_hex: str, key: int) -> str:
    """
    Perfect inverse of the encryption algorithm
    """
    plaintext = []
    hex_values = ciphertext_hex.split()
    
    for i, hex_val in enumerate(hex_values):
        encrypted = int(hex_val, 16)
        # Reverse XOR
        rotated = encrypted ^ ((key + i) % 256)
        # Reverse rotation
        val = (rotated - key - i) % 256
        plaintext.append(chr(val))
    return ''.join(plaintext)

# Test case with verification
if __name__ == "__main__":
    key = 42  # Try different keys (0-255)
    plaintext = "Hello, QuantumShift!"
    
    print(f"Original: {plaintext}")
    print(f"Original (hex): {' '.join(f'{ord(c):02x}' for c in plaintext)}")
    
    # Encryption
    ciphertext = quantum_shift_encrypt(plaintext, key)
    print(f"Encrypted (hex): {ciphertext}")
    
    # Decryption
    decrypted = quantum_shift_decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Decrypted matches original: {decrypted == plaintext}")
