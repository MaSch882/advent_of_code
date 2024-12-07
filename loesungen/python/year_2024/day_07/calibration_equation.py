from dataclasses import dataclass


@dataclass
class CalibrationEquation:
    target_value: int
    operands: list[int]

    def __init__(self, init_string: str):
        splits = init_string.split(":")
        self.target_value = int(splits[0].strip())

        operand_strings = splits[1].strip().split(" ")
        self.operands = [int(op) for op in operand_strings]

    def __eq__(self, other) -> bool:
        return self.target_value == other.target_value and self.operands == other.operands

    def is_solvable_using_addition_and_multiplication(self, operands: list[int]) -> bool:
        # error case
        if len(operands) < 2:
            raise RecursionError("List of operands became too short.")

        # basecase
        if len(operands) == 2:
            first = operands[0]
            second = operands[1]
            return first + second == self.target_value or first * second == self.target_value

        # recursion
        first = operands[0]
        second = operands[1]
        list_with_addition = [first + second]
        list_with_multiplication = [first * second]
        for i in range(2, len(operands)):
            list_with_addition.append(operands[i])
            list_with_multiplication.append(operands[i])

        return self.is_solvable_using_addition_and_multiplication(
            list_with_addition) or self.is_solvable_using_addition_and_multiplication(list_with_multiplication)

    def is_solvable_using_addition_multiplication_and_concatenation(self, operands: list[int]) -> bool:
        # error case
        if len(operands) < 2:
            raise RecursionError("List of operands became too short.")

        # basecase
        if len(operands) == 2:
            first = operands[0]
            second = operands[1]
            concatenation = int(str(first) + str(second))
            return first + second == self.target_value or first * second == self.target_value or concatenation == self.target_value

        # recursion
        first = operands[0]
        second = operands[1]
        list_with_addition = [first + second]
        list_with_multiplication = [first * second]
        list_with_concatenation = [int(str(first) + str(second))]
        for i in range(2, len(operands)):
            list_with_addition.append(operands[i])
            list_with_multiplication.append(operands[i])
            list_with_concatenation.append(operands[i])

        return self.is_solvable_using_addition_multiplication_and_concatenation(
            list_with_addition) or self.is_solvable_using_addition_multiplication_and_concatenation(
            list_with_multiplication) or self.is_solvable_using_addition_multiplication_and_concatenation(
            list_with_concatenation)
