import pytest
from game import *

@pytest.fixture
def game():
    return Game()

def test_exception_when_input_is_none(game):
    with pytest.raises(TypeError):
        game.guess(None)

def test_exception_when_input_length_is_unmatched(game):
    try:
        game.guess("12")
    except TypeError:
        pass