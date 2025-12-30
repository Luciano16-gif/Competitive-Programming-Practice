def main() -> None: 
    def calculate_positions(m: int) -> int:
        return m*(m-1) // 2

    def calculate_attacks(k:int) -> int:
        if k < 3:
            return 0
        else:
            return 4*((k-1)*(k-2)) 

    n = int(input())

    possible_positions: int = 0
    possible_attacks: int = 0

    for i in range(1, n + 1):
        possible_positions = calculate_positions(i*i)
        possible_attacks = calculate_attacks(i)

        print(possible_positions - possible_attacks)

    



if __name__ == "__main__":
    main()