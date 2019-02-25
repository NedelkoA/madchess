from core.figures.base import BaseFigure


class PawnFigure(BaseFigure):
    def generate_move(self):
        for reverse_number in self.reverse_operation:
            for shift in range(1, 3):
                yield (
                    self.row + shift * reverse_number,
                    self.col
                )
