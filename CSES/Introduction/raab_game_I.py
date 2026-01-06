def main() -> None:
    t: int = int(input())
    games: list[list[int]] = []
    for i in range(t):
        games.append(list(map(int, input().split())))

    player1_cards: list[int] = []
    player2_cards: list[int] = []

    for i in range(t):
        n = games[i][0]
        p1_points = games[i][1]
        p2_points = games[i][2]
        if (p1_points + p2_points) > n or ((p1_points == 0) != (p2_points == 0)):
            print("NO")
            continue
        scoring_rounds = p1_points + p2_points
        tie_rounds = n - scoring_rounds
        remaining_cards = list(range(tie_rounds + 1, n + 1))

        ties = list(range(1, tie_rounds + 1))


        player1_cards = ties + remaining_cards
        player2_cards = ties + remaining_cards[p1_points:] + remaining_cards[:p1_points]


        

        print("YES")
        print(*player1_cards)
        print(*player2_cards)
        player1_cards = []
        player2_cards = []
    
if __name__ == "__main__":
    main()