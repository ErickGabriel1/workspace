import random
import os

def cards_draw(hand, quantity):
    
    for card in range(0, quantity):
        key = random.choice(list(cards.keys()))
        value = random.choice(cards[key])
        hand.append((value, key))
        cards[key].remove(value)
    return hand
    


print("Do wana play a game of Blackjack? Type 'y' or 'n': ")
if input().lower() != 'y':
    exit()

while(True):

    end_game = False
    os.system('cls')

    cards = {
    "♥": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "♦": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "♣": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "♠": [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    }

    user_hand = []
    computer_hand = []

    cards_draw(user_hand, 2)
    cards_draw(computer_hand, 2)

    print(f"your cards are: {', '.join(str(value) + naipe for value, naipe in user_hand)}, current score: {sum([card[0] for card in user_hand])}\n")
    print(f"Computer's first card: {str(computer_hand[0][0])+computer_hand[0][1]}\n")

    choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    os.system('cls')

    while choice == 'y':
        cards_draw(user_hand, 1)
        print(f"your cards are: {', '.join(str(value) + naipe for value, naipe in user_hand)}, current score: {sum([card[0] for card in user_hand])}\n")
        if sum([card[0] for card in user_hand]) > 21:
            print(f"Computer's final hand: {', '.join(str(value) + naipe for value, naipe in computer_hand)}, final score: {sum([card[0] for card in computer_hand])}\n")
            print("You went over. You lose 😤")
            end_game = True
            break
            
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        os.system('cls')
    
    if sum([card[0] for card in computer_hand]) < 17:
        cards_draw(computer_hand, 1)
        if sum([card[0] for card in computer_hand]) > 21:
            print(f"Computer's final hand: {', '.join(str(value) + naipe for value, naipe in computer_hand)}, final score: {sum([card[0] for card in computer_hand])}\n")
            print(f"user's final hand: {', '.join(str(value) + naipe for value, naipe in user_hand)}, final score: {sum([card[0] for card in user_hand])}\n")
            print("Opponent went over. You win 😁")
            end_game = True

    if not end_game:
        final_user_score = sum([card[0] for card in user_hand])
        final_computer_score = sum([card[0] for card in computer_hand])

        if final_user_score > final_computer_score:
            print(f"Computer's final hand: {', '.join(str(value) + naipe for value, naipe in computer_hand)}, final score: {final_computer_score}\n")
            print(f"user's final hand: {', '.join(str(value) + naipe for value, naipe in user_hand)}, final score: {final_user_score}\n")
            print("You win 😃")
        elif final_user_score < final_computer_score:
            print(f"Computer's final hand: {', '.join(str(value) + naipe for value, naipe in computer_hand)}, final score: {final_computer_score}\n")
            print(f"user's final hand: {', '.join(str(value) + naipe for value, naipe in user_hand)}, final score: {final_user_score}\n")
            print("You lose 😤")
        else:
            print(f"Computer's final hand: {', '.join(str(value) + naipe for value, naipe in computer_hand)}, final score: {final_computer_score}\n")
            print(f"user's final hand: {', '.join(str(value) + naipe for value, naipe in user_hand)}, final score: {final_user_score}\n")
            print("It's a draw 🙃")
    
    print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if input().lower() != 'y':
        break   

    
