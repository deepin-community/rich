import subprocess
from typing import List, Tuple
import sys

from rich.progress import Progress

from wcwidth import wcwidth


progress = Progress()


def make_widths_table() -> List[Tuple[int, int, int]]:
    table: List[Tuple[int, int, int]] = []
    append = table.append

    make_table_task = progress.add_task("Calculating table...")

    widths = (
        (codepoint, wcwidth(chr(codepoint)))
        for codepoint in range(0, sys.maxunicode + 1)
    )

    _widths = [(codepoint, width) for codepoint, width in widths if width != 1]
    iter_widths = iter(_widths)

    endpoint, group_cell_size = next(iter_widths)
    start_codepoint = end_codepoint = endpoint
    for codepoint, cell_size in progress.track(
        iter_widths, task_id=make_table_task, total=len(_widths) - 1
    ):
        if cell_size != group_cell_size or codepoint != end_codepoint + 1:
            append((start_codepoint, end_codepoint, group_cell_size))
            start_codepoint = end_codepoint = codepoint
            group_cell_size = cell_size
        else:
            end_codepoint = codepoint
    append((start_codepoint, end_codepoint, group_cell_size))
    return table


def get_cell_size(table: List[Tuple[int, int, int]], character: str) -> int:
    codepoint = ord(character)
    lower_bound = 0
    upper_bound = len(table) - 1
    index = (lower_bound + upper_bound) // 2
    while True:
        start, end, width = table[index]
        if codepoint < start:
            upper_bound = index - 1
        elif codepoint > end:
            lower_bound = index + 1
        else:
            return width
        if upper_bound < lower_bound:
            break
        index = (lower_bound + upper_bound) // 2
    return 1


def test(widths_table):
    for codepoint in progress.track(
        range(0, sys.maxunicode + 1), description="Testing..."
    ):
        character = chr(codepoint)
        width1 = get_cell_size(widths_table, character)
        width2 = wcwidth(character)
        if width1 != width2:
            print(f"{width1} != {width2}")
            break


def run():
    with progress:
        widths_table = make_widths_table()
        test(widths_table)
    table_file = f"""# Auto generated by make_terminal_widths.py

CELL_WIDTHS = {widths_table!r}

"""
    with open("../rich/_cell_widths.py", "wt") as fh:
        fh.write(table_file)

    subprocess.run("black ../rich/_cell_widths.py", shell=True)


if __name__ == "__main__":
    run()
