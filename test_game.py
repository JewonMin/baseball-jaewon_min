import pytest
from game import *
from game_result import *

@pytest.fixture
def game():
    return Game()

def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

@pytest.mark.parametrize("invalid_input", [None,"12","1234","12s","121"])
def test_exception_when_invalid_input(game, invalid_input):
    assert_illegal_argument(game, invalid_input)

def test_return_solved_result_if_matched_number(game):
    game.question = "123"
    result: GameResult = game.guess("123")

    assert result is not None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0
