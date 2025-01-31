import random
BLACKJACK = 21
MIN_BET = 1
MAX_BET = 100

categories = ['Hearts', 'Diamonds', 'Spade', 'Clubs']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in categories for card in cards]

def value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 1
    else:
        return int(card[0])

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
    return amount

def play(balance, bet):
    winner = False

    random.shuffle(deck)
    playerCard = [deck.pop(), deck.pop()]
    playerScore = sum(value(card) for card in playerCard)

    if any(card[0] == "Ace" for card in playerCard) and playerScore + 10 <= 21:
        playerScore += 10

    print(f"Player drew {playerCard} with score: {playerScore}")
    dealerCard = [deck.pop()]
    dealerScore = sum(value(card) for card in dealerCard)
    print(f"Dealer drew {dealerCard} with score: {dealerScore}")


    while playerScore < 21 and not winner:
        choice = input("Write 'hit' to request another card, write 'stand' to stop:  ")
        if choice == "hit":
            playerScore += hit()
            print(f"New Player Score: {playerScore}")
            if playerScore > 21:
                print("Dealer wins")
                balance -= bet
                True
                break
        elif choice == "stand":
            print()
            print("Dealer's turn!")
            while dealerScore < 17 and not winner:
                dealerScore += hit()
                if any(card[0] == "Ace" for card in dealerCard) and dealerCard + 10 <= 21:
                    dealerScore += 10
                print(f"Dealer Score: {dealerScore}")
                if playerScore == dealerScore:
                    print("Tie!")
                    winner = True
                    break
                elif dealerScore > 16 and dealerScore > playerScore:
                    print("Dealer wins")
                    balance -= bet
                    winner = True
                    break
                elif dealerScore < playerScore:
                    print("Player wins")
                    balance += bet
                    winner = True
                    break
                break

    return balance

def hit():
    card = [deck.pop()]
    newScore = sum(value(card) for card in card)
    print(f"Drew {card} with score: {newScore}")
    return newScore

def stand():
    newScore = 0
    return newScore

def main():
    balance = deposit()

    while True:
        betAmount = bet()
        if betAmount > balance:
            print(f"Bet is larger than balance. Current balance is ${balance}")
        else:
            break

    while True:
        print(f"Current balance is ${balance}, you're bet is ${betAmount}")
        print()
        if balance < betAmount:
            print("You're out of money!")
            repeat = input("Would you like to deposit more money? If yes, press enter, else type q to quit")
            balance = deposit()
            while True:
                betAmount = bet()
                if betAmount > balance:
                    print(f"Bet is larger than balance. Current balance is ${balance}")
                else:
                    break

            print(f"Current balance is ${balance}, you're bet is ${betAmount}")
            print()
            if repeat == "q":
                break

        answer = input("Print enter to play, q to quit")
        if answer == "q":
            break
        balance = play(balance, betAmount)
    print(f"You left with ${balance}")



main()
