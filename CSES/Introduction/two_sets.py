def main() -> None:
    n = int(input())
    s = ((n*(n+1)) // 2)
    num_to_count: int = (s // 2)

    if s % 2 != 0:
        print('NO')
        return

    nums1: list[int] = []
    nums2: list[int] = []
    nums1_sum: int = 0

    for i in range(n, 0, -1):
        if (num_to_count - nums1_sum) - i >= 0:
            nums1.append(i)
            nums1_sum += i
        else:
            nums2.append(i)

    print('YES')

    print(len(nums1))
    print(*nums1)

    print(len(nums2))
    print(*nums2)
    

if __name__ == "__main__":
    main()