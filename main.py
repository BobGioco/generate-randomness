from src.data_collection import collect_data, process_data
from src.triad_update import triad_update, triads_dct_update
from src.helpers import balance_budget, check_binary_string

if __name__ == "__main__":
    final_string = collect_data()
    triads_dct = process_data(final_string)

    print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
    print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

    balance = 1000

    while True:
        print("\nPrint a random string containing 0 or 1:\n")
        guess_numbers = input()

        if guess_numbers.lower() == 'enough':
            break
        elif len(guess_numbers) < 4 or check_binary_string(guess_numbers) is False:
            continue

        right_guess = 0
        prediction = ''
        temp_update_dct = dict()
        for i in range(3, len(guess_numbers)):
            triad = triads_dct[guess_numbers[i - 3:i]]
            predict = '1' if triad['zero'] < triad['one'] else '0'
            prediction += predict
            right_guess += predict == guess_numbers[i]
            temp_update_dct = triad_update(temp_update_dct, guess_numbers[i - 3:i], guess_numbers[i])

        print(f'predictions:\n{prediction}\n')

        accuracy = right_guess / (len(guess_numbers) - 3)
        balance -= balance_budget(right_guess, (len(guess_numbers) - 3))

        print(f"Computer guessed {right_guess} out of {len(guess_numbers) - 3} symbols right ({accuracy:.2%})")
        print(f"Your balance is now ${balance}")

        triads_dct = triads_dct_update(triads_dct, temp_update_dct)

    print('Game over!')
