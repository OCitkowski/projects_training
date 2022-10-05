def spin_words(sentence):
    full_str = sentence.split(" ")
    new_str = ''
    for i in full_str:

        if len(i) >= 5:
            word = i[::-1] + " "
        else:
            word = i + " "

        new_str += word

    return new_str.strip()

def spin_words_best_practics(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


if __name__ == '__main__':

    assert spin_words("Welcome to") == "emocleW to"
    # print(f'yyyy')
