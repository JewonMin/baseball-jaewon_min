import pytest
from game import *

@pytest.fixture
def game():
    return Game()

def test_exception_when_input_is_none(game):
    with pytest.raises(TypeError):
        game.guess(None)

def test_exception_when_input_length_is_unmatched(game):
    guessNumber = "12"
    assert_illegal_argument(game, guessNumber)


def assert_illegal_argument(game, guessNumber):
    try:
        game.guess(guessNumber)
        pytest.fail()
    except TypeError:
        pass