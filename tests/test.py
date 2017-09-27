from hang import check_already_guessed


def test_check_guessed_true():
    already = ['abcnotrymjkl']
    letter = 't'
    assert check_already_guessed(letter, already) == True


def test_checked_guessed_false():
    already = ['abcnotrymjkl']
    letter = 'w'
    assert check_already_guessed(letter, already) == False

