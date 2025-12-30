def main() -> None:
    sequence: str =  input()
    if not sequence:
        print(0)
        return
    
    char: str = sequence[0]
    result = n = 1
   
    for x in sequence[1:]:
        if x == char:
            n += 1
        else:
            n = 1
        
        if result < n:
            result = n
        
        char = x
    
    print(result)
            
if __name__ == "__main__":
    main()