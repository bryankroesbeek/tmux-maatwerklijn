
from typing import Literal
from scripts.utils import make_style
from options.separator import Separator


class Pane:
    def __init__(self, title: str, content: str, foreground: str, background: str) -> None:
        self.title = title
        self.content = content
        self.foreground = foreground
        self.background = background

    def print(self, pad: bool = False):
        content = f" {self.content} " if pad else self.content
        return make_style(content, bg=self.background, fg=self.foreground, bold=True)


class Panes:
    def __init__(self, *panes: Pane, foreground: str, background: str) -> None:
        self.panes = list(panes) if len(panes) > 0 else list()
        self.foreground = foreground
        self.background = background

    def add(self, pane: Pane):
        self.panes.append(pane)

    def print(self, position: Literal["left", "right"], separator: Separator):
        default_style = make_style("", bg=self.background, fg=self.foreground)
        sep = separator.get(position, default=" ")

        styles: list[str] = []
        for pane in self.panes:
            if not separator.is_set():
                styles.append(pane.print(pad=True))
                continue

            style: list[str] = []
            if position == "right":
                style.append(make_style(sep, fg=pane.background, bg=self.background))
            if position == "left":
                style.append(make_style(sep, fg=self.background, bg=pane.background))

            style.append(pane.print(pad=True))

            if position == "left":
                style.append(make_style(sep, fg=pane.background, bg=self.background))
            if position == "right":
                style.append(make_style(sep, fg=self.background, bg=pane.background))

            styles.append("".join(style))

        spacing = "" if separator.is_set() else " "
        return f"{default_style}{spacing}".join(styles)


# def pane_status(col1, col2, bold=False):
#     sections = []
#     if not separator.is_set():
#         sections.append(make_style(" ", bg=background, bold=bool(bold)))
#     else:
#         sections.append(make_style(left, bg=col1, fg=background, bold=bool(bold)))
#     sections.append(make_style(" #I | ", bg=col1, fg=col2, bold=bool(bold)))
#     sections.append(make_style("#W ", fg=col2, bold=bool(bold)))
#     sections.append(make_style(left, bg=background, fg=col1, bold=bool(bold)))
#
#     return "".join(sections)
#
