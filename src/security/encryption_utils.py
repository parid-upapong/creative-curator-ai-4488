from cryptography.fernet import Fernet
import os

class DataHarnering:
    """
    Utility for encrypting sensitive fields within the JSON-C schema
    and User PII before database insertion.
    """
    def __init__(self, master_key: Optional[bytes] = None):
        # In production, this key is retrieved from a Key Management Service (KMS)
        self.key = master_key or os.getenv("ENCRYPTION_KEY", Fernet.generate_key())
        self.cipher_suite = Fernet(self.key)

    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypts PII or sensitive metadata."""
        if not data:
            return data
        return self.cipher_suite.encrypt(data.encode()).decode()

    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """Decrypts data for processing within the secure enclave."""
        if not encrypted_data:
            return encrypted_data
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()

# Example: Hardening the JSON-C Portfolio
# json_c_data["metadata"]["owner_email"] = security.encrypt_sensitive_data("creator@email.com")