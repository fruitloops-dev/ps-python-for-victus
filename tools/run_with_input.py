from __future__ import annotations

import argparse
import runpy
import sys
from collections.abc import Sequence
from pathlib import Path


def run_solution(solution: Path, input_file: Path) -> None:
    """Run a solution as __main__ while reading stdin from a UTF-8 file."""
    solution = solution.resolve(strict=True)
    input_file = input_file.resolve(strict=True)

    if solution == Path(__file__).resolve():
        raise ValueError("실행 대상은 run_with_input.py가 아닌 풀이 파일이어야 합니다.")

    original_stdin = sys.stdin
    original_argv = sys.argv
    original_path = sys.path.copy()

    try:
        with input_file.open(encoding="utf-8") as stream:
            sys.stdin = stream
            sys.argv = [str(solution)]
            sys.path.insert(0, str(solution.parent))
            runpy.run_path(str(solution), run_name="__main__")
    finally:
        sys.stdin = original_stdin
        sys.argv = original_argv
        sys.path[:] = original_path


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="입력 파일을 stdin으로 연결해 풀이를 실행합니다.")
    parser.add_argument("solution", type=Path, help="실행할 Python 풀이 파일")
    parser.add_argument("input_file", type=Path, help="stdin으로 사용할 UTF-8 텍스트 파일")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    run_solution(args.solution, args.input_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
