from pathlib import Path

import pytest

from tools.run_with_input import run_solution


def test_run_solution_redirects_stdin(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    solution = tmp_path / "solution.py"
    input_file = tmp_path / "input.txt"
    solution.write_text(
        "a, b = map(int, input().split())\nprint(a + b)\n",
        encoding="utf-8",
    )
    input_file.write_text("20 22\n", encoding="utf-8")

    run_solution(solution, input_file)

    assert capsys.readouterr().out == "42\n"
