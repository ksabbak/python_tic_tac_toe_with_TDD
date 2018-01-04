import pytest

from ..app.__init__ import AI, Player, Board

@pytest.fixture()
def ai():
    return AI("x")
@pytest.fixture()
def board():
    return Board.create_from_scratch()

def tests_ai_is_a_player():
    assert issubclass(AI, Player)

def test_player_is_ai(ai):
    assert ai.is_ai() is True

def test_ai_player_has_move_log(ai):
    assert ai.moves == []

def test_ai_player_logs_moves(ai, board):
    move = ai.make_move(board, None)
    move_2 = ai.make_move(board, None)
    assert ai.moves == [move, move_2]

def test_ai_can_determine_opponent_marker(ai, board):
    board.mark_space(0, "o")
    assert ai._deduce_opponent_marker(board) == "o"

def tests_ai_can_move_without_input(ai, board):
    assert ai._get_move(board) in range(0, 9)

def tests_ai_moves_to_empty_spot(ai, board):
    for i in range(1, 9):
        board.mark_space(i, ai.marker)
    assert ai._get_move(board) == 0

def test_ai_can_make_winning_move(ai, board):
    board.mark_space(0, ai.marker)
    board.mark_space(1, ai.marker)
    assert ai._get_move(board) == 2

def test_ai_can_stop_immediate_horizontal_loss0(ai, board):
    board.mark_space(3, "o")
    board.mark_space(0, ai.marker)
    board.mark_space(4, "o")
    assert ai._get_move(board) == 5

def test_ai_can_stop_immediate_horizontal_loss2(ai, board):
    board.mark_space(3, "o")
    board.mark_space(2, ai.marker)
    board.mark_space(4, "o")
    assert ai._get_move(board) == 5

def test_ai_can_stop_immediate_horizontal_loss6(ai, board):
    board.mark_space(3, "o")
    board.mark_space(6, ai.marker)
    board.mark_space(4, "o")
    assert ai._get_move(board) == 5

def test_ai_can_stop_immediate_horizontal_loss8(ai, board):
    board.mark_space(3, "o")
    board.mark_space(8, ai.marker)
    board.mark_space(4, "o")
    assert ai._get_move(board) == 5

def test_ai_1st_move_when_1st_is_center(ai, board):
    assert ai._get_move(board) == 4

def test_ai_1st_move_when_2nd_is_middle_space_if_open(ai, board):
    board.mark_space(3, "o")
    assert ai._get_move(board) == 4

def test_ai_1st_move_when_2nd_is_corner_space_if_middle_taken(ai, board):
    board.mark_space(4, "o")
    assert ai._get_move(board) in [0, 2, 6, 8]

def test_ai_prevents_opponent_from_fork_win(ai, board):
    board.mark_space(0, "o")
    board.mark_space(4, ai.marker)
    board.mark_space(8, "o")
    assert ai._get_move(board) in [1, 3, 5, 7]

def test_ai_prevents_opponent_from_fork_win_side_middle(ai, board):
    board.mark_space(0, "o")
    board.mark_space(4, ai.marker)
    board.mark_space(7, "o")
    assert ai._get_move(board) not in [2, 1]

def test_ai_ends_game_when_possible(ai, board):
    board.mark_space(0, "o")
    board.mark_space(1, "o")
    board.mark_space(7, ai.marker)
    board.mark_space(8, ai.marker)
    assert ai._get_move(board) == 6

def test_ai_prevents_opponent_from_fork_win_middle_two_corners(ai, board):
    board.mark_space(4, "o")
    board.mark_space(8, ai.marker)
    board.mark_space(0, "o")
    assert ai._get_move(board) in [2, 6]


@pytest.fixture()
def big_board():
    return Board.create_from_scratch(16)

def test_ai_can_make_winning_move_16_space_board(ai, big_board):
    big_board.mark_space(0, ai.marker)
    big_board.mark_space(1, ai.marker)
    big_board.mark_space(3, ai.marker)
    assert ai._get_move(big_board) == 2

def test_ai_can_stop_immediate_horizontal_loss_16_space_board(ai, big_board):
    big_board.mark_space(4, "o")
    big_board.mark_space(5, "o")
    big_board.mark_space(6, "o")
    assert ai._get_move(big_board) == 7

def test_ai_ends_game_when_possible_16_space_board(ai, big_board):
    big_board.mark_space(0, "o")
    big_board.mark_space(1, "o")
    big_board.mark_space(2, "o")
    big_board.mark_space(12, ai.marker)
    big_board.mark_space(13, ai.marker)
    big_board.mark_space(14, ai.marker)
    assert ai._get_move(big_board) == 15

def test_ai_prevents_fork_16_space_board(ai, big_board):
    big_board.mark_space(3, "o")
    big_board.mark_space(5, "o")
    big_board.mark_space(6, "o")
    big_board.mark_space(11, "o")
    big_board.mark_space(13, ai.marker)
    big_board.mark_space(14, ai.marker)
    assert ai._get_move(big_board) == 7
