
def filter(string, lenght_filter = 3):
    result = []

    for i in string:
        if len(i) <= lenght_filter:
            result.append(i)

    return result


string = ['111', '2222', '3', '44', 'aaa', 'bbbbbbb', 'c', 'ddddddd']
result = filter(string)

print(f'Original list:\n'
      f'{string}.\n\n'
      f'Filtered list:\n'
      f'{result}.')