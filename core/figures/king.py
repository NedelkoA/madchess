from core.figures.base import BaseFigure


class KingFigure(BaseFigure):
    def generate_move(self):
        for reverse_number in self.reverse_operation:
            yield (
                self.row,
                self.col + 1 * reverse_number
            )
            yield (
                self.row - 1 * reverse_number,
                self.col
            )
            for reverse_number_1 in self.reverse_operation:
                yield (
                    self.row - 1 * reverse_number,
                    self.col - 1 * reverse_number_1
                )
