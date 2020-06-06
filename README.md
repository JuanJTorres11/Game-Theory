# Game-Theory
Identifies perfect equilibria in subgames using backward induction

## Data file structure:

The data file should be like this: 

'''
players: 2
nodes:
0;F;[1,2];1
1;T;(1,-1)
2;T;(-1,1)
'''

- Players: the number of players.
- Node: this is divided by the ';' character into:
	- Node id: unique id
	- Is leaf:
		- T:
			- Payoffs: this field must have a list of the payoffs, this must be consistent with the number of players.
		- F: 
			- Children: this field must have a list of the cildren ids enclosed in [].
			- Player: this field must be the number of a player, the player who decides the next node.