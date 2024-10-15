class Game:
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    current_turn = 1

    def get_choice_from_user(self):
        while True:
            try:
                user_input = int(input("Enter a position on board between 0-8: "))
            except ValueError:
                print("You can only enter numbers not strings!")
                continue

            if user_input in range(9):
                break
            else:
                print("Ridi! just numbers between 1-9!")
                continue

        return user_input

    def add_choice(self, choice):
        if self.board[choice] != 0:
            print("Error! Position already in use")
            return

        self.board[choice] = self.current_turn
        self.current_turn = 1 if self.current_turn == 2 else 2

    def display_board(self):
        print("==============================")
        for rows in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            output_row = ""
            for row in rows:
                output_row += " " + str(self.board[row])
            print(output_row)
        print("==============================")

    def is_finished(self):
        win_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]

        # check if any empty position is exist
        is_zero_exist = False
        for value in self.board:
            if value == 0:
                is_zero_exist = True
                break

        if not is_zero_exist:
            print("idontknow")
            return True

        # check horizontal wins
        for position in win_positions:
            p1 = self.board[position[0]]
            p2 = self.board[position[1]]
            p3 = self.board[position[2]]

            if p1 == p2 == p3 and p1 != 0:
                print("hz", p1, p2, p3)
                return True

        # check vertical wins
        for inner_index in range(3):
            values = []
            for outter_index in range(len(win_positions)):
                values.append(self.board[win_positions[outter_index][inner_index]])

            if values[0] == values[1] == values[2] and values[0] != 0:
                print("vert", values[0], values[1], values[2])
                return True

        # check cross l-t-r
        values = []
        for i, position in enumerate(win_positions):
            values.append(self.board[position[i]])

        if values[0] == values[1] == values[2] and values[0] != 0:
            print("crr ltr", values[0], values[1], values[2])
            return True

        # check cross r-t-l
        values = []
        for i, position in enumerate(win_positions):
            overriden_index = i
            if i == 0:
                overriden_index = 2
            elif i == 2:
                overriden_index = 0

            values.append(self.board[position[overriden_index]])

        if values[0] == values[1] == values[2] and values[0] != 0:
            print("cross rtl", values[0], values[1], values[2])
            return True

        return False

    def get_winner(self) -> str:
        return "Player One" if self.current_turn == 2 else "Player Two"


game = Game()

while True:
    choice = game.get_choice_from_user()

    game.add_choice(choice)

    game.display_board()

    if game.is_finished():
        print(f"Game ended! {game.get_winner()} is winner!!")
        break
