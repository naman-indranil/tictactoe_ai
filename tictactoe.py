def printBoard(board):
	# This function prints out the board.
	# We have taken board as a list of 10 characters representing the board.
	# 0th position is ignored as we are taking input from user from 1 to 9
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[7] + '|' + board[8] + '|' + board[9])


def insertLetter():
	# Take the character from the player which they select ('X' or 'O') 
	# Returns a list with the player's character and the computer's character.
	character=''
	while not(character=='X' or character=='O'):
		print("Do you want to be 'X' or 'O'?")
		character = input().upper()

	if character == 'X':
		return ['X','O']
	else:
		return ['O','X']


def whoGoesFirst():
	# This function ask the player whether he want to start first or not
	print('Do you want to go first? (Y or N)')
	if  input().lower().startswith('y'):
		return 'player'
	else:
		return 'computer'



def playAgain():
	# This function asks the player whether he want to play again or not.
	print('Do you want to play again? (Yes or No)')
	return input().upper().startswith('Y')


def makeMove(board, character, pos):
	# This funtion assign the character on postion pos on the board.
	board[pos] = character


def isWinner(board,character):
	# This function checks and return true if the player has won else it returns false
	# We check winner by considering all possible ways i.e same characters in rows,columns or the 2 diagonals
	return ((board[1]==character and board[2]==character and board[3]==character) or
			(board[4]==character and board[5]==character and board[6]==character) or
			(board[7]==character and board[8]==character and board[9]==character) or
			(board[1]==character and board[4]==character and board[7]==character) or
			(board[2]==character and board[5]==character and board[8]==character) or
			(board[3]==character and board[6]==character and board[9]==character) or
			(board[1]==character and board[5]==character and board[9]==character) or
			(board[3]==character and board[5]==character and board[7]==character))


def isSpaceFree(board, pos):
	#check whether the board at position pos is free or not
	#return true if the board is free else return false
	return board[pos] == ' '


def getPlayerMove(board):
	# This function takes the player move and check whether it is valid or not
	move = ''
	allMoves = '1 2 3 4 5 6 7 8 9'
	while move not in allMoves.split() or not isSpaceFree(board,int(move)):
		print('Please, Enter yout move (1-9).') 
		move = input()
		if move not in allMoves.split():
			print('Invalid Move, Enter a valid digit (1-9)')
		elif not isSpaceFree(board,int(move)):
			print('Invalid Move, the postion is already occupied.')
	return int(move)


def minimax(board, depth, isMax, alpha, beta, computerLetter):
	# This function uses minimax algorithm along with alpha beta pruning to calculate the best score
	# for the current move
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if isWinner(board, computerLetter):
		return 10
	if isWinner(board, playerLetter):
		return -10
	if isBoardFull(board):
		return 0

	if isMax:
		best = -1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = computerLetter
				best = max(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) - depth)
				alpha = max(alpha, best)
				board[i] = ' '

				if alpha >= beta:
					break

		return best
	else:
		best = 1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = playerLetter
				best = min(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) + depth)
				beta = min(beta, best)
				board[i] = ' '

				if alpha >= beta:
					break

		return best


def findBestMove(board, computerLetter):
	# This function takes computer character and find the best move
	# if computerLetter == 'X':
	# 	playerLetter = 'O'
	# else:
	# 	playerLetter = 'X'

	bestVal = -1000
	bestMove = -1


	for i in range(1,10):
		if isSpaceFree(board, i):
			board[i] = computerLetter

			moveVal = minimax(board, 0, False, -1000, 1000, computerLetter)

			board[i] = ' '

			if moveVal > bestVal:
				bestMove = i
				bestVal = moveVal

	return bestMove


def isBoardFull(board):
	# Return True if every space on the board has been taken. Otherwise return False.
	# We check it by counting the no of ' ' in board.
	if(board.count(' ')>1):
		return False
	else:
		return True


print('\nWelcome to Tic Tac Toe!\n')
print('Reference of numbering on the board')
printBoard('0 1 2 3 4 5 6 7 8 9'.split())
print('')

while True:
	# Reset the board
	theBoard = [' '] * 10
	playerLetter, computerLetter = insertLetter()
	turn = whoGoesFirst()
	print('The ' + turn + ' will go first.')
	playing = True

	while playing:
		if turn == 'player':
			printBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				printBoard(theBoard)
				print('You won the game, Good Job!')
				playing = False
			else:
				if isBoardFull(theBoard):
					printBoard(theBoard)
					print('The game is a tie')
					break
				else:
					turn = 'computer'
		else:
			move = findBestMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				printBoard(theBoard)
				print('Sorry!, You lose the game')
				playing = False
			else:
				if isBoardFull(theBoard):
					printBoard(theBoard)
					print('The game is a tie')
					break
				else:
					turn = 'player'
	if not playAgain():
		break