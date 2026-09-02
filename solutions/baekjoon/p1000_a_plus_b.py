import sys


def solve() -> None:
    a, b = map(int, sys.stdin.buffer.readline().split())
    print(a + b)


if __name__ == "__main__":
    solve()
