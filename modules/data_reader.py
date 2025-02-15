"""
Data reader module for handling text input from various sources.
Currently supports local file reading, designed for easy extension to other sources.
"""
import os
from pathlib import Path
from typing import List, Optional


class DataReader:
    """Base class for data readers defining the interface."""
    
    def list_sources(self) -> List[str]:
        """List available data sources."""
        raise NotImplementedError
    
    def read_text(self, source: str) -> str:
        """Read text from the specified source."""
        raise NotImplementedError


class LocalFileReader(DataReader):
    """Implementation of DataReader for local files."""
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True)
    
    def list_sources(self) -> List[str]:
        """List available text files in the data directory."""
        return [
            f.name for f in self.data_dir.glob("*.txt")
            if f.is_file()
        ]
    
    def read_text(self, source: str) -> str:
        """Read text from a specific file in the data directory."""
        file_path = self.data_dir / source
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {source}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()


# Factory function to get appropriate reader based on source type
def get_reader(source_type: str = "local", **kwargs) -> DataReader:
    """
    Factory function to create appropriate data reader.
    
    Args:
        source_type: Type of data source ("local" for now, extensible for future)
        **kwargs: Additional arguments for specific reader types
    
    Returns:
        DataReader: Instance of appropriate reader class
    """
    if source_type == "local":
        data_dir = kwargs.get("data_dir", "data")
        return LocalFileReader(data_dir)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")
