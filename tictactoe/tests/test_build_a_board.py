import pytest
from textwrap import dedent

from tictactoe.app.models.board import Board
from tictactoe.app.command_line_views.build_a_board import BuildABoard
from tictactoe.app.command_line_views.aesthetics import Aesthetics


def xtest_printable_board_returns_correct_boards():
    board = Board.create_fresh_board(9)
    aesthetics = Aesthetics(["x", "o"])

    pretty_board = """\
           1   2   3
        A    |   |   \n===+===+===
        B    |   |   \n===+===+===
        C    |   |
        """

    printable_board = (BuildABoard(board, aesthetics, None).printable_board())
    printable_board = printable_board.strip("\033[0m")
    printable_board = printable_board.replace("\x1b[0m", "")
    print ("\n")
    print (repr(printable_board))
    print ("\n")
    print (repr(dedent(pretty_board)))
    print("\n")

    assert printable_board.strip(" ") == dedent(pretty_board).strip(" ")
    # assert BuildABoard(board, aesthetics, None).printable_board() == dedent(pretty_board)
    # pretty_big_board = """\
    #        1   2   3   4
    #     A    |   |   |
    #       ===+===+===+===
    #     B    |   |   |
    #       ===+===+===+===
    #     C    |   |   |
    #       ===+===+===+===
    #     D    |   |   |
    #     """
    # assert str(big_board) == dedent(pretty_big_board)
