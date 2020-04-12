class Sudoku:
    def __init__(self):
        self.puzzle = []
        self.create_or_reset()

    def create_or_reset(self):
        self.puzzle = []
        for _ in range(9):
            self.puzzle.append([0]*9)

    def create_or_reset(self):
        pass


if __name__ == "__main__":
    s = Sudoku()
    print(s.puzzle)
    assert len(s.puzzle) == 9
    assert len(s.puzzle[0]) == 9
