from game_result import *

LEN3 = 3

class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True,3,0)
        strikes, balls = self.get_strikes_and_balls(guess_number)
        return GameResult(False, strikes,balls)

    def get_strikes_and_balls(self, guess_number):
        strikes = balls = 0
        for i, digit in enumerate(guess_number):
            if digit == self._question[i]:
                strikes += 1
            elif digit in self._question:
                balls += 1
        return strikes, balls

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None입니다")

        if len(guess_number) != LEN3:
            raise TypeError("입력은 3자리 문자열이어야 합니다")

        if not guess_number.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guess_number):
        return len(set(guess_number)) != 3