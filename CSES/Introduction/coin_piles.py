def main() -> None:
    t: int = int(input())
    answers: list[str] = []

    for i in range(1, t + 1):
        x, y = map(int, input().split())
        if ((x + y) % 3) == 0 and max(x, y) <= 2*min(x, y):
            answers.append("YES")
        else:
            answers.append("NO")

    print("\n".join(answers))




if __name__ == "__main__":
    main()