class TLSChecker:
    ip_adress: str

    def __init__(self, ip: str):
        self.ip_adress = ip

    def supports_tls(self):
        pass

    def extract_non_hypernet_sequences(self):
        pass

    def extract_hypernet_sequences(self):
        pass

    def has_ABBA_in_non_hypernet_sequences(self):
        pass

    def has_ABBA_in_hypernet_sequences(self):
        pass
