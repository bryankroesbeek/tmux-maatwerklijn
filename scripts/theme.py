
from scripts.tmux import get_option


def get_color(default="#ffffff"):
    theme = get_option("color", default)
    return theme


def get_background(default="#333333"):
    theme = get_option("background", default)
    return theme


def get_background_inactive(default="#555555"):
    theme = get_option("background_inactive", default)
    return theme
