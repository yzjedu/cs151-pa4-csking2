import os

def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name


def particular_word(file_name):
    try:
        word = input("Enter a word: ")
        word = word.lower().strip()
        count = 0
        with open(file_name, 'r') as file:
            for line in file:
                if word in line:
                    count += 1
        print(f'{word} is in {count} of the headlines.')
    except FileNotFoundError:
        print(f'Error')


def write_headlines(file_name, output_file_name):
    try:
        word = input("Enter a word: ")
        word = word.lower().strip()
        with open(file_name, 'r') as file:
            with open(output_file_name, 'w') as new_file:
                for line in file:
                    if word in line.lower():
                        new_file.write(line)

    except FileNotFoundError:
        print(f'Error:')


def average(file_name):
    sum = 0
    count = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sum += len(line.strip())
                count += 1
            average = sum / count
            print(f'The average length of each headline in {file_name} is {average}')
    except FileNotFoundError:
        print(f'Error:')

def longest_shortest(file_name):
    longest = ''
    shortest = None
    length_of_longest = 0
    length_of_shortest = 9999999
    try:
        with open(file_name, 'r') as file:
            for line in file:
                length = len(line.strip())
                if length > length_of_longest:
                    longest = line.strip()
                    length_of_longest = length
        print(f'The longest headline is {longest}')

        with open(file_name, 'r') as file:
            for line in file:
                length = len(line.strip())
                if length < length_of_shortest:
                    shortest = line.strip()
                    length_of_shortest = length
        print(f'The shortest headline is {shortest}')

    except FileNotFoundError:
        print(f'Error:')

def read_in_new_file(file_name):
    with open(file_name, 'w') as file:
        file.write('file has been overwrite')


def main(file_name):

    print(f"\nSelect an option below (Enter a number 1-6):")
    print(f"1. Count how many headlines have a specific word")
    print(f"2. Write headlines with a specific word into a new file")
    print(f"3. Average number of characters in headlines")
    print(f"4. Longest and shortest headlines")
    print(f"5. Read in a new file to analyze")
    print(f"6. Exit")
    choice = int(input("Enter your option: "))

    while choice >= 1 and choice <= 5:
        if choice == 1:
            particular_word(file_name)
        elif choice == 2:
            output_file_name = input(f"What do you want your output file name: ")
            write_headlines(file_name, output_file_name)
        elif choice == 3:
            average(file_name)
        elif choice == 4:
            longest_shortest(file_name)
        elif choice == 5:
            read_in_new_file(file_name)
        elif choice == 6:
            print('program exited')
        else:
            print("Invalid option")

    print('program finished')






main(read_file_name())


