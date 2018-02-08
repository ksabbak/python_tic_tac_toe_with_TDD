from .command_line_views.view_printer import print_sorry


class Validator:
    @staticmethod
    def handle_input( input_getter, input_parser, arguments=[]):
        user_input = None
        while user_input is None:
            user_input = input_getter(*arguments)
            unacceptable_input = input_parser(user_input)
            if unacceptable_input:
                user_input = None
                print_sorry(unacceptable_input)
            else:
                return user_input
