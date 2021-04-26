# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
full_phrase = ' '.join(words)
print(full_phrase)

# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
words = ['Coding', 'For', 'All']
full_phrase = ' '.join(words)
print(full_phrase)

# 3 - Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(len(company))

# 6 - Change all the characters to capital letters using upper() method.
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.swapcase())
print(company.title())

# 9 - Cut(slice) out the first word of Coding For All string.
print(company[0])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))

# 11 Replace the word coding in the string 'Coding For All' to Python.
company = company.replace('Coding', 'Python')
print(company)

# 12 Change Python for Everyone to Python for All using the replace method or other methods.
company = company.replace('All', 'Everyone')
print(company)

# 13 Split the string 'Coding For All' using space as the separator (split()) .
company = company.split(' ')
print(company)

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(' ')
print(companies)

# 15 What is the character at index 0 in the string Coding For All.
company = ' '.join(company)
print(company[0])

# 16 What is the last index of the string Coding For All.
last_index = len(company) - 1
print(company[last_index])

# 17 What character is at index 8 in "Coding For All" string.
print(company[8])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
company_name_splited = 'Python For Everyone'.split(' ')
abbreviation = ''
for split_part in company_name_splited:
	abbreviation += split_part[0]
print(abbreviation)

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
company_name_splited = 'Coding For All'.split(' ')
abbreviation = ''
for split_part in company_name_splited:
	abbreviation += split_part[0]
print(abbreviation)

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
c_index = 'Coding For All'.index('C')
print(c_index)

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
f_index = 'Coding For All'.index('F')
print(f_index)

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
f_last_index = 'Coding For All People'.rfind('F')
print(f_last_index)

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because_index = 'You cannot end a sentence with because because because is a conjunction'.index('because')
print(because_index)

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because_last_index = 'You cannot end a sentence with because because because is a conjunction'.rindex('because')
print(because_last_index)

# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because_split = 'You cannot end a sentence with because because because is a conjunction'.split('because because because')
print(because_split)

# 28 Does ''Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))

# 29 Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('Coding'))

# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31 Which one of the following variables return True when we use the method isidentifier():
# a 30DaysOfPython
print('30DaysOfPython'.isidentifier())
# b thirty_days_of_python
print('thirty_days_of_python'.isidentifier())
# B

# 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33 Use the new line escape sequence to separate the following sentences
sentence = """
I am enjoying this challenge.
I just wonder what is next.
"""
print(sentence.strip().split('\n'))

# 34 Use a tab escape sequence to write the following lines
sentence = """
Name\tAge\tCountry
Asabeneh\t250\tFinland
"""
print(sentence)

# 35 Use the string formating method to display the following:
radius = 5674.32
pi = 3.14
area = pi * radius ** 2
print('The area of a cricle with radius {} is {:.2f} meters square.'.format(radius, area))

# 36 Make the following using string formating methods:
a = 8
b = 6
operators = ['+', '-', '*', '/', '%', '//', '**']
for operator in operators:
	result = eval(str(a) + operator + str(b))
	print('{} + {} = {}'.format(a, b, result))
