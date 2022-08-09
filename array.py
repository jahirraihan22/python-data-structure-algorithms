print("_____________________________ Problem 01 _____________________________")
expenses = [2200,2350,2600,2130,2190]

# print(expense)

# 1. In Feb, how many dollars you spent extra compare to January?
# print("February expense, "+str(expense[1] - expense[0])) 
print("1. Extra February expense ", expenses[1] - expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
expense = 0
for month in range(3):
    expense += expenses[month]

print("2. Total expense in first quarter ", expense)

# 3. Find out if you spent exactly 2000 dollars in any month
if 2000 in expenses:
    print("3. Spent exactly 2000 dollars in a month")
else:
    print("3. Didn\'t spend exactly 2000 dollars in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("4. After June my expenses ",expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses[3] = expenses[3] - 200

print("5. After getting refund on April 200$ ",expenses)

print("_____________________________ Problem 02 _________________________________")

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print("Length of the list is ", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print("2. Added 'black panther' at the end of this list ",heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther') # insert will not replace elements, it will shift the element and place it in destination
print("3. 'black panther' after 'hulk' ",heros)

"""
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
"""

heros[1:3] = ['doctor strange']
print("4. remove thor and hulk from list and replace them with doctor strange ",heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("5. Sort the heros list in alphabetical order ",heros)

print("_____________________________ Problem 03 _________________________________")

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_number = int(input("Enter Max Number: "))

odd_array = []
for number in range(max_number):
    if number % 2 != 0:
        odd_array.append(number)

print("Odd Numbers ",odd_array)