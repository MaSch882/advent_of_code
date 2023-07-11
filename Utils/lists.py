class ListUtils:

    @staticmethod
    def delete_first(list_to_process: list) -> None:
        list_to_process.pop(0)

    @staticmethod
    def get_and_delete_first(list_to_process: list):
        return list_to_process.pop(0)

    @staticmethod
    def get_first(list_to_process: list):
        return list_to_process[0]
