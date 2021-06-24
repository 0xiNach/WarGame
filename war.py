from game import Game
import random


class War(Game):

    def __init__(self, player_names, num_players=2, max_players=2):
        super().__init__(num_players, max_players)
        self.player_names = player_names
        assert self.num_players < self.max_players + 1, f"Oops, War does not support more than {self.max_players} players."    

    def war(self, p1, p2, p1_card, p2_card, recursion=False):
        """Method to handle war

        :param p1       : All cards of Player1
        :param p2       : All cards of Player2
        :param p1_card  : Current face up card of Player1
        :param p2_card  : Current face up card of Player2
        :param recursion: Bool, if method is called by recursion

        :return p1: updated cards of Player1
        :return p2: updated cards of Player2

        """

        # Drawing face down cards
        p1_card_down = p1.pop(0)
        p2_card_down = p2.pop(0)

        # Drawing face up cards
        p1_card_up = p1.pop(0)
        p2_card_up = p2.pop(0)

        # if both face up cards are same again
        if p1_card_up[1] == p2_card_up[1]:

            # Check if both players have enough cards to play War
            flag = self.war_check(p1, p2, p1_card, p2_card)
            if flag:
                p1, p2 = flag
                return p1, p2
            else:
                # recursive call
                p1, p2 = self.war(p1, p2, p1_card_up, p2_card_up, recursion=True)
        if recursion:
            if p1_card_up[1] > p2_card_up[1]:
                p1.extend([p2_card_up, p1_card_up, p2_card_down, p1_card_down])
            else:
                p2.extend([p2_card_up, p1_card_up, p2_card_down, p1_card_down])
        else:
            if p1_card_up[1] > p2_card_up[1]:
                p1.extend([p2_card_up, p1_card_up, p2_card_down, p1_card_down,  p2_card, p1_card])
            else:
                p2.extend([p2_card_up, p1_card_up, p2_card_down, p1_card_down,  p2_card, p1_card])
        return p1, p2   

    def battle(self, p1, p2):
        """Method to handle Battle

        :param p1       : All cards of Player1
        :param p2       : All cards of Player2

        :return p1: updated cards of Player1
        :return p2: updated cards of Player2
        """

        # draw face up cards
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        
        # if both face up cards are same
        if p1_card[1] == p2_card[1]:
            # Check if both players have enough cards to play War
            flag = self.war_check(p1, p2, p1_card, p2_card)
            if flag:
                p1, p2 = flag
                return p1, p2
            else:
                p1, p2 = self.war(p1, p2, p1_card, p2_card)       
        elif p1_card[1] > p2_card[1]:
            p1.extend([p1_card, p2_card])
        else:
            p2.extend([p1_card, p2_card])
        return p1, p2

    def win_check(self, p1, p2):
        """Helper method to check if any player won the game

        :param p1       : All cards of Player1
        :param p2       : All cards of Player2

        :retrun: None or results of the game        
        """

        # if both player has cards in hand
        if p1 != [] and p2 != []:
            return None
        # if Player1 has no cards in hand    
        elif p1 == [] and p2 is not None:
            return f'Congrats, {self.player_names[1]} wins the War.'
        else:
            return f'Congrats, {self.player_names[0]} wins the War.'

    def war_check(self, p1, p2, p1_card, p2_card):
        """helper method to check if both players can play War

        :param p1       : All cards of Player1
        :param p2       : All cards of Player2
        :param p1_card  : Current face up card of Player1
        :param p2_card  : Current face up card of Player2
        :param recursion: Bool, if method is called by recursion

        :return p1, p2 or Bool: updated cards of Player1 and Player2
        """

        # ASSUMPTION: if any player has not enough cards to play war
        # then he will lose the game
        # Check if any players have enough card to play War
        if len(p1) < 2 or len(p2) < 2:
            return ([], p2+p1+[p1_card, p2_card]) if len(p1) < len(p2) else (p1+p2+[p1_card, p2_card], [])
        else:
            return False

    def start(self):
        """Method to start the game

        :return: Result of the game
        """

        # dealing half of the cards from deck randomly to Player1
        player1 = set(random.sample(self.card_deck, len(self.card_deck)//2))
        # other half to player2
        player2 = list(self.card_deck.difference(player1))
        player1 = list(player1)

        # ASSUMPTION: Game is consider as Draw if no results in 5000 try
        n = 0
        while n < 5000:
            # check if any player has win the game
            winner = self.win_check(player1, player2)
            if winner:
                return winner
            else:
                player1, player2 = self.battle(player1, player2)   
            n += 1
        return "It's a Draw!"
