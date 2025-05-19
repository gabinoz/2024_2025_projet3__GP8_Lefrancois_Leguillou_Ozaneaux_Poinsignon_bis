import pygame
import random
import copy
from game.utilities import *

pygame.font.init()
pygame.init()

class Game:
    def __init__(self, width=720, height=720):
        self.n_squares = 8
        self.board = self.create_board()
        self.turn = RED_PIECE
        self.winner = None
        self.draw = False
        self.selected_piece = None
        self.available_moves = []
        self.capture_moves = []
        self.move_count = 0
        self.width = width
        self.height = height
        self.square_size = width // self.n_squares

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Checkers")

        self.font = pygame.font.Font(None, 36)
        self.text_black_king = self.font.render("Q", True, WHITE)
        self.text_white_king = self.font.render("Q", True, BLACK)

    def create_board(self):
        board = [[0 for _ in range(self.n_squares)] for _ in range(self.n_squares)]
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                if (row + col) % 2 != 0:
                    if row < 3:
                        board[row][col] = BLACK_PIECE
                    elif row > 4:
                        board[row][col] = RED_PIECE
        return board

    def copy_game_state(self):
        new_game = Game(self.width, self.height)
        new_game.board = copy.deepcopy(self.board)
        new_game.turn = self.turn
        new_game.winner = self.winner
        new_game.draw = self.draw
        new_game.selected_piece = self.selected_piece
        new_game.available_moves = copy.deepcopy(self.available_moves)
        new_game.capture_moves = copy.deepcopy(self.capture_moves)
        new_game.move_count = self.move_count
        return new_game

    def draw_board(self):
        self.window.fill(WHITE)
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                if (row + col) % 2 != 0:
                    pygame.draw.rect(
                        self.window, BLACK,
                        (col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                    )
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                piece = self.board[row][col]
                if piece != 0:
                    x = col * self.square_size + self.square_size // 2
                    y = row * self.square_size + self.square_size // 2
                    radius = self.square_size // 2 - 10
                    color = BROWN if piece in [BLACK_PIECE, BLACK_KING] else RED
                    pygame.draw.circle(self.window, color, (x, y), radius)

                    if piece in [BLACK_KING, RED_KING]:
                        text = self.text_black_king if piece == BLACK_KING else self.text_white_king
                        self.window.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

        for move in self.available_moves:
            row, col = move
            pygame.draw.circle(
                self.window, BLUE,
                (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2),
                15
            )

        if self.winner:
            self.draw_winner()

    def draw_winner(self):
        if self.winner == "draw":
            text = self.font.render("Draw", True, BLACK)
        else:
            text = self.font.render(
                "Black wins" if self.winner == BLACK_PIECE else "Red wins", True, (0, 255, 0)
            )
        self.window.blit(
            text,
            (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2)
        )

    def get_available_moves(self, row, col):
        moves = []
        piece = self.board[row][col]
        if piece == BLACK_PIECE:
            moves.extend(self.get_diagonal_moves(row, col, 1))
        elif piece == RED_PIECE:
            moves.extend(self.get_diagonal_moves(row, col, -1))
        elif piece in [BLACK_KING, RED_KING]:
            moves.extend(self.get_diagonal_moves(row, col, 1))
            moves.extend(self.get_diagonal_moves(row, col, -1))
        return moves

    def get_diagonal_moves(self, row, col, direction):
        moves = []
        for d_col in [-1, 1]:
            new_row, new_col = row + direction, col + d_col
            if self.is_valid_move(new_row, new_col):
                moves.append((new_row, new_col))
            else:
                cap_row, cap_col = row + 2 * direction, col + 2 * d_col
                mid_row, mid_col = row + direction, col + d_col
                if self.is_valid_move(cap_row, cap_col):
                    if self.board[mid_row][mid_col] != 0 and self.board[mid_row][mid_col] not in [self.turn, self.turn + 2]:
                        moves.append((cap_row, cap_col))
        return moves

    def is_valid_move(self, row, col):
        return 0 <= row < self.n_squares and 0 <= col < self.n_squares and self.board[row][col] == 0

    def select(self, row, col):
        piece = self.board[row][col]
        if self.capture_moves:
            if (row, col) in self.capture_moves:
                self.move(row, col)
            return

        if piece != 0 and (piece == self.turn or piece == self.turn + 2):
            self.selected_piece = (row, col)
            self.available_moves = self.get_available_moves(row, col)
        elif self.selected_piece:
            self.move(row, col)

    def move(self, row, col):
        if (row, col) in self.available_moves:
            from_row, from_col = self.selected_piece
            self.board[row][col] = self.board[from_row][from_col]
            self.board[from_row][from_col] = 0

            if self.board[row][col] == BLACK_PIECE and row == self.n_squares - 1:
                self.board[row][col] = BLACK_KING
            elif self.board[row][col] == RED_PIECE and row == 0:
                self.board[row][col] = RED_KING

            if abs(row - from_row) == 2:
                cap_row = from_row + (row - from_row) // 2
                cap_col = from_col + (col - from_col) // 2
                self.board[cap_row][cap_col] = 0

                self.move_count = 0
                self.selected_piece = (row, col)
                self.available_moves = self.get_available_moves(row, col)
                self.capture_moves = self.has_capture_moves(row)

                if self.capture_moves:
                    self.available_moves = self.capture_moves
                else:
                    self.change_turn()
            else:
                self.change_turn()
        else:
            self.selected_piece = None

    def has_capture_moves(self, row):
        return [move for move in self.available_moves if abs(move[0] - row) == 2]

    def change_turn(self):
        self.turn = RED_PIECE if self.turn == BLACK_PIECE else BLACK_PIECE
        self.selected_piece = None
        self.available_moves = []
        self.move_count += 1
        if self.move_count >= 100:
            self.winner = "draw"
        if self.check_winner():
            self.winner = BLACK_PIECE if self.turn == RED_PIECE else RED_PIECE

    def check_winner(self):
        red_moves, black_moves = [], []
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                piece = self.board[row][col]
                if piece in [RED_PIECE, RED_KING]:
                    red_moves.extend(self.get_available_moves(row, col))
                elif piece in [BLACK_PIECE, BLACK_KING]:
                    black_moves.extend(self.get_available_moves(row, col))
        if self.turn == RED_PIECE and not red_moves:
            return True
        if self.turn == BLACK_PIECE and not black_moves:
            return True
        return not any(p in [BLACK_PIECE, BLACK_KING] for row in self.board for p in row) or not any(p in [RED_PIECE, RED_KING] for row in self.board for p in row)

    def evaluate_board(self):
        score = 0
        for row in self.board:
            for piece in row:
                if piece == BLACK_PIECE:
                    score += 1
                elif piece == RED_PIECE:
                    score -= 1
                elif piece == BLACK_KING:
                    score += 1.5
                elif piece == RED_KING:
                    score -= 1.5
        return score

    def get_all_moves(self, color):
        moves = []
        for row in range(self.n_squares):
            for col in range(self.n_squares):
                piece = self.board[row][col]
                if piece != 0 and (piece == color or piece == color + 2):
                    for move in self.get_available_moves(row, col):
                        moves.append(((row, col), move))
        return moves

    def apply_move(self, move):
        (from_row, from_col), (to_row, to_col) = move
        self.selected_piece = (from_row, from_col)
        self.available_moves = self.get_available_moves(from_row, from_col)
        self.move(to_row, to_col)

    def minimax(self, depth, maximizing, alpha=float('-inf'), beta=float('inf')):
        if depth == 0 or self.winner:
            return self.evaluate_board(), None

        best_move = None
        if maximizing:
            max_eval = float('-inf')
            for move in self.get_all_moves(BLACK_PIECE):
                copy_game = self.copy_game_state()
                copy_game.apply_move(move)
                eval, _ = copy_game.minimax(depth - 1, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in self.get_all_moves(RED_PIECE):
                copy_game = self.copy_game_state()
                copy_game.apply_move(move)
                eval, _ = copy_game.minimax(depth - 1, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move


    def play_ai_move(self, depth= 8):
        eval, best_move = self.minimax(depth, True)
        if best_move:
            (from_row, from_col), (to_row, to_col) = best_move
            self.selected_piece = (from_row, from_col)
            self.available_moves = self.get_available_moves(from_row, from_col)
            self.move(to_row, to_col)

    def run(self):
        run = True
        last_player_move_time = None

        while run:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.select(y // self.square_size, x // self.square_size)

            if self.turn == BLACK_PIECE and not self.winner:
                if last_player_move_time is None:
                    last_player_move_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - last_player_move_time > 500:
                    self.play_ai_move(depth=4)
                    last_player_move_time = None
            else:
                last_player_move_time = None

            pygame.display.update()