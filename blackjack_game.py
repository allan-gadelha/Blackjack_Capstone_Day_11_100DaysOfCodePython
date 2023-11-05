from blackjack_art import logo
import random

#Start cards, we're making it simpler, the deck is infinite, so if a card is drawn it stay in the deck
#Ace count as 11 until the user goes over 21, then it becomes 1.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def call_cards():
    """Function that call the cards for user or computer"""
    return random.choice(cards)

def ask_for_card():
    """Function that keep asking the player if he wants another card, till a valid input pass through"""
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card in ['y', 'n']:
            return another_card
        print("Invalid input. Please type 'y' or 'n'.")

def initial_draw(user, computer):
    """Function that make the inital drawing of cards"""
    for _ in range(2):
        user.append(call_cards())
        computer.append(call_cards())

def results(user_card, computer_card, stage):
    """Function to print out the results, dependeding on the stage!"""
    check_ace(user_card, computer_card)
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    
    if stage == "first":
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's cards: {computer_card}")
    elif stage == "final":
        print(f"Your {stage} hand: {user_card}, final score: {user_score}")
        print(f"Computer's {stage} hand: {computer_card}, final score: {computer_score}")

    return user_score, computer_score

def check_bust(user_card, computer_card):
    """Function to check if the user has busted after drawing a new card"""
    check_ace(user_card, computer_card)
    user_score = sum(user_cards)
    if user_score > 21:
        print("You've busted!")
        return True
    return False

def check_blackjack(hand):
    """Function to check if a hand is a blackjack"""
    if sum(hand) == 21 and len(hand) == 2:
        return True
    return False

def check_ace(user_card, computer_card):
    """Function that find if there's a Ace in the cards and chance the value of it
    if the sum is higher than 21"""
    if 11 in user_card and sum(user_card) > 21:
        index = user_card.index(11)
        user_card[index] = 1
    
    if 11 in computer_card and sum(computer_card) > 21:
        index = computer_card.index(11)
        computer_card[index] = 1

def winner(user_score, computer_score):
    """Function to check the Winner"""
    if user_score > 21 and computer_score > 21:
        print("Both busted, it's a draw!")
    elif user_score <= 21 and computer_score > 21:
        print("Computer busted, You Win!")
    elif user_score > 21 and computer_score <= 21:
        print("You busted, Computer Win!")
    elif user_score <= 21 and computer_score <= 21:
        if user_score == computer_score:
            print("It's a Draw!")
        elif user_score < computer_score:
            print("Computer Win!")
        else:
            print("You Win!")

def computer_draw(computer_cards):
    """Function to make the computer keep drawing when his score is lesser than 17"""
    while sum(computer_cards) < 17:
        computer_cards.append(call_cards())
    return computer_cards


#Starting the game!
keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while keep_playing == "y":
    #Logo
    print(logo)

    #List for Holding Cards
    user_cards = []
    computer_cards = []

    #stage for results
    stage1 = "first"
    stage2 = "final"

    #Scores
    user_score = 0
    computer_score = 0

    #Inital draw of cards
    initial_draw(user_cards, computer_cards)

    #Check for blackjacks
    user_blackjack = check_blackjack(user_cards)
    computer_blackjack = check_blackjack(computer_cards)

    if computer_blackjack and user_blackjack:
        print("Both players have blackjack! Draw!")
    elif computer_blackjack:
        print("Computer has blackjack! You lose!")
    elif user_blackjack:
        print("You have blackjack! You win!")
    else:
        
        #Getting the first cards and score!
        user_score, computer_score = results(user_cards, computer_cards, stage1)

        #If the player want another card
        another_card = ask_for_card()

        #Asking another card for the player till he don't want anymore or till he bust!!
        while another_card == "y":
                user_cards.append(call_cards())
                if check_bust(user_cards, computer_cards):
                    break
                user_score, computer_score = results(user_cards, computer_cards, stage1)
                another_card = ask_for_card()

        #Time to get the computer's cards
        computer_cards = computer_draw(computer_cards)
        
        #Getting the full score now through results
        user_score, computer_score = results(user_cards, computer_cards, stage2)
        
        #Getting how won!
        winner(user_score, computer_score)

        #In case the player want's to play another round
        keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if keep_playing == "n":
                break