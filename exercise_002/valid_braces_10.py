def valid_braces(string: int) -> bool:
    result = True
    string = list(string)
    right, left = '({[', ')}]'
    counter_right, counter_left = 0, 0
    for i in range(len(string)):
        if i + 1 == len(string):
            break
        if string[i] in right:
            counter_right += 1
        elif string[i] in left:
            counter_left += 1

        if string[i] == right[0] and (string[i + 1] == left[1] or string[i + 1] == left[2]):
            result = False
            print(f'{string[i]} , {string[i + 1]} / {right[0]} /{left[1]} /{left[2]}')
            break
        print(f'{i} {result}')
        if string[i] == right[1] and (string[i + 1] == left[0] or string[i + 1] == left[2]):
            result = False
            print(f'{string[i]} , {string[i + 1]} / {right[1]} / {left[0]} / {left[2]}')
            break
        print(f'{i} {result}')
        if string[i] == right[2] and (string[i + 1] == left[1] or string[i + 1] == left[0]):
            print(f'{string[i]} , {string[i + 1]} / {right[2]} / {left[0]} / {left[1]}')
            result = False
            break
        print(f'{i} {result}')
        i += 1

    if counter_right != counter_left + 1:
        result = False

    return result

def validBraces_bestpr(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


if __name__ == '__main__':
    valid_braces("()")
    # assert valid_braces("(({{[[]]}}))") == True
    # assert valid_braces("(((({{") == False
    # assert valid_braces("[(])") == False
