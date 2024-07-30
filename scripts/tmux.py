from scripts.utils import simple_proc, simple_read


def set_global(option, value):
    simple_proc(["tmux", "set-option", "-g", option, value])


def set_window_global(option, value):
    simple_proc(["tmux", "set-option", "-w", "-g", option, value])


def get_option(option: str, default="") -> str:
    proc = simple_proc(["tmux", "show-option", "-gqv", f"@maatwerklijn_{option}"])
    text = simple_read(proc).decode("utf-8")
    if not bool(text):
        return default
    if text == "default":
        return default

    return text


def get_theme(default="#ffffff"):
    theme = get_option("theme", default)
    return theme
