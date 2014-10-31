from random import shuffle

def main():
    # Setting up deck
    deck = draw_card()
    
    # Setting up score board
    players = [0] * int(input("How many players: "))
    
    # Draw first two cards
    players = draw_two_cards(players, deck)
    
    #Game loop
    while(1):
        player_out = 0
        for i in range(len(players)):
            # Has the player lost?
            if players[i] >= 21:
                player_out += 1
                continue
            
            # Show score and ask for move
            print_player_score(i, players[i])
            while(1):
                move = input("Hit or stay: ").lower()
                # If hit draw another card and go back to game loop
                if move == "hit":
                    players[i] += next(deck)
                    print_player_score(i, players[i])
                    break
                # If break make player ignored in loop
                elif move == "stay":
                    players[i] = player_stayed(players[i])
                    break
            print()
        if player_out == len(players):
            break
    
    # Find the top score
    players = fix_scores(players)
    winners = get_winners(players, get_highest_score(players))
    
    # Print the winner
    print_winners(winners)

def draw_card():
    deck = ([i for i in range(1, 10)] * 4) + ([10] * 16)
    shuffle(deck)
    
    for i in range(56):
        yield deck[0]
        del deck[0]

def get_highest_score(players):
    top_score = 0
    
    for player in players:
        if top_score < player < 22:
            top_score = player
    return top_score

def get_winners(players, top_score):
    winners = []
    
    for player in players:
        if player == top_score:
            winners.append(player)
    return winners

def draw_two_cards(players, deck):
    output_score = []

    for player in players:
        output_score.append(next(deck) + next(deck))
    
    return output_score

def print_player_score(player_number, player):
    print("Player {0}: {1}".format(player_number + 1, player))

def player_stayed(player):
    return player + 1000

def print_winners(winners):
    for index, winner in enumerate(winners):
        print("Player {0} wins with: {1}".format(index + 1, winner))

def fix_scores(players):
    for i in range(len(players)):
        players[i] -= 1000 if players[i] >= 1000 else players[i]
    return players

if __name__ == '__main__':
    main()