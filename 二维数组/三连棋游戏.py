class TicTacToe:

    def __init__(self):
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'
    
    #下棋
    def mark(self, i, j):
        #边界检查
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        #检测棋盘是否被占位
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        #胜负不分，抛出异常
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        
        #这个检测判断是X先手，后到O
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'
            
    #检测是否赢得游戏
    def _is_win(self, mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0]  )

    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

if __name__ == "__main__":
    game = TicTacToe()

    game.mark(1, 1)
    print(game)
