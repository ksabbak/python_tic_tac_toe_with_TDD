class Colorist:
    @classmethod
    def colors(cls):
        colors = {
                    "BLACK" : "\033[1;30m",
                    "RED" : "\033[1;31m",
                    "GREEN" : "\033[0;32m",
                    "YELLOW" : "\033[1;33m",
                    "BLUE" : "\033[1;34m",
                    "PINK" : "\033[1;35m",
                    "CYAN"  : "\033[1;36m",
                    "WHITE": "\033[1;37m"
                 }
        return colors

    @classmethod
    def color_option_string(cls):
        color_string = "\n"
        for text, color in Colorist.colors().items():
            color_string += Colorist.color_text(text, color) + "\n"
        return color_string

    @classmethod
    def color_text(cls, text, color):
        color = Colorist.assign_color_value(color)
        no_color = "\033[0m"
        return (color + text + no_color)

    @classmethod
    def uncolor_text(cls, text, color):
        color = Colorist.assign_color_value(color)
        no_color = "\033[0m"
        return no_color + text + color

    @classmethod
    def assign_color_value(cls, color):
        if color.upper() in Colorist.colors().keys():
            color = Colorist.colors()[color.upper()]
        elif color == "none":
            color = ""
        return color
