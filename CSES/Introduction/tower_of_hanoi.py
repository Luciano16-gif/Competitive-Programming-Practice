def main() -> None:
    n: int = int(input())
    min_moves: int = 2**n - 1
    print(min_moves)
    def solve(num_of_disks, src, aux, dest): #this is just a simulation not the real code
        if num_of_disks == 1:
            print(src, dest)
            return
        solve(num_of_disks - 1, src, dest, aux)
        print(src, dest)
        solve(num_of_disks - 1, aux, src, dest)
    
    solve(n, 1, 2, 3)


if __name__ == "__main__":
    main()