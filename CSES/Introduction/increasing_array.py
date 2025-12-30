def main() -> None:
    n: int = int(input())
    nums: list[int] = list(map(int, input().split()))
    moves: int = 0

    previous_num: int = nums[0]
    for i in range(1, n):
        if previous_num > nums[i]:
            moves += previous_num - nums[i] 
            nums[i] = previous_num
        previous_num = nums[i]

    print(moves)

if __name__ == "__main__":
    main()
