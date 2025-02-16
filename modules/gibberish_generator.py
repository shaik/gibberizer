"""
Gibberish generator module for processing input text into gibberish output.
"""
import random
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.DEBUG)


class GibberishGenerator:
    def __init__(self, min_chunk_size: int = 3, max_chunk_size: int = 3):
        """
        Initialize the gibberish generator.
        
        Args:
            min_chunk_size: Minimum size of text chunks to use
            max_chunk_size: Maximum size of text chunks to use
        """
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
    
    def _split_into_chunks(self, text: str) -> List[str]:
        """Split input text into word chunks of varying sizes."""
        words = text.split()
        chunks = []
        i = 0
        
        while i < len(words):
            # Randomly choose chunk size
            chunk_size = random.randint(self.min_chunk_size, self.max_chunk_size)
            chunk = words[i:i + chunk_size]
            if chunk:  # Only add non-empty chunks
                chunks.append(" ".join(chunk))
            i += chunk_size
        
        return chunks
    
    def _ensure_sentence_structure(self, text: str) -> str:
        """Ensure basic sentence structure (capitalization, punctuation)."""
        # Capitalize first letter
        text = text[0].upper() + text[1:] if text else ""
        
        # Add period if no punctuation at end
        if text and text[-1] not in ".!?":
            text += "."
        
        return text
    
    def generate(self, text: str, randomness: float = 0.7) -> str:
        """
        Generate gibberish text from input text.
        
        Args:
            text: Input text to process
            randomness: Float between 0 and 1 controlling how much to shuffle
                       (0 = original order, 1 = completely random)
        
        Returns:
            str: Generated gibberish text
        """
        # Split into chunks
        chunks = self._split_into_chunks(text)
        
        # If randomness is 0.0, return the original text
        if randomness == 0.0:
            return self._ensure_sentence_structure(text)
        
        # Randomly reorder some chunks based on randomness parameter
        num_to_shuffle = int(len(chunks) * randomness)
        if num_to_shuffle > 0:
            shuffle_indices = random.sample(range(len(chunks)), num_to_shuffle)
            shuffled_chunks = [chunks[i] for i in shuffle_indices]
            random.shuffle(shuffled_chunks)
            
            for idx, new_chunk in zip(shuffle_indices, shuffled_chunks):
                chunks[idx] = new_chunk
        
        # Join chunks and ensure proper sentence structure
        result = " ".join(chunks)
        return self._ensure_sentence_structure(result)


def create_generator(algorithm="random", **kwargs):
    logging.debug(f"Creating generator with algorithm: {algorithm}")
    if algorithm == "semi_random":
        from modules.semi_random_gibberish_generator import SemiRandomGibberishGenerator
        logging.debug("Created SemiRandomGibberishGenerator.")
        return SemiRandomGibberishGenerator(**kwargs)
    else:
        logging.debug("Created GibberishGenerator.")
        return GibberishGenerator(**kwargs)
