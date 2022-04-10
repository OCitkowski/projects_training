# return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this

def likes(names: list) -> str:
    text = ''
    if not len(names):
        text = "no one likes this"
    elif len(names) == 1:
        text = f'{names[0]} likes this'
    elif len(names) == 2:
        text = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        text = f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 2:
        text = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    else:
        text = f"don't worry"

    print(text)
    return text

# def likes(names: list) -> str:
#     text = []
#     text[0]= "no one likes this"
#     text[1] = f'{names[0]} likes this'
#     text[2] = f'{names[0]} and {names[1]} like this'
#     text[3] = f'{names[0]}, {names[1]} and {names[2]} like this'
#     text[4] = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
#
#     print(text)
#     return f'{text[len(names)]}'

if __name__ == '__main__':

    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'



