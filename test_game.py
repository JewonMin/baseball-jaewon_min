import pytest
from game import *

def test_exception_when_input_is_none():
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)