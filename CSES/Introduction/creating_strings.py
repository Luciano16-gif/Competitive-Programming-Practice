def main() -> None:
    s = input().strip()
    n = len(s)
    chars = sorted(s)
    used = [False] * n
    ans = []
    path = []
    def dfs():
        if len(path) == n:
            ans.append("".join(path))
            return
        for i in range(n):
            if used[i]:
                continue
            elif i > 0 and chars[i] == chars[i-1] and not used[i-1]: 
                continue
            
            path.append(chars[i])
            used[i] = True

            dfs()

            path.pop()
            used[i] = False
    
    dfs()

    print(len(ans))
    for x in ans:
        print(x)


    


if __name__ == "__main__":
    main()