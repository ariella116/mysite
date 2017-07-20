import game

def test_resetgame():
    the_word = "ariella"
    state = game.reset_state(the_word)
    assert the_word == state['word']
    # there are 7 letters in ariella sp guessed should be a list of 7 underscores
    assert state['guessed'] == ['_', '_', '_', '_', '_', '_', '_' ]

def test_get_word():
    # get a value from the function choose_word in game
    # assert that it is equal to "jerusalem"
    possible_words = ['jerusalem', 'dumpster', 'bus', 'chocolate',
                      'morning', 'live', 'cats']
    chosen_word = game.choose_word()
    assert chosen_word in possible_words
