from abstract_bs_player import AbstractBSPlayer


class ExamplePlayer(AbstractBSPlayer):
    def __init__(self, hand: list[int]):
        super().__init__(hand)
        # Any necessary initialization goes here

    def call_bs(self, player_name: str, card_rank: int, number_of_cards: int) -> bool:
        return bool(int(input(f"<1> call_bs({player_name!r}, {card_rank!r}, {number_of_cards!r}) -> ")))

    def bs_call_outcome(self, player_name: str, caller_name: str, card_rank: int, cards: list[int], cheated: bool):
        print(f"<1> bs_call_outcome({player_name!r}, {caller_name!r}, {card_rank!r}, {cards!r}, {cheated!r})")

    def pb(self, player_name: str, card_rank: int, number_of_cards: int):
        print(f"<1> pb({player_name!r}, {card_rank!r}, {number_of_cards!r})")

    def play_cards(self, card_rank: int) -> list[int]:
        return_val = []
        for i in range(int(input(f"<1> (hand: {self.hand}; len) play_cards({card_rank!r}) -> "))):
            return_val.append(self.hand[int(input(f"<1> (hand: {self.hand}; {i + 1}) play_cards({card_rank!r}) -> "))])
        return return_val


class ExamplePlayer2(AbstractBSPlayer):
    def __init__(self, hand: list[int]):
        super().__init__(hand)
        # Any necessary initialization goes here

    def call_bs(self, player_name: str, card_rank: int, number_of_cards: int) -> bool:
        return bool(int(input(f"<2> call_bs({player_name!r}, {card_rank!r}, {number_of_cards!r}) -> ")))

    def bs_call_outcome(self, player_name: str, caller_name: str, card_rank: int, cards: list[int], cheated: bool):
        print(f"<2> bs_call_outcome({player_name!r}, {caller_name!r}, {card_rank!r}, {cards!r}, {cheated!r})")

    def pb(self, player_name: str, card_rank: int, number_of_cards: int):
        print(f"<2> pb({player_name!r}, {card_rank!r}, {number_of_cards!r})")

    def play_cards(self, card_rank: int) -> list[int]:
        return_val = []
        for i in range(int(input(f"<2> (hand: {self.hand}; len) play_cards({card_rank!r}) -> "))):
            return_val.append(self.hand[int(input(f"<2> (hand: {self.hand}; {i+1}) play_cards({card_rank!r}) -> "))])
        return return_val
