import zlib
import gzip
import lzma
import logging
from pathlib import Path

class FileCompressor:
    def __init__(self):
        self.compression_methods = {
            'zlib': self._zlib_compress,
            'gzip': self._gzip_compress,
            'lzma': self._lzma_compress
        }
        
    def compress_file(self, file_path, method='zlib', level=9):
        """Compress file using specified method"""
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            compressed_data = self.compression_methods[method](data, level)
            
            # Save compressed file
            compressed_path = f"{file_path}.{method}"
            with open(compressed_path, 'wb') as f:
                f.write(compressed_data)
                
            return compressed_path
            
        except Exception as e:
            logging.error(f"Compression error: {str(e)}")
            raise
            
    def decompress_file(self, file_path):
        """Decompress file based on extension"""
        try:
            method = file_path.split('.')[-1]
            with open(file_path, 'rb') as f:
                compressed_data = f.read()
                
            if method == 'zlib':
                data = zlib.decompress(compressed_data)
            elif method == 'gzip':
                data = gzip.decompress(compressed_data)
            elif method == 'lzma':
                data = lzma.decompress(compressed_data)
                
            output_path = str(file_path).replace(f'.{method}', '')
            with open(output_path, 'wb') as f:
                f.write(data)
                
            return output_path
            
        except Exception as e:
            logging.error(f"Decompression error: {str(e)}")
            raise
            
    def _zlib_compress(self, data, level):
        return zlib.compress(data, level)
        
    def _gzip_compress(self, data, level):
        return gzip.compress(data, level)
        
    def _lzma_compress(self, data, level):
        return lzma.compress(data) 