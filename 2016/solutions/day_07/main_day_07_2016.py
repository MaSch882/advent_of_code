filename = r"..\..\input_data\input_day_07_2016.txt"


def main():
    test_string_1 = "ioxxoj[asdfgh]zxcvbn"
    test_string_2 = "abcd[bddb]xyyx"
    test_string_3 = "aaaa[qwer]tyui"

    # Hypernet Sequences aufloesen
    reframed = test_string_3.replace("]", "[")
    splitted = reframed.split("[")

    # Nur nicht HS betrachten
    non_hypernet_sequences = []
    hypernet_sequences = []
    for i, x in enumerate(splitted):
        if i % 2 == 0:
            non_hypernet_sequences.append(x)
        if i % 2 == 1:
            hypernet_sequences.append(x)

    # Auf ABBA testen
    has_abba_in_non_hypertext_sequence = False
    has_abba_in_hypertext_sequence = False

    for sequence in non_hypernet_sequences:
        for i, char in enumerate(sequence):
            try:
                first = char
                second = sequence[i + 1]
                third = sequence[i + 2]
                fourth = sequence[i + 3]

                if first == fourth and second == third:
                    has_abba_in_non_hypertext_sequence = True

            except IndexError:
                break

    for sequence in hypernet_sequences:
        for i, char in enumerate(sequence):
            try:
                first = char
                second = sequence[i + 1]
                third = sequence[i + 2]
                fourth = sequence[i + 3]

                if first == fourth and second == third:
                    has_abba_in_hypertext_sequence = True

            except IndexError:
                break

    supports_tls = has_abba_in_non_hypertext_sequence and not has_abba_in_hypertext_sequence

    print(supports_tls)


if __name__ == "__main__":
    main()
