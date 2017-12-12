from ..app.__init__ import Game

# GENERAL
def test_there_is_a_game():
    assert Game() is not None

# BOARD
def test_game_has_board():
    assert Game().board is not None

def test_game_is_marked_over_when_board_is_filled():
    game = Game()
    i = 0
    while i < len(game.board.spaces):
        game.board.mark_space(i, "X")
        i += 1
    assert game.is_over

#PLAYERS
def test_game_has_two_players():
    assert len(Game().players) == 2

def test_player_one_has_marker_x():
    assert Game().players[0].marker == "x"

def test_player_two_has_marker_o():
    assert Game().players[1].marker == "o"
