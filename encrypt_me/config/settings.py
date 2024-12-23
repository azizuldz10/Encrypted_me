import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Encryption settings
ENCRYPTION_CONFIG_FILE = "encryption_config.json"
DEFAULT_SALT = b'complex_salt_value_here'
KEY_ITERATIONS = 100000

# Compression settings
COMPRESSION_METHODS = ['zlib', 'gzip', 'lzma']
DEFAULT_COMPRESSION = 'zlib'
DEFAULT_COMPRESSION_LEVEL = 9

# Logging settings
LOG_FILE = "encryption.log"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# File extensions
ENCRYPTED_EXTENSION = '.encrypted'
COMPRESSED_EXTENSIONS = ['.zlib', '.gzip', '.lzma'] 