import chess
import chess.svg
import chess.pgn
import chess.polyglot
from IPython.display import SVG

board = chess.Board()
SVG(chess.svg.board(board=board, size=400))

def evaluate_board():
	if board.is_checkmate():
		if board.turn:
			return -9999
		else:
			return 9999
	
	if board.is_stalemate():
		return 0
	if board.is_insufficient_material():
		return 0
		
	wp = len(board.pieces(chess.PAWN, chess.WHITE))
	wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
	wb = len(board.pieces(chess.BISHOP, chess.WHITE))
	wr = len(board.pieces(chess.ROOK, chess.WHITE))
	wq = len(board.pieces(chess.QUEEN, chess.WHITE))
	bp = len(board.pieces(chess.PAWN, chess.BLACK))
	bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
	bb = len(board.pieces(chess.BISHOP, chess.BLACK))
	br = len(board.pieces(chess.ROOK, chess.BLACK))
	bq = len(board.pieces(chess.QUEEN, chess.BLACK))
	
	material = 100 * (wp-bp) + 320 * (wn-bn) + 330 *(wb-bb) + 500*(wr - br) + 900 *(wq-bq)
	
	pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
	pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
		for i in board.pieces(chess.PAWN, chess.BLACK)])
		
	knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
	knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
		for i in board.pieces(chess.KNIGHT, chess.BLACK)])
		
	bishopsq = sum([bishoptable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
	bishopsq = bishopsq + sum([-bishoptable[chess.square_mirror(i)]
		for i in board.pieces(chess.BISHOP, chess.BLACK)])
		
	rooksq = sum([rooktable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
	rooksq = rooksq + sum([-rooktable[chess.square_mirror(i)]
		for i in board.pieces(chess.ROOK, chess.BLACK)])
	
	queensq = sum([queentable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
	queensq = queensq + sum([-queentable[chess.square_mirror(i)]
		for i in board.pieces(chess.QUEEN, chess.BLACK)])
		
	kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
	kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
		for i in board.pieces(chess.KING, chess.BLACK)])
		
	eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
	if board.turn:
		return eval
	else:
		return -eval
		
pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishoptable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rooktable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

queentable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]


def alphabeta(alpha, beta, depthleft):
	bestscore = -9999
	if(depthleft == 0):
		return quiesce(alpha, beta)
	for move in board.legal_moves:
		board.push(move)
		score = -alphabeta(-beta, -alpha, depthleft -1)
		board.pop()
		if(score >= beta):
			return score
		if(score > bestscore):
			bestscore = score
		if(score > alpha):
			alpha = score
	return bestscore
	

def quiesce(alpha, beta):
	stand_pat = evaluate_board()
	if(stand_pat >= beta):
		return beta
	if(alpha < stand_pat):
		alpha = stand_pat
		
	for move in board.legal_moves:
		if board.is_capture(move):
			board.push(move)
			score = -quiesce(-beta, -alpha)
			board.pop()
			
			if(score >= beta):
				return beta
			if(score > alpha):
				alpha = score
	return alpha
	
def selectmove(depth):
	try:
		move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(board).move()
		movehistory.append(move)
		return move
	except:
		bestMove = chess.Move.null()
		bestValue = -9999
		alpha = -10000
		beta = 10000
		for move in board.legal_moves:
			board.push(move)
			boardValue = -alphabeta(-beta, -alpha, depth-1)
			if boardValue > bestValue:
				bestValue = boardValue;
				bestMove = move
			if(boardValue > alpha):
				alpha = boardValue
			board.pop()
		movehistory.append(bestMove)
		return bestMove

movehistory = []
board = chess.Board()
mov = selectmove(3)
board.push(mov)

game = chess.pgn.Game()
game.headers["Event"] = "Example"
game.headers["Round"] = 1

while not board.is_game_over(claim_draw=True):
	if board.turn:
		move = selectmove(3)
		board.push(move)
	else:
		move = selectmove(1)
		board.push(move)
		
game.add_line(movehistory)
game.headers["result"] = str(board.result(claim_draw=True))
print(game)
SVG(chess.svg.board(board=board, size=400))

