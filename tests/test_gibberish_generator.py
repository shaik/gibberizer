"""
Tests for the gibberish generator module.
"""
import pytest
from modules.gibberish_generator import create_generator


def test_generator_creation():
    """Test that generator can be created with default parameters."""
    generator = create_generator()
    assert generator is not None


def test_gibberish_generation():
    """Test basic gibberish generation functionality."""
    generator = create_generator()
    input_text = "This is a test sentence for gibberish generation."
    result = generator.generate(input_text, randomness=1.0)
    
    # Basic validation
    assert isinstance(result, str)
    assert len(result) > 0
    assert result[0].isupper()  # Should start with capital letter
    assert result[-1] in ".!?"  # Should end with punctuation


def test_randomness_parameter():
    """Test that randomness parameter affects output."""
    generator = create_generator()
    input_text = "This is a test sentence that should remain unchanged."
    
    # With randomness=0, output should match input (except for punctuation)
    result = generator.generate(input_text, randomness=0.0)
    assert result.rstrip(".!?").lower() == input_text.rstrip(".!?").lower()
    