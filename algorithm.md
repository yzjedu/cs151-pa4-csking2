# Algorithm 

1. import os

2. Function 1: read_file_name 
* Purpose: Processes user's input and output's if user's input is invalid
* Name: read_file_name
* Parameters: none
* Return: f_name
* Algorithm:
    1. ask user to input the file name, store under f_name
    2. while not os.path.isfile(f_name)
        1. tell the user the file doesn't exist, prompt to enter again
    3. return f_name

3. Function 2: particular_word
* Purpose: Checks if word is in line, counts the line and then goes to another, outputs number of headlines
* Name: particular_word
* Parameters: file_name
* Return: none
* Algorithm:
    1. try
       1. ask user to enter the word, store under word
       2. word.lower().strip()
       3. set count to 0
       4. with open(file_name, 'r') as file
          1. for line in file
             1. count += 1
       5. output the count of the word in the headline
    2. except
        1. output error

4. Function 3: write_headlines
* Purpose: Checks if word is in line, writes that line in a new file, continues to other lines
* Name: write_headlines
* Parameters: file_name, output_file
* Return: none
* Algorithm:
    1. try
        1. ask user to input word, store under word
        2. word.lower().strip()
        3. with open(file_name, 'r) as file
            1. with open(output_file, 'w') as new_file
                1. for line in file
                    1. if word in line.lower:
                        1. new_file.write(line)
    2. except
        1. output error

5. Function 4: average
* Purpose: Finds the average number of characters in each headline
* Name: average
* Parameters: file_name
* Return: None
* Algorithm
    1. initialize sum and count to 0
    2. try
       1. with open(file_name, 'r') as file
            1. for line in file
                1. sum += len(lin.strip())
                2. count += 1
            2. average = sum / count
            3. output the average length
    3. except
        1. output error

6. Function 5: longest_shortest
* Purpose: Finds the shortest and longest headline in each file
* Name: longest_shortest
* Parameters: file_name
* Return: None
* Algorithm
    1. initialize all the variables, longest '', shortest None, length of longest 0, length of shortest 9999999
    2. try
        1. with open(file_name, 'r') as file
            1. for line in file
               1. length = len(line.strip())
               2. if length > length_of_longest
                    1. longest = line.strip()
                    2. length_of_longest = length
        2. output the longest headline
        3. with open(file_name, 'r') as file
            1. for line in file
                1. length = len(line.strip())
                2. if length < length of shortest
                    1. shortest = line.strip()
                    2. length_of_shortest = length
        4. output the shortest headline
    3. except
        1. output error

7. Function 6: read_in_new_file
* Purpose: Overwrites a file the user chooses
* Name: read_in_new_file
* Parameters: file_name
* Return: None
* Algorithm
    1. with open(file_name, 'w') as file
        1. file.write('file has been overwrite')

8. Function 7: menu
* Purpose: display menu to the user
* Name: menu
* Parameters: none
* Return: none
* Algorithm
    1. output Select an option below (Enter a number 1-6):
    2. output Count how many headlines have a specific word
    3. output Write headlines with a specific word into a new file
    4. output Average number of characters in headlines
    5. output Longest and shortest headlines
    6. output Read in a new file to analyze
    7. output Exit

9. Function 8: main
* Purpose: main function
* Name: main
* Parameters: file_name
* Return: none
* Algorithm
    1. output the purpose of the program
    2. initialize choice to 0
    3. while choice != 6
        1. output the '~'
        2. call read_file_name()
        3. call menu()
        4. ask user to enter their choice
        5. if choice == 1
            1. call particular_word()
        6. otherwise if choice == 2
            1. ask user what they want their output file to be named
            2. call write_headlines()
        7. otherwise if choice == 3
            1. call average()
        8. otherwise if choice == 4
            1. call longest_shortest
        9. otherwise if choice == 5
            1. call read_in_new_file()
        10. otherwise if choice == 6
            1. output program exited
    4. output the program has finished

10. call main()

