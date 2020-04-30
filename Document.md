# Documents

### enviroment
- python 3.7.3
- numpy 

### Run Code and play

```
# To the target folder
jackson@bdalab30000:~/AI$

# Run python and the 15game.py
jackson@bdalab30000:~/AI$ python 15game.py

# Choose User first or AI first
# only can type y or n
User First ? (y/n)

# Choose board size
# only can type 4 or 6 
Board Size ? (4/6)

```
After chosen first player and board size, we can start the game, the following is initial state

![](https://i.imgur.com/dZsDDql.png)

At "input", player can type only int, and must be separated by spaces .

the position(row and column) cannot beyond the board size, and weight is represent the card value player wants to put in.

![](https://i.imgur.com/Um23fed.png)

After player played, the program will show the state after player's action, and the AI will do search and choose action.

The game will repeat these moves until the game end.

### Error detection

```
User_chess : [2, 8, 13]
AI_chess : [3, 5, 8]

# Can not put a card in position that already has a crad
input(row, col, weight)0 0 8
Had A Value Already !

# Can not beyond the board size
input(row, col, weight)5 5 8
Out of Board Range !

# Cannot use cards that have already been used or cards that are not in hand.
input(row, col, weight)1 1 3
You need to choose another card !

```
