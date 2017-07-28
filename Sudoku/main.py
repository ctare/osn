#! cat input | python3 main.py

DATA_SIZE0 = 2
DATA_SIZE = DATA_SIZE0 ** 2

#/************************************************************************
#  問題 (答え) の表示							
#************************************************************************/
def print_board(board):
#  /* 問題 (答え) (board[y][x]) を表示する。 
#     数字がまだ決まっていないところには - を表示する。
#     <表示例>
#        - - 1 - 8 7 - 5 - 
#        - 5 - - 3 - - 8 - 
#        - - - - - 9 - - 3 
#        3 - - - - - 6 - - 
#        6 4 - - - - - 7 2 
#        - - 5 - - - - - 9 
#        7 - - 1 - - - - - 
#        - 1 - - 7 - - 2 - 
#        - 9 - 8 6 - 5 - -                               */
    for x in board:
        print(*map(lambda x: str(x) if x else "-", x))


#/************************************************************************
#   問題データの読み込み						
#************************************************************************/
def read_problem():
    return [list(map(int, input().split())) for x in range(DATA_SIZE)]


#/************************************************************************
#  空白マスの検出							
#    board[0][0]から順番にチェックしていき、
#    空白マス(0が入っているところ)があれば   TRUE  を返す
#           (x,y)が空白マス
#                                   なければ FALSE を返す 
#************************************************************************/
def find_blank(board):
    for f in board:
#      /* 行に0が含まれているならば TRUE を返す */
        if 0 in f:
            return True

    return False


#/************************************************************************
#   問題を解く
#************************************************************************/
def solve(x, y, board):
#  /* 1〜9のうちどの数字が使えるか */
#  /* 全て使用可にする */
    possible = [True for x in range(DATA_SIZE + 1)]


#  /* 途中経過を表示 */
    # print( "[途中経過]" );
    # print_board(board)

#  /* 空白のマスがなければ答えを表示する */
    if not find_blank(board):
        print( "[答え]" );
        print_board(board);
        return True

    if x >= DATA_SIZE:
        if y >= DATA_SIZE:
            return False
        else:
            return solve(0, y + 1, board)

    if board[y][x]:
        return solve(x + 1, y, board)
    else:
#  /* 横方向に boardの値を調べて、すでに使用されている数字のところは
#     possible を FALSE にする */
        possible = check_x(x, y, board, possible)
#  /* 縦方向に boardの値を調べて、すでに使用されている数字のところは
#     possible を FALSE にする */
        possible = check_y(x, y, board, possible)
#  /* DATA_SIZE0xDATA_SIZE0の枠の中の board の値を調べて、
#    すでに使用されている数字のところは possible を FALSE にする */
        possible = check_33(x, y, board, possible)

        for i, v in enumerate(possible[1:], 1):
            if v:
#               /* i を (x,y)に入れることができるとして探索 */
                board[y][x] = i
                if solve(x + 1, y, board): # 再帰呼び出し
                    return True
                board[y][x] = 0
    return False


#/************************************************************************
#   縦方向の検査
# boardの値を調べて、すでに使用されている数字のところは possible を FALSE にする
#************************************************************************/
def check_y(x, y, board, possible):
    possible = possible[:]
    for i in range(DATA_SIZE):
        if board[i][x]:
            possible[board[i][x]] = False
    return possible


#/************************************************************************
#   DATA_SIZE0xDATA_SIZE0の枠の中の検査
# boardの値を調べて、すでに使用されている数字のところは possible を FALSE にする
#************************************************************************/
def check_x(x, y, board, possible):
    possible = possible[:]
    for f in board[y]:
        if f:
            possible[f] = False
    return possible


#/************************************************************************
#   横方向の検査
# boardの値を調べて、すでに使用されている数字のところは possible を FALSE にする
#************************************************************************/
def check_33(x, y, board, possible):
    possible = possible[:]
    for i in range((y//DATA_SIZE0)*DATA_SIZE0, (y//DATA_SIZE0)*DATA_SIZE0 + DATA_SIZE0):
        for j in range((x//DATA_SIZE0)*DATA_SIZE0, (x//DATA_SIZE0)*DATA_SIZE0 + DATA_SIZE0):
            if board[i][j]:
                possible[board[i][j]] = False
    return possible

#/************************************************************************
#   メインプログラム
#************************************************************************/
#  /* 問題の読み込み */
try:
    board = read_problem()
except EOFError:
    print("使用法 : cat 問題ファイル | python3 main.py")
#  /* 問題の表示 */
print("[問題]");
print_board(board);	
#  /* 問題を解く */
solve(0, 0, board)
