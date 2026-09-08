def Multiply(x: int, y: int) -> int:
    # 이 구현은 음이 아닌 정수를 가정
    if x < 0 or y < 0:
        raise ValueError("x와 y는 음이 아닌 정수여야 합니다.")

    if x == 0 or y == 0:
        return 0

    n = max(len(str(x)), len(str(y)))

    if n == 1:
        return x * y

    # ceil(n / 2)를 정수 연산으로 계산
    m = (n + 1) // 2
    base = 10**m

    # x = a * base + b
    # y = c * base + d
    a, b = divmod(x, base)
    c, d = divmod(y, base)

    ac = Multiply(a, c)
    bd = Multiply(b, d)
    z = Multiply(a + b, c + d)

    # 핵심: 10^n이 아니라 10^(2m)
    xy = ac * (base**2) + (z - ac - bd) * base + bd

    return xy


def main() -> None:
    x = int(input())
    y = int(input())
    print(Multiply(x, y))


if __name__ == "__main__":
    main()
