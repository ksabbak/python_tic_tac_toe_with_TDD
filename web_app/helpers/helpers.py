def end_conditions(board, player_marker):
    if board.winning_marker() == player_marker:
        return game_over(board=board, result="You won! 😃")
    elif board.winning_marker() is not None:
        return game_over(board=board, result="You lost 😱")
    elif board.is_full():
        return game_over(board=board, result="Game over, no one wins. 🙃")
