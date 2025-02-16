import random
import re
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class SemiRandomGibberishGenerator:
    def __init__(self, min_chunk_size=3, max_chunk_size=3):
        """
        Initialize the semi-random gibberish generator.
        
        Args:
            min_chunk_size (int): Minimum number of words per chunk.
            max_chunk_size (int): Maximum number of words per chunk.
        """
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size

    def _clean_word(self, word):
        """
        Clean a word by removing non-letter characters and converting to lowercase.
        This version supports Hebrew and other languages by using the Unicode property
        of letters.
        
        Args:
            word (str): The word to clean.
        
        Returns:
            str: Cleaned word.
        """
        return ''.join(ch for ch in word if ch.isalpha()).lower()

    def _split_into_chunks(self, text):
        """
        Split the input text into chunks of random lengths between min and max chunk sizes.
        
        Args:
            text (str): The input text.
            
        Returns:
            List[str]: A list of text chunks.
        """
        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunk_size = random.randint(self.min_chunk_size, self.max_chunk_size)
            chunk = words[i:i+chunk_size]
            if chunk:
                chunks.append(" ".join(chunk))
            i += chunk_size
        return chunks

    def _build_mappings(self, chunks):
        """
        Build two mappings:
          - first_word_map: maps cleaned first word to a list of chunks starting with that word.
          - last_word_map: maps cleaned last word to a list of chunks ending with that word.
        
        Args:
            chunks (List[str]): List of text chunks.
        
        Returns:
            Tuple[Dict[str, List[str]], Dict[str, List[str]]]: first_word_map, last_word_map.
        """
        first_word_map = {}
        last_word_map = {}
        for chunk in chunks:
            words = chunk.split()
            if not words:
                continue
            first_word = self._clean_word(words[0])
            last_word = self._clean_word(words[-1])
            first_word_map.setdefault(first_word, []).append(chunk)
            last_word_map.setdefault(last_word, []).append(chunk)
        return first_word_map, last_word_map

    def _ensure_sentence_structure(self, text):
        """
        Ensure the generated text has proper sentence structure.
        
        Args:
            text (str): The generated text.
        
        Returns:
            str: Text with proper sentence structure.
        """
        assembled = text.strip()
        if assembled:
            assembled = assembled[0].upper() + assembled[1:]
            if assembled[-1] not in ".!?":
                assembled += "."
        return assembled

    def generate(self, text, randomness=0.7):
        logging.debug(f"Generating gibberish with randomness: {randomness}")
        chunks = self._split_into_chunks(text)
        if not chunks:
            return ""
        
        if randomness == 0.0:
            return self._ensure_sentence_structure(text)
        
        # Build the word mappings.
        first_word_map, last_word_map = self._build_mappings(chunks)
        
        # Start with a random chunk.
        current_chunk = random.choice(chunks)
        result_chunks = [current_chunk]
        logging.debug(f"First chunk: {current_chunk}")

        while True:
            current_words = current_chunk.split()
            if not current_words:
                break
            link_word = self._clean_word(current_words[-1])
            logging.debug(f"Current words: |{current_words}|")
            logging.debug(f"Link word: |{link_word}|")

            # Find candidate chunks that start with link_word.
            candidates = first_word_map.get(link_word, [])
            # logging.debug(f"Candidates: {candidates}")
            if not candidates:
                break  # No candidates, so stop linking.
            
            # Select one candidate randomly.
            candidate = random.choice(candidates)
            candidate_words = candidate.split()
            
            # If the first word of the candidate matches link_word, remove it.
            if candidate_words and self._clean_word(candidate_words[0]) == link_word:
                candidate = " ".join(candidate_words[1:])
            
            # Append the candidate and update current_chunk.
            result_chunks.append(candidate)
            current_chunk = candidate
        
        # Join all chunks and enforce proper sentence structure.
        assembled = " ".join(result_chunks)
        return self._ensure_sentence_structure(assembled)
