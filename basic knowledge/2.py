"""КЛАССЫ. ИЗ КНИГИ"""


class Chair:
    """A chair on a chairlift"""
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

