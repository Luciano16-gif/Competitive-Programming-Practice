def main() -> None:
    n: int = int(input())
    nums: list[int] = []

    if n == 1:
        print(n)
        return
    
    if n == 2 or n == 3:
        print('NO SOLUTION')
        return

    for i in range(2, n + 1, 2):
        nums.append(i)
    
    for i in range(1, n + 1, 2):
        nums.append(i)
        
    print(*nums)
            

if __name__ == "__main__":
    main()