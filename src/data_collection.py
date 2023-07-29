def collect_data():
    output = list()
    print("Please provide AI some data to learn...\nThe current data length is 0, 100 symbols left\n")

    while True:
        print("Print a random string containing 0 or 1:\n")
        numbers = input()
        for number in list(numbers):
            if number in ["0", "1"]:
                output.append(number)

        if len(output) >= 100:
            final_string = ''.join(output)
            print('\nFinal data string:\n', final_string, '\n')
            break
        else:
            print(f"Current data length is {len(output)}, {100 - len(output)} symbols left")

    return final_string


def process_data(final_string):
    final_sliced = [final_string[x:x + 4] for x in range(0, len(final_string) - 3)]
    triads = [str(bin(n))[2:].zfill(3) for n in range(0, 8)]
    triads_dct = {triad: {'zero': 0, 'one': 0} for triad in triads}

    for key, value in triads_dct.items():
        triads_dct[key]['zero'] += final_sliced.count(key + '0')
        triads_dct[key]['one'] += final_sliced.count(key + '1')

    return triads_dct
