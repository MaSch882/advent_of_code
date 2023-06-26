class Room:
    encrypted_name: str = ""
    sector_id: str = ""
    checksum: str = ""

    def __init__(self, full_name: str):
        separated_parts_of_full_room_name = full_name.split("-")
        combined_id_and_checksum = separated_parts_of_full_room_name.pop()

        self.extract_encrypted_name(separated_parts_of_full_room_name)
        self.extract_sector_id(combined_id_and_checksum)
        self.extract_checksum(combined_id_and_checksum)

    def extract_encrypted_name(self, splitted_name: list[str]):
        for element in splitted_name:
            self.encrypted_name += str(element)

    def extract_sector_id(self, combined_id_and_checksum: str):
        for char in combined_id_and_checksum:
            if char != "[":
                self.sector_id += str(char)
                combined_id_and_checksum = combined_id_and_checksum[1:]
            else:
                break

    def extract_checksum(self, combined_id_and_checksum: str):
        # Alles bis zur '[' abschneiden
        for char in combined_id_and_checksum:
            if char != "[":
                combined_id_and_checksum = combined_id_and_checksum[1:]
            else:
                break

        # Alles in den Klammern an die Checksum antackern
        for char in combined_id_and_checksum:
            if char == "[":
                combined_id_and_checksum = combined_id_and_checksum[1:]
            elif char != "]":
                self.checksum += str(char)
                combined_id_and_checksum = combined_id_and_checksum[1:]
            else:
                break


class RoomTester:
    room_to_test: Room
    symbol_counter: dict[str, int] = {}

    def __init__(self, room: Room):
        self.room_to_test = room
        self.initialize_symbol_counter(room)
        self.sort_symbols()

    def initialize_symbol_counter(self, room):
        encrypted_name = room.encrypted_name

        for char in encrypted_name:
            if char in self.symbol_counter:
                self.symbol_counter[char] += 1
            else:
                self.symbol_counter[char] = 1

    def sort_symbols(self):
        symbols = self.symbol_counter
        sorted_symbols = {key: value for key, value in
                          sorted(symbols.items(), key=lambda symbol: symbol[1], reverse=True)}
        self.symbol_counter = sorted_symbols
