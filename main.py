# Programmers:  [Cody]
# Course:  CS151, [Professor Zee]
# Due Date: [11/21/2024]
# Lab Assignment:  [PA 4]
# Problem Statement:  [Program allows user to interact with different files]
# Data In: [the file they want to read from, words they want to search]
# Data Out:  [number of headlines with word, new file user creates, average characters in each headline, longest and shortest headline]
# Credits: [class notes and class program, to assigned shortest with None I used the internet because I couldn't figure out how else to make it usable]
# Input Files: [the files with all the headlines on them]
import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    f_name = input("Enter file name: ")
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

# Name: particular_word
# Parameters: None
# Return: None
# Checks if word is in line, counts the line and then goes to another, outputs number of headlines has that word
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

# Name: write_headlines
# Parameters: file_name, output_file
# Return: None
# Checks if word is in line, writes that line in a new file, continues to other lines
def write_headlines(file_name, output_file):
    try:
        word = input("Enter a word: ")
        word = word.lower().strip()
        with open(file_name, 'r') as file:
            with open(output_file, 'w') as new_file:
                for line in file:
                    if word in line.lower():
                        new_file.write(line)

    except FileNotFoundError:
        print(f'Error:')

# Name: average
# Parameters: file_name
# Return: None
# Finds the average number of characters in each headline
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

# Name: longest_shortest
# Parameters: file_name
# Return: None
# Finds the shortest and longest headline in each file
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

# Name: read_in_new_file
# Parameters: None
# Return: None
# Overwrites a file the user chooses
def read_in_new_file(file_name):
    with open(file_name, 'w') as file:
        file.write('file has been overwrite')

# Name: menu
# Parameters: None
# Return: None
# Displays menu to the user
def menu():
    print(f"\nSelect an option below (Enter a number 1-6):")
    print(f"1. Count how many headlines have a specific word")
    print(f"2. Write headlines with a specific word into a new file")
    print(f"3. Average number of characters in headlines")
    print(f"4. Longest and shortest headlines")
    print(f"5. Read in a new file to analyze")
    print(f"6. Exit")

# Name: main
# Parameters: file_name
# Return: None
# main function
def main(file_name):
    print('This program allows you to work with different files that contains headlines')
    choice = 0
    while choice != 6:
        print('~' * 100)
        file_name = read_file_name()
        menu()
        choice = int(input("Enter your option: "))
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
            print('Program exited')
        else:
            print("Invalid option, please try again.")

    print('Program finished')

#Call the main function
main(read_file_name())


