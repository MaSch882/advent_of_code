from structure_day_04_2016 import Room

filename = r"..\..\input_data\input_day_04_2016.txt"

testdata = ["aaaaa-bbb-z-y-x-123[abxyz]", "a-b-c-d-e-f-g-h-987[abcde]", "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"]


def main():
    print_solution_part_1()  #
    print_solution_part_2()  #


def print_room_data(room: Room):
    name = room.encrypted_name
    id = room.sector_id
    checksum = room.checksum
    print(f"Name: {name}; ID: {id}; Checksum: {checksum}.")


def print_solution_part_1():
    pass


def print_solution_part_2():
    pass


if __name__ == "__main__":
    main()
