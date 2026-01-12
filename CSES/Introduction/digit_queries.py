import sys

def main() -> None:
    input = sys.stdin.readline

    query_count: int = int(input())
    positions: list[int] = [int(input()) for _ in range(query_count)]

    for position in positions:
        if position < 10:
            print(position)
            continue

        digits_before_block: int = 0
        digit_length: int = 0
        first_number_in_block: int = 0

        for d in range(1, 19):
            numbers_in_block = 9 * (10 ** (d - 1))
            digits_in_block = numbers_in_block * d
            digits_up_to_block = digits_before_block + digits_in_block

            if digits_before_block < position <= digits_up_to_block:
                digit_length = d
                first_number_in_block = 10 ** (d - 1)
                break

            digits_before_block = digits_up_to_block

        position_in_block = position - digits_before_block
        index_in_block = (position_in_block - 1) // digit_length
        digit_index = (position_in_block - 1) % digit_length

        target_number = first_number_in_block + index_in_block
        print(str(target_number)[digit_index])

if __name__ == "__main__":
    main()
