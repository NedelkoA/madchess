from itertools import permutations

from core.figures.base import BaseFigure


class KnightFigure(BaseFigure):
    def generate_move(self):
        for reverse_number in self.reverse_operation:
            for combination in permutations((1, 2), 2):
                for reverse_number_1 in self.reverse_operation:
                    yield (
                        self.row + combination[0] * reverse_number_1,
                        self.col + combination[1] * reverse_number
                    )
