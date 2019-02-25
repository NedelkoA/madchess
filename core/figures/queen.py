from core.figures.base import BaseFigure


class QueenFigure(BaseFigure):
    def generate_move(self):
        for reverse_number in self.reverse_operation:
            for shift_number in range(1, 9):
                yield (
                    self.row,
                    self.col + shift_number * reverse_number
                )
                yield (
                    self.row - shift_number * reverse_number,
                    self.col
                )
                for reverse_number_1 in self.reverse_operation:
                    yield (
                        self.row - shift_number * reverse_number,
                        self.col - shift_number * reverse_number_1
                    )
