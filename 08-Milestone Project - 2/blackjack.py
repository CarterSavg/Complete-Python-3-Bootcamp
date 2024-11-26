import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Player:
    
    def __init__ (self, name = "dealer", balance = 100):
        self.name = name
        self.balance = balance
        self.hand = []
        self.hand_value = 0
        self.wins = 0
        self.aces = 0

    def clear_hand(self):
        self.hand = []
        self.hand_value = 0
        self.aces = 0

    def adjust_balance(self, amount):
        self.balance += amount
    
    def dealer_show(self):
        print(f"Dealer is showing {self.hand[0]}")

    def show_hand(self):
        temp = ""
        for card in self.hand:
            temp += f"{card.__str__()}\n"
        print(f"You have a total of {self.hand_value} with the following cards:\n{temp}")
    
    def show_hand_dealer(self):
        temp = ""
        for card in self.hand:
            temp += f"{card.__str__()}\n"
        print(f"Dealer has a total of {self.hand_value} with the following cards:\n{temp}")

    def __str__(self):
        return f"{self.name} has a balance of: {self.balance} and {self.wins} wins"


class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()
        
def deal_hand(dealer, player, deck):
    '''Gives dealer and player both two cards'''
    for _ in range(0,2):
        card = deck.all_cards.pop()
        dealer.hand_value += card.value
        
        if card.value == 11:
            dealer.aces += 1
            
        dealer.hand.append(card)
        card = deck.all_cards.pop()
        player.hand_value += card.value
        if card.value == 11:
            player.aces += 1
        player.hand.append(card)

def get_bet(player):
    '''Gets bet from player returns it as an int'''
    bet = ""
    valid_bet = False
    while not valid_bet:
        bet = input(f"Balance {player.balance}\nHow much are you betting: ")
        if bet.isdigit() and int(bet) <= player.balance:
            valid_bet = True
    return int(bet)

def hit_me(player, deck):
    '''Asks player if they want any more cards and keeps asking till they bust or they dont want anymore'''
    hit = " "
    game = True
    if player.hand_value == 21:
        return True
    while game:
        hit = " "
        while hit not in ["Y", "N"]:
            player.show_hand()
            hit = input("Do you want another card? (Y / N)")

        if hit == "N":
            game = False
            break
        elif hit == "Y":
            card = deck.all_cards.pop()
            player.hand_value += card.value
            player.hand.append(card)
        if player.hand_value > 21:
            if player.aces == 0:
                return False
            else:
                player.aces -= 1
                player.hand_value -= 10
    return True

def check_win(player, dealer, deck):
    '''Checks if the player has beaten the dealer. Dealer will keep adding cards till they win or they bust (True = win False = lose)'''
    if player.hand_value == 21:
        return True
    while dealer.hand_value < player.hand_value and dealer.hand_value < 21:
        card = deck.all_cards.pop()
        dealer.hand_value += card.value
        dealer.hand.append(card)
    if dealer.hand_value > 21:
        if dealer.aces == 0:
            return False
        else:
            dealer.aces -= 1
            dealer.hand_value -= 10
        return True
    return False

def main():

    game = True
    name = input("Name: ")
    player = Player(name=name)
    dealer = Player()
    while game:
        dealer.clear_hand()
        player.clear_hand()
        if player.balance <= 0:
            print("You have no money left goodbye")
            return
        contin = " "
        while contin not in ["Y", "N"]:
            contin = input("Do you want to keep playing? (Y / N)")

        if contin == "N":
            game = False
            break

        bet = get_bet(player)
        deck = Deck()
        deck.shuffle()
        deal_hand(dealer, player, deck)
        dealer.dealer_show()
        if not hit_me(player, deck):
            print("BUST")
            player.adjust_balance(-bet)
        else:
            if check_win(player, dealer, deck):
                print("Win\n")
                player.show_hand()
                dealer.show_hand_dealer()
                player.adjust_balance(bet)
                player.wins += 1
            else:#lose
                print("Lose\n")
                player.show_hand()
                dealer.show_hand_dealer()
                player.adjust_balance(-bet)
        print(player)   
        #TODO Create game (pull cards and let player get hit, then do the same for dealer dealer goes till they win or bust)
main()
