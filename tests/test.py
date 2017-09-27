from bin.hang import check_already_guessed


def test_check_guessed_true():
    assert check_already_guessed('t', 'abcnotrymjkl')
    print('OK!')


def test_checked_guessed_false():
    assert not check_already_guessed('w', 'abcnotrymjkl')
    print('OK!')


if __name__ == '__main__':
    test_check_guessed_true()
    test_checked_guessed_false()
