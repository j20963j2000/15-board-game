# 15-board-game
This is a simple board game 

# Readme

-Project Name : 15 Search Game
-Project Target : 
> Bulid a board game AI player using Search Algorithm

### Game Introduction

This board game is a 2 players game. Every player has same cards in hand initially, the game end up when both players have no card in hand.
![](https://i.imgur.com/VsI966j.png)

When each player put a card in, the “check-and-mark” algorithm will check and compute the total sum around the card, and the card will be marked and removed if the sum exceed 15. At the end of the game, the system will check and compute the remaining card value at the board for every player. The winner is the player who has the highest remaining card value.
![](https://i.imgur.com/mqiCJ0l.png)

### Game Target

Because the winning goes to highest remaining card value player, so a optimal player(or AI program) should figure out how to reduce opponent remaining card and keep its own remaining card value high.

So the best game winning target, in my opinion, is using the low value card to exchange opponent's high value card as much as possible.

> Game target is using the low value card to exchange opponent's high value card as much as possible.

### Search Design for AI program

I design a sacrifice ratio for computing the playing action benefit for each AI player action.

> Sacrifice Ratio : (alpha - beta)/card_ai_put_in

the alpha represent the AI player remaining board value when AI put a card in board, and the beta represent its opponent's remaining board value.

AI will scan every legal position in board, and try every card in hand to find every card' sacrifice ratio in every position. And choose the best ratio with lowest card value and the very position as the best next action.
![](https://i.imgur.com/WiCkNWw.png)

This Algorithm is much closer to the human thinking, and is oriented to the game target I just mentioned above.

And for the space complexity, because the program will memory the card in hand, so the search algorithm only have to memory the ratio for every position, so the space complexity is O(AI remaining card in hand * board_size^2).

> Space Complexity : O(cards * Board_size^2)

For time complexity, the search algorithm will scan every legal position with every remaining card in hand, so it will be same as space complexity.

> Time Complexity : O(cards * Board_size^2) 

For the search algorithm mentioned above, I only  compute 2 layer for search algorithm.

### Check and Mark

for checking remaining card value in board, there are three situations. 

![](https://i.imgur.com/URHqvEz.png)

for each situation, every card in board will be compute it surrounding sum and if the sum exceed 15, the center card will be removed and replaced with "X"

### Further advanced search algorithm

The search algorithm mentioned above is not really complete. Because it only depends on the move that its opponent had played at last round.

But it is enough to be a elementary level difficulty AI game player, for those players who play this game first, this elementary level AI is a good practice opponent.

If the players want to play against harder AI, we only need to stack the search algorithm, so that the AI will start to predict the player's next move and respond to that.
