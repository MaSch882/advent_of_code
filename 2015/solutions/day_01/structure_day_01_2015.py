class FloorCalculator:

    @staticmethod
    def calculate_floor(instruction: str):
        floor = 0
        for command in instruction:
            if command == '(':
                floor += 1
            if command == ')':
                floor -= 1
        return floor

    @staticmethod
    def calculate_first_basement_floor(instruction: str):
        floor = 0
        for index, command in enumerate(instruction):
            if command == '(':
                floor += 1
            if command == ')':
                floor -= 1
            if floor < 0:
                return index + 1
        return -1
