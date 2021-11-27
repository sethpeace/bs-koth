class AbstractBSPlayer:
    def __init__(self, hand: list[int]):
        self.hand: list[int] = hand
        self.store: dict = {}
        self.player_name: str = self.__class__.__name__

    def call_bs(self, player_name: str, card_rank: int, number_of_cards: int) -> bool:
        raise NotImplementedError

    def bs_call_outcome(self, player_name: str, caller_name: str, card_rank: int, cards: list[int], cheated: bool):
        raise NotImplementedError

    def pb(self, player_name: str, card_rank: int, number_of_cards: int):
        raise NotImplementedError

    def play_cards(self, card_rank: int) -> list[int]:
        raise NotImplementedError
