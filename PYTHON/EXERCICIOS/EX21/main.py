import os
people_dict = {}
import time

def find_highest_bidder(bidding_dictionary):
    choice_name = ''  
    choice_bid = 0
    for people in people_dict:
        if bidding_dictionary[people] > choice_bid:
            choice_bid = bidding_dictionary[people]
            choice_name = people
    print(f"The highest bid was ${choice_bid:.2f} by {choice_name}")

print("Welcome to the secret auction program.")
time.sleep(2)

while(True):
    os.system('cls')
    name = str(input("What is your name?: "))
    bid = float(input("What's your bid?: $"))

    people_dict[name] = bid

    choice = str(input("Are there any other bidders? Type 'yes' or 'no'")).lower()
    if choice != 'yes' and choice != 'no':
        print("Escolha incorreta!")
    elif choice == 'no':
        break

find_highest_bidder(people_dict)

