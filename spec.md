# Baloney Sandwich KOTH
## Introduction
In this King Of The Hill Challenge, your bots will be playing Baloney Sandwich.
### How Baloney Sandwich is played
1. First, the entire deck is dealt equally to all players (EVERY BOT PLAYS; if there is more than 26 bots, it will be 2 decks mixed together).
2. Then, the player with the ace of spades goes first.
3. They play all of their aces
   * However! They could opt to "cheat" and instead play cards that are not aces, or mix and match aces with other cards.
4. Every other player has their `call_bs` (bs = Baloney Sandwich) method called after this play, in turn until a player returns `True`; if a player returns `True` then the cards played are "revealed".
   * Every player has their `bs_call_outcome` method to "reveal" the cards
   * If no player returns `True` but the player was lying, the `pb` method is called (pb = Peanut Butter)
5. Play continues with twos, threes, etc.; after kings, start over at aces
## Creating A Player
Your player should be in this format:
```python
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
        return False # never calls "Baloney Sandwich"
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
        pass # Couldn't care less

    def play_cards(self, card_rank: int) -> list[int]:
        """
        The rank you will claim to play is card_rank
        """
        # Magic decision maker
        return self.hand[0] # Always plays the first thing in hand
```
A player has access to the following instance variables:
* `self.store`: A dictionary that is empty by default. The only instance variable allowed to be written to.
* `self.hand`: A list of `int`s, each representing a card (1 is Ace, 11-13 are face cards)

### Testing Your Player
The controller can be found at 

## Rules
### Runtime Disqualifications
* You must play at least one card every turn
* You can't play cards you dont have in your hand
* You can't take longer than one second to return from a function
### Pre-runtime Disqualifications
* No reading or writing to controller, runtime, or other submissions (bots can't read them; you can if you feel like it)
* Only write to `self.store` instance variable
  * Other variables inside function scope are of course OK
* Don't design a bot to defend or support specific bots
* Bots can't use the same strategy as another bot