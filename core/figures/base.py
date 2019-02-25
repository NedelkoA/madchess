from abc import ABCMeta, abstractmethod


INIT_COLS = {
    'PawnFigure': range(8),
    'KnightFigure': [1, 6],
    'BishopFigure': [2, 5],
    'RookFigure': [0, 7],
    'QueenFigure': [3],
    'KingFigure': [4]
}


class BaseFigure(metaclass=ABCMeta):
    reverse_operation = (-1, 1)

    def __init__(self, position, color):
        self.color = color
        self.position = position
        self.row, self.col = position

    @abstractmethod
    def generate_move(self):
        """
        Generator of available moves.
        """
        pass

    @classmethod
    def create_figures(cls, color):
        """
        Create instances of figures.
        Positions depend on color of figure.
        """
        row = cls._get_init_row(cls, color)
        for col in INIT_COLS[cls.__name__]:
            yield cls(
                (row, col),
                color
            )

    @staticmethod
    def _get_init_row(cls, color):
        """
        Return row position depend on figure.
        """
        if 'Pawn' in cls.__name__:
            return 1 if color == 'white' else 6
        return 0 if color == 'white' else 7

    @property
    def available_moves(self):
        """
        Return list of available moves.
        """
        moves = [
            move
            for move in self.generate_move()
        ]
        return self.filter_moves(moves)

    def can_move(self, target_position):
        """
        Check if list of available moves has target position.
        """
        return target_position in self.available_moves

    def filter_moves(self, list_moves):
        """
        Filtering move list so as not to go beyond the field.
        """
        return [
            move
            for move in list_moves
            if 7 >= move[0] >= 0 and 7 >= move[1] >= 0
        ]
