from cryptography.fernet import Fernet
import base64
import hashlib
import logging
from pathlib import Path
from .compressor import FileCompressor
from .utils import load_config, save_config
from ..config import settings

class AdvancedFileEncryptor:
    def __init__(self):
        self.config = load_config()
        self.compressor = FileCompressor()
        
    def generate_key(self, password):
        return base64.urlsafe_b64encode(
            hashlib.pbkdf2_hmac(
                'sha256', 
                password.encode(), 
                settings.DEFAULT_SALT,
                settings.KEY_ITERATIONS
            )
        )

    def process_file(self, file_path, password, compress=True, compression_method='zlib'):
        """Process file with compression and encryption"""
        try:
            # First compress if enabled
            if compress:
                compressed_path = self.compressor.compress_file(
                    file_path, 
                    method=compression_method
                )
                file_to_encrypt = compressed_path
            else:
                file_to_encrypt = file_path
                
            # Then encrypt
            return self.encrypt_file(file_to_encrypt, password)
            
        except Exception as e:
            logging.error(f"Processing error: {str(e)}")
            raise

    # ... (rest of encryption/decryption methods) 