from enum import Enum

from scripts.tmux import get_option

ARROW_RIGHT = '\ue0b2'
ARROW_LEFT = '\ue0b0'

ROUND_RIGHT = '\ue0b6'
ROUND_LEFT = '\ue0b4'

SLICED_RIGHT = '\ue0ba'
SLICED_LEFT = '\ue0b8'

class Style(Enum):
    NONE = 0
    ARROW = 1
    ROUND = 2
    SLICED = 3

class Separator:
    def __init__(self, style: Style) -> None:
        self.style: Style = style

    def left(self):
        if self.style == Style.ARROW:
            return ARROW_LEFT

        if self.style == Style.ROUND:
            return ROUND_LEFT

        if self.style == Style.SLICED:
            return SLICED_LEFT

        return ""

    def right(self):
        if self.style == Style.ARROW:
            return ARROW_RIGHT

        if self.style == Style.ROUND:
            return ROUND_RIGHT

        if self.style == Style.SLICED:
            return SLICED_RIGHT

        return ""

    def is_set(self):
        return self.style != Style.NONE

def get_separator() -> Separator:
    style_option = get_option("separator_style", "0")
    if not style_option.isdigit():
        return Separator(Style.NONE)
    style_number = int(style_option)
    style = Style(style_number)
    return Separator(style)

