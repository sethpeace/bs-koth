from abstract_bs_player import AbstractBSPlayer
from util import exit_after
from random import shuffle

# Import Bots Here
# from example import ExamplePlayer
from manualbot import ExamplePlayer, ExamplePlayer2


class Disqualified(Exception):
    pass


def deal(decks=1):
    deck = list(range(1, 14)) * 4 * decks
    shuffle(deck)

    hands = [[] for _ in range(4)]

    hand = 0
    for card in deck:
        hands[hand].append(card)
        hand += 1
        if hand >= len(hands):
            hand = 0

    return hands


def get_players():
    hands = deal((len(AbstractBSPlayer.__subclasses__()) // 26) + 1)
    players = AbstractBSPlayer.__subclasses__()
    shuffle(players)
    return [player(hands[i]) for i, player in enumerate(players)]


def play_cards(player, cards_played):
    for card in cards_played:
        if card in player.hand:
            player.hand.remove(card)
        else:
            raise Disqualified(player.player_name)


def check_cheating(player, rank, cards_played):
    cheated = False
    if not cards_played:
        raise Disqualified(player.player_name)
    for card in cards_played:
        if card != rank:
            cheated = True
            break
    return cheated


def call_bs(cheated, rank, cards_played, players, player, caller, discard_pile):
    for bot in players:
        exit_after(1)(bot.bs_call_outcome)(player.player_name, caller.player_name, rank, cards_played, cheated)
        if cheated:
            player.hand = [*player.hand, *discard_pile]
        else:
            caller.hand = [*caller.hand, *discard_pile]


def game_loop():
    players = get_players()
    player_turn = 0

    rank = 1

    discard_pile = []
    while True:
        player = players[player_turn]
        try:
            cards_played = exit_after(1)(player.play_cards)(rank)

            discard_pile = [*discard_pile, *cards_played]
            play_cards(player, cards_played)

            cheated = check_cheating(player, rank, cards_played)

            for caller in players:
                if caller.player_name != player.player_name and \
                   exit_after(1)(caller.call_bs)(player.player_name, rank, len(cards_played)):
                    call_bs(cheated, rank, cards_played, players, player, caller, discard_pile)
                    discard_pile = []
                    break
            else:
                if cheated:
                    for bot in players:
                        exit_after(1)(bot.pb)(player.player_name, rank, len(cards_played))
        except KeyboardInterrupt:
            raise Disqualified(player.player_name)

        player_turn += 1
        if player_turn >= len(players):
            player_turn = 0

        rank += 1
        if rank > 13:
            rank = 0

        print()


if __name__ == "__main__":
    game_loop()
