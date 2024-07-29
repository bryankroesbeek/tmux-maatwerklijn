from scripts.utils import simple_proc


def set_global(option, value):
    simple_proc(["tmux", "set-option", "-g", option, value])


def set_window_global(option, value):
    simple_proc(["tmux", "set-option", "-w", "-g", option, value])
