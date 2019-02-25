from core.figures.base import BaseFigure


class BishopFigure(BaseFigure):
    def generate_move(self):
        for external_number in self.reverse_operation:
            for shift_number in range(1, 9):
                for internal_number in self.reverse_operation:
                    yield (
                        self.row - shift_number * external_number,
                        self.col - shift_number * internal_number
                    )
