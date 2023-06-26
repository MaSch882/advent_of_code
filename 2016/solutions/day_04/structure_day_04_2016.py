class Room:
    full_name: str
    encrypted_name: str = ""
    sector_id: str = ""
    checksum: str = ""

    def __init__(self, full_name: str):
        self.full_name = full_name

        splitted = self.full_name.split("-")
        sector_id_and_checksum = splitted.pop()

        self.extract_encrypted_name(splitted)
        self.extract_sector_id(sector_id_and_checksum)
        self.extract_checksum(sector_id_and_checksum)

    def extract_encrypted_name(self, splitted_name: list[str]):
        for element in splitted_name:
            self.encrypted_name += str(element)

    def extract_sector_id(self, id_and_checksum: str):
        for char in id_and_checksum:
            if char != "[":
                self.sector_id += str(char)
                id_and_checksum = id_and_checksum[1:]
            else:
                break

    def extract_checksum(self, id_and_checksum: str):
        for char in id_and_checksum:
            if char != "[":
                id_and_checksum = id_and_checksum[1:]
            else:
                break

        for char in id_and_checksum:
            if char == "[":
                id_and_checksum = id_and_checksum[1:]
            elif char != "]":
                self.checksum += str(char)
                id_and_checksum = id_and_checksum[1:]
            else:
                break


class RoomTester:
    symbol_counter: dict[str, int]
