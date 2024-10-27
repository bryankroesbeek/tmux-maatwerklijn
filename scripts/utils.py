from subprocess import Popen, PIPE


def simple_proc(args):
    proc = Popen(args, stdout=PIPE)
    return proc

def simple_read(proc: Popen) -> bytes:
    output, _ = proc.communicate()
    return output


def set_style(bg=None, fg=None, bold=False):
    styles = []

    if bg:
        styles.append(f"bg={bg}")

    if fg:
        styles.append(f"fg={fg}")

    if bold:
        styles.append("bold")

    if (styles.__len__() > 0):
        style = ", ".join(styles)
        return f"#[{style}]"

    return ""

def make_style(content, bg=None, fg=None, bold=False):
    style = set_style(bg=bg, fg=fg, bold=bold)
    return f"{style}{content}"

