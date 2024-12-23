import os
import json
import logging
from pathlib import Path
from ..config import settings

def setup_logging():
    """Configure logging settings"""
    logging.basicConfig(
        filename=settings.LOG_FILE,
        level=logging.INFO,
        format=settings.LOG_FORMAT
    )

def load_config():
    """Load encryption configuration"""
    try:
        if os.path.exists(settings.ENCRYPTION_CONFIG_FILE):
            with open(settings.ENCRYPTION_CONFIG_FILE, 'r') as f:
                return json.load(f)
        return {
            'encrypted_files': [],
            'encryption_count': 0,
            'last_encryption': None,
            'compression_stats': {
                'total_compressed': 0,
                'space_saved': 0
            }
        }
    except Exception as e:
        logging.error(f"Config loading error: {str(e)}")
        return None

def save_config(config):
    """Save encryption configuration"""
    try:
        with open(settings.ENCRYPTION_CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        logging.error(f"Config saving error: {str(e)}") 