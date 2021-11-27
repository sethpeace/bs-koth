from abstract_bs_player import AbstractBSPlayer


class ExamplePlayer(AbstractBSPlayer):
    def __init__(self, hand: list[int]):
        super().__init__(hand)
        # Any necessary initialization goes here

    def call_bs(self, player_name: str, card_rank: int, number_of_cards: int) -> bool:
        """
        player_name is the name of the bot who just played
        The number of cards they played is number_of_cards
        The claimed rank is card_rank (1 is Ace; 11-13 are face cards)
        """
        # Magic decision maker
        return False  # never calls "Baloney Sandwich"
        # return True would always call "Baloney Sandwich"

    def bs_call_outcome(self, player_name: str, caller_name: str, card_rank: int, cards: list[int], cheated: bool):
        """
        player_name is the name of the bot who just played
        caller_name is the name of the bot who called "Baloney Sandwich"
        The claimed rank is card_rank
        The cards they played is cards
        cheated is True if the player cheated
        """
        pass  # Couldn't care less

    def pb(self, player_name: str, card_rank: int, number_of_cards: int):
        """
        player_name is the name of the bot who just played
        The number of cards they played is number_of_cards
        The claimed rank is card_rank (1 is Ace; 11-13 are face cards)
        """
        pass  # Couldn't care less

    def play_cards(self, card_rank: int) -> list[int]:
        """
        The rank you will claim to play is card_rank
        """
        # Magic decision maker
        return [self.hand[0]]  # Always plays the first thing in hand
