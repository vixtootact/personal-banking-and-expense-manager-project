#Load data explanation

# 1 - we stored bank_data.txt in a variable called data_file
# 3 - i created a function called load data for the program
# 4 - i put a try statement for error handling
# 5 - i opened and read the file with open() and "r", and i stored the opened version in file
# 6 - i read all the lines in "file" and stored it in lines variable
# 7 - i closed the file
# 8 - i used lines[0] for the 1st item in lines list, and strip() to remove unwanted space
# 9 - assigned float data type to balance, lines[1] to print the 2nd item, and strip() to 
#     unwanted space
# 10 - an empty expenses array
# 11 - for loop to loop lines list, from the 3rd list until the last
# 12 - created a description, category, amount for the items in the list
# 13-16 - appended description, category, amount to the expenses array, typecasted amount to float
# 18 - returned name, balance, expenses
# 19 - error handling a missing file
# 20 - returned No values in the file when the error occurs
# 21 - it catches other errors that couldn't be caught other than missing file error
# 22 - prints error loading data together with the error
# 23 - it stores No value in the array

# Save data explanation
# 25 - a function called save data was made to handle saving new data to the bank_data.txt file, using name, balance and expenses
# 26 - try part of the try and except
# 27 - opened the file with file.open() and wrote to it with "w"
# 29-30 - writing and saving data to name and balance, the str() in line 30 is to convert the balance to a string and the \n is for a new line
# 32 - expense is an object so we have to use for loop 
# 33 - writing and saving to expense and its content inside the for loop
# 34-36 - writing and saving new info to description, category and amount, \n is to make a new line after amount
# 39 - to close the file after all the writing and saving is done
# 40 - print the output of the try
# 42 - the except part to print an error message incase things go "south"
# 43 - print the "Error saving data:", + the error message.

# Create account explanation
# 47 - a function to create an account is made
# 48 - outputs "Create Account"
# 49 - an input to ask users for their name
# 51 - while loop to continue running until the condition is false
# 52 - try part in try and except
# 53 - ask the user for balance with input() and convert to float (float())
# 55-57 - if balance is less than 0, print it cant be negative, then continue
# 59 - return name and balance
# 61 - except part in try and except, to check for invalid data types other than digits
# 62 - output please enter a valid amount.

# 71 - function for deposit
# 72 - try part in try and except
# 73 - input statement to enter amount to deposit in a float data type assigned to amount var
# 75 - checking if amount is less than/equal to 0
# 76 - outputs amount must be greater than 0
# 77-78 - returns balance and increments balance by the amount
# 79 - prints amount(with 2 decimal places) has been deposited successfully
# 81-82 - except part, prints "Invalid amount"
# 86 - a withdraw function
# 87 - try part in try and except
# 89 - user input for amount in float data type
# 91-92 - if amount is less than or equal to 0, print amount must be greater than 0
# 94-95 - if amount is greater than balance, print Insufficient balance
# 97-98 - else subtract the amount from the balance 
# 99 - print amount (in 2 decimal places) withdrawn successfully
# 101-102 - print Invalid amount when there valueError arises using except
# 103 - return balance after the try and except
