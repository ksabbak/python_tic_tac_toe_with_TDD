def mock_get_game_input_with_one():
    return "1"

def mock_get_game_input(mock_input):
    def getter():
        return mock_input
    return getter
