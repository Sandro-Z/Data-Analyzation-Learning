import numpy as np
board=np.matrix(np.zeros((8,8)))

for x in range(np.shape(board)[0]):
	for y in range(np.shape(board)[1]):
		if (x+y)%2==0:
			board[x,y]=1
print(board)