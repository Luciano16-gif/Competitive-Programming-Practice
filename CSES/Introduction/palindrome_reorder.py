def main() -> None:
    from collections import Counter
    string: str = input()
    n: int = len(string)
    if n < 1:
        print("NO SOLUTION")
        return
    
    half: list[str] = []
    no_repeats: int = 0
    middle: str = ""

    cnt = Counter(string)
    
    for ch, times in cnt.items(): 
        if times % 2 != 0:
            no_repeats += 1
            middle = ch
        half.extend(ch * (times // 2))

    if no_repeats > 1 or (no_repeats == 1 and n % 2 == 0):
        print("NO SOLUTION")
        return
        

    print("".join(half) + middle + "".join(reversed(half)))



if __name__ == "__main__":
    main()