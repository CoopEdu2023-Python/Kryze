class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                move = int(input(f"Player {self.symbol}, enter your move (1-9): "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")


class Game:
    def __init__(self, num_players=10):
        self.board = [" " for _ in range(9)]
        self.players = [Player(str(i)) for i in range(1, num_players + 1)]

    def print_board(self):
        print("-------------")
        for i in range(0, 9, 3):
            print(f"| {self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]} |")
            print("-------------")

    def check_winner(self, symbol):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combination in winning_combinations:
            if all(self.board[i] == symbol for i in combination):
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def play(self):
        current_player = 0
        while True:
            self.print_board()
            move = self.players[current_player].get_move() - 1
            if self.board[move] == " ":
                self.board[move] = self.players[current_player].symbol
                if self.check_winner(self.players[current_player].symbol):
                    self.print_board()
                    print(f"Player {self.players[current_player].symbol} wins! Congratulations!")
                    break
                elif self.is_draw():
                    self.print_board()
                    print("It's a draw! No one wins.")
                    break
                else:
                    current_player = (current_player + 1) % len(self.players)
            else:
                print("Invalid move. That position is already taken. Please try again.")


if __name__ == "__main__":
    num_players = 10
    game = Game(num_players)
    game.play()