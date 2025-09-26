import os
import ecdsa
import hashlib

def generate_eth_wallet():
    # Generate random 32-byte private key
    private_key = os.urandom(32).hex()

    # Create public key
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key.to_string()

    # Ethereum address = last 20 bytes of keccak256(public_key)
    public_key_bytes = b"\x04" + vk  # uncompressed format
    keccak_hash = hashlib.new("sha3_256", public_key_bytes).digest()
    address = "0x" + keccak_hash[-20:].hex()

    return private_key, address

if __name__ == "__main__":
    priv, addr = generate_eth_wallet()
    print("New Ethereum Wallet Generated 🔑")
    print(f"Private Key: {priv}")
    print(f"Address: {addr}")
