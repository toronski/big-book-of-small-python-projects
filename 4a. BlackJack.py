






import sys, random


HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

BACKSIDE = 'backside'

def main():
    money = 5000

    while True:
        if money == 0:
            print('\nYou are bankrupt!')
            print('Want to play again? (y/n)')
            playAgain = input('> ')
            if playAgain.lower() == 'y':
                continue
            else:
                print('See you next time!')
                sys.exit()
        print()
        print('Budget: ', money)
        bet = getBet(money)
        deck = getDeck()

        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]
        showDealerHand = False
        displayHands(playerHand, dealerHand, showDealerHand)
        
        # Player moves
        while True:
            playerMove = getMove(playerHand)
            if playerMove == 'P':
                bet = getBet(bet)
                playerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, showDealerHand)
                break
            if playerMove == 'D':
                print('----------------------')
                playerHand.append(deck.pop())
                newCard = ' '.join(playerHand[-1])
                print('Card drawn: ', newCard)
                print('----------------------')
                displayHands(playerHand, dealerHand, showDealerHand)
                if getHandValue(playerHand) < 21:
                    continue
                elif getHandValue(playerHand) > 21:
                    print("\nPress 'ENTER'...")
                    break
            if playerMove == 'S' or getHandValue(playerHand) == 21:
                while not getHandValue(dealerHand) >= 17:
                        input("\nPress 'ENTER'...")
                        dealerHand.append(deck.pop())
                        displayHands(playerHand, dealerHand, showDealerHand)
                break

        showDealerHand = True
        print()
        displayHands(playerHand, dealerHand, showDealerHand)
        print()
        # Deciding who won
        if getHandValue(playerHand) == getHandValue(dealerHand) or getHandValue(playerHand) > 21 and getHandValue(dealerHand) > 21:
            print('Draw - your bet goes back to you.')
            continue
        elif getHandValue(playerHand) <= 21 and getHandValue(playerHand) > getHandValue(dealerHand):
            money += bet*2
            print(f'You won {bet*2} PLN!')
            continue
        elif getHandValue(dealerHand) <= 21 and getHandValue(dealerHand) > getHandValue(playerHand):
            money -= bet
            print(f'You lost {bet} PLN.')
            continue
        elif getHandValue(playerHand) > 21 and getHandValue(dealerHand) < 22:
            money -= bet
            print(f'You lost {bet} PLN.')
            continue
        elif getHandValue(playerHand) <= 21 and getHandValue(dealerHand) > 21:
            money += bet*2
            print(f'You won {bet*2} PLN!')
            continue
        
def getBet(maxBet):
    while True:
        print(f'How much you want to bet (1 - {maxBet})?')
        bet = input('> ')
        if bet.isdecimal():
            bet = int(bet)
            if 0 < bet <= maxBet:
                return bet
        else: 
            continue

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for courts in ('J', 'Q', 'K', 'A'):
            deck.append((courts, suit))
    
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand == False:
        print('\nCROUPIER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    else:
        print('CROUPIER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    print('\nPLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    cardsValue = 0
    
    for card in cards:
        if card[0] in ['J', 'Q', 'K']:
            cardsValue += 10
        elif card[0] == 'A':
            cardsValue += 10
            if cardsValue <= 20:
                cardsValue += 1
        else:
            cardsValue += int(card[0])
            
    return cardsValue

def displayCards(cards):
    rows = ['', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    
    for row in rows:
        print(row)


def getMove(playerHand):
    print()
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2:
            moves.append('(D)ouble down ')
        playerMove = ', '.join(moves) + '> '
        move = input(playerMove).upper()
        
        if len(playerHand) == 2 and move in ['H', 'S', 'D']:
            return move
        if len(playerHand) >= 3 and move in ['H', 'S']:
            return move
        else: continue

if __name__ == '__main__':
    main()