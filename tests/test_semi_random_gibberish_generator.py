import random
import re
import pytest
from modules.semi_random_gibberish_generator import SemiRandomGibberishGenerator

def set_seed(seed=42):
    random.seed(seed)

def test_semi_random_instantiation():
    """Test that the semi-random generator can be instantiated with valid parameters."""
    generator = SemiRandomGibberishGenerator(min_chunk_size=3, max_chunk_size=5)
    assert generator.min_chunk_size == 3
    assert generator.max_chunk_size == 5

def test_semi_random_output_structure():
    """Test that the output string has the correct structure."""
    set_seed()  # Ensure reproducibility
    generator = SemiRandomGibberishGenerator(min_chunk_size=3, max_chunk_size=3)
    input_text = "I was not here, and I am not happy about it"
    output = generator.generate(input_text, randomness=1.0)
    # Check that output is a string and is not empty.
    assert isinstance(output, str)
    assert len(output) > 0
    # Ensure the output starts with a capital letter and ends with proper punctuation.
    assert output[0].isupper()
    assert output[-1] in ".!?"

def test_semi_random_linking_behavior():
    """
    Test that the algorithm links chunks properly.
    Given a text with overlapping words, verify that the linking does not
    duplicate the linking word.
    """
    set_seed()  # Fix the randomness for predictable behavior.
    generator = SemiRandomGibberishGenerator(min_chunk_size=3, max_chunk_size=3)
    input_text = "I was not here, and I am not happy about it"
    output = generator.generate(input_text, randomness=1.0)
    
    # Split the output into words.
    words = output[:-1].split()  # remove final punctuation for this test
    # Check that no two adjacent words are identical (which would indicate a failed linking)
    for i in range(1, len(words)):
        assert words[i-1].lower() != words[i].lower(), "Linking error: duplicate adjacent linking word found."
    
def test_semi_random_output_subset_of_input():
    """
    Ensure that the generated gibberish only contains words from the original input.
    This is a rough check since punctuation may be present.
    """
    set_seed()  # Fix the randomness.
    generator = SemiRandomGibberishGenerator(min_chunk_size=3, max_chunk_size=3)
    input_text = "I was not here, and I am not happy about it"
    output = generator.generate(input_text, randomness=1.0)
    
    # Remove punctuation and lowercase the words.
    clean_input = set(re.sub(r'[^ \w\s]', '', input_text).lower().split())
    clean_output = set(re.sub(r'[^ \w\s]', '', output).lower().split())
    
    # All words in the output should be part of the input.
    assert clean_output.issubset(clean_input), "Output contains words not present in input."
