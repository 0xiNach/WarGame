from abc import ABCMeta, abstractmethod

class Game(object):

    def __init__(self, num_players, max_players):
        self.num_players = num_players
        self.max_players = max_players
        self.card_deck = {(suite, num)
                          for suite in ['spade', 'club', 'heart', 'diamond']
                          for num in range(2, 15)}

    @abstractmethod
    def start(self):
        """Implement start method that starts the game
        :return: Result of the game
        """
        pass


