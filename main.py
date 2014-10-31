from random import shuffle

def main():
    # Setting up deck
    deck = draw_card()
    
    # Setting up score board
    num_of_players = int(input("How many players: "))
    player_total = [0] * num_of_players
    
    # Draw first two cards
    for player in range(num_of_players):
        for i in range(2):
            player_total[player] += next(deck)
    
    #Game loop
    while(1):
        player_out = 0
        for player in range(num_of_players):
            # Has the player lost?
            if player_total[player] >= 21:
                player_out += 1
                continue
            
            # Show score and ask for move
            print("\nPlayer {0}: {1}".format(player + 1, player_total[player]))
            while(1):
                move = input("Hit or stay: ").lower()
                
                # If hit draw another card and go back to game loop
                if move == "hit":
                    player_total[player] += next(deck)
                    print("Player {0}: {1}".format(player + 1,
                                                   player_total[player]))
                    break
                # If break make score huge so it's ignored in loop
                elif move == "stay":
                    player_total[player] += 1000
                    break
        if player_out == num_of_players:
            break
    
    # End game score tally
    top_score = 0
    winners = []
    
    # Find the top score
    for player in range(num_of_players):
        if player_total[player] >= 1000:
            player_total[player] -= 1000
        if top_score < player_total[player] < 22:
            top_score = player_total[player]
    
    # Find those who have the top score
    for player in range(num_of_players):
        if player_total[player] == top_score:
            winners.append(player)
    
    # Print the winner
    for winner in winners:
        print("Player {0} wins with: {1}".format(winner + 1, top_score))
    

def draw_card():
    deck = []
    deck += [i for i in range(1, 10)] * 4
    deck += [10] * 16
    shuffle(deck)
    
    for i in range(56):
        yield deck[0]
        del deck[0]

if __name__ == '__main__':
    main()