def to_nato(words: str) -> str:
    nato_dict = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf',
                 'H': 'Hotel',
                 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
                 'P': 'Papa',
                 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor',
                 'W': 'Whiskey',
                 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu', '.': '.', '?': '?', '!': '!', '.': '.', ' ': ''}

    # print(f"'{' '.join([nato_dict[words[i].upper()] for i in range(len(words)) if words[i].upper() != ' '])}'")
    return ' '.join([nato_dict[words[i].upper()] for i in range(len(words)) if words[i].upper() != ' '])


if __name__ == '__main__':
    # to_nato('words')
    # to_nato('.d?d!')
    assert to_nato('.d?d!') == '. Delta ? Delta !'

