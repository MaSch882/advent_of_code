from abc import abstractmethod, ABC

A = 10
B = 11
C = 12
D = 13


class Keypad(ABC):
    def process_one_keystroke(self, direction: str, current_button: int) -> int:
        if direction == "U":
            return self.process_up(current_button)
        if direction == "R":
            return self.process_right(current_button)
        if direction == "D":
            return self.process_down(current_button)
        if direction == "L":
            return self.process_left(current_button)

    @staticmethod
    @abstractmethod
    def process_up(current_button: int) -> int:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def process_right(current_button: int) -> int:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def process_down(current_button: int) -> int:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def process_left(current_button: int) -> int:
        raise NotImplementedError()


class SimpleKeypad(Keypad):

    @staticmethod
    def process_up(current_button: int) -> int:
        if current_button in [1, 2, 3]:
            return current_button
        else:
            return current_button - 3

    @staticmethod
    def process_right(current_button: int) -> int:
        if current_button in [3, 6, 9]:
            return current_button
        else:
            return current_button + 1

    @staticmethod
    def process_down(current_button: int) -> int:
        if current_button in [7, 8, 9]:
            return current_button
        else:
            return current_button + 3

    @staticmethod
    def process_left(current_button: int) -> int:
        if current_button in [1, 4, 7]:
            return current_button
        else:
            return current_button - 1


class ComplexKeypad(Keypad):

    @staticmethod
    def process_up(current_button: int) -> int:
        if current_button in [5, 2, 1, 4, 9]:
            return current_button
        if current_button in [D, 3]:
            return current_button - 2
        else:
            return current_button - 4

    @staticmethod
    def process_right(current_button: int) -> int:
        if current_button in [1, 4, 9, C, D]:
            return current_button
        else:
            return current_button + 1

    @staticmethod
    def process_down(current_button: int) -> int:
        if current_button in [5, A, D, C, 9]:
            return current_button
        if current_button in [1, B]:
            return current_button + 2
        else:
            return current_button + 4

    @staticmethod
    def process_left(current_button: int) -> int:
        if current_button in [1, 2, 5, A, D]:
            return current_button
        else:
            return current_button - 1


class KeypadDecrypter:
    current_button: int
    passcode: list[int]
    keypad: Keypad

    def __init__(self, keypad: Keypad):
        self.current_button = 5
        self.passcode = []
        self.keypad = keypad

    def decrypt_set_of_commands(self, set_of_commands: list[str]):
        for command_string in set_of_commands:
            self.decrypt_command_string(command_string)

    def decrypt_command_string(self, command_string: str):
        for direction in command_string:
            self.decrypt_one_command(direction)
        self.passcode.append(self.current_button)

    def decrypt_one_command(self, direction: str):
        keypad = self.keypad
        next_button = keypad.process_one_keystroke(direction, self.current_button)
        self.current_button = next_button

    def build_passcode(self) -> str:
        passcode: str = ""
        for key in self.passcode:
            if key not in [A, B, C, D]:
                passcode += str(key)
            if key == A:
                passcode += "A"
            if key == B:
                passcode += "B"
            if key == C:
                passcode += "C"
            if key == D:
                passcode += "D"
        return passcode
