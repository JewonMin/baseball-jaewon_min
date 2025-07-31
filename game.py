class Game:
    def guess(self, guess_number):
        self._assert_illegal_value(guess_number)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError()
        if len(guess_number) != 3:
            raise TypeError()
        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self._is_duplicated_number(guess_number):
            raise TypeError()

    def _is_duplicated_number(self, guess_number):
        return guess_number[0] == guess_number[1] or \
            guess_number[0] == guess_number[2] or \
            guess_number[1] == guess_number[2]