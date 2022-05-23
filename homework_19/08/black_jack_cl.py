import random


class Two:
    def __init__(self):
        self.name = '2'
        self.points = 2


class Three:
    def __init__(self):
        self.name = '3'
        self.points = 3


class Four:
    def __init__(self):
        self.name = '4'
        self.points = 4


class Five:
    def __init__(self):
        self.name = '5'
        self.points = 5


class Six:
    def __init__(self):
        self.name = '6'
        self.points = 6


class Seven:
    def __init__(self):
        self.name = '7'
        self.points = 7


class Eight:
    def __init__(self):
        self.name = '8'
        self.points = 8


class Nine:
    def __init__(self):
        self.name = '9'
        self.points = 9


class Ten:
    def __init__(self):
        self.name = '10'
        self.points = 10


class Jack:
    def __init__(self):
        self.name = 'Jack'
        self.points = 10


class Queen:
    def __init__(self):
        self.name = 'Queen'
        self.points = 10


class King:
    def __init__(self):
        self.name = 'King'
        self.points = 10


class Ace:
    def __init__(self, sum_score=21):
        self.name = 'Ace'
        if sum_score <= 10:
            self.points = 11
        else:
            self.points = 1


class BlackJackGame:
    def __init__(self):
        self.pack_of_cards = [[Two().name, Two().points], [Three().name, Three().points], [Four().name, Four().points],
                              [Five().name, Five().points], [Six().name, Six().points], [Seven().name, Seven().points],
                              [Eight().name, Eight().points], [Nine().name, Nine().points], [Ten().name, Ten().points],
                              [Jack().name, Jack().points], [Queen().name, Queen().points],
                              [King().name, King().points], [Ace().name, Ace().points]] * 4
        self.your_score = 0
        self.croupier_score = 0

    def random_card(self, score, who_plays):
        if len(self.pack_of_cards) != 0:
            card = random.choice(self.pack_of_cards)
            card_points = card[1]
            card_name = card[0]
            self.pack_of_cards.remove(card)
        else:
            raise IndexError
        if card_name == 'Ace':
            score += Ace(score).points
        else:
            score += card_points
        self.who_get_card(score, card_name, who_plays)
        return score

    @staticmethod
    def who_get_card(score, card_name, who_plays):
        if who_plays == 'H':
            print(f'Your random card is {card_name}. You have {score} points for it.')
        else:
            print(f"Croupier's random card is {card_name}. He has {score} points for it.")

    def game(self):
        your_score = 0
        croupier_score = 0
        print('Initial 2 random cards:')
        print('YOURS:')
        for i in range(2):
            print(i + 1, '-> ', end='')
            your_score += self.random_card(self.your_score, 'H')
        print('Your total score: ', your_score)
        print("CROUPIER'S:")
        for i in range(2):
            print(i + 1, '-> ', end='')
            croupier_score += self.random_card(self.croupier_score, 'C')
        print("Croupier's total score: ", croupier_score)
        while True:
            answer = int(input('Do you want to take a card? 1 - yes, 2 - no \n'))
            if answer == 1:
                your_score = self.random_card(your_score, 'H')
                if croupier_score < 19 and your_score <= 21:
                    croupier_score = self.random_card(croupier_score, 'C')
                if your_score > 21 or croupier_score == 21:
                    print('You lost :(')
                    break
                elif your_score == 21 and croupier_score == 21:
                    print('Draw.')
                    break
                elif your_score == 21 or croupier_score > 21:
                    print('You won :)')
                    break
            elif answer == 2:
                if your_score > croupier_score and croupier_score < 19:
                    while croupier_score < 19:
                        croupier_score = self.random_card(croupier_score, 'C')
                if your_score < croupier_score <= 21:
                    print(f'You lost, you have {your_score} points, croupier has {croupier_score} points.')
                else:
                    print(f'You won, you have {your_score} points, croupier has {croupier_score} points.')
                break

    def start_game(self):
        random.shuffle(self.pack_of_cards)
        print('Game has started.')
        self.game()
