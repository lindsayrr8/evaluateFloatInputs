
# This program reads a set of floating-point values and
# asks the user to enter random values then calculates the
# average, smallest, largest, and difference between the values
# then displays the results.


numList = []
num = 0
length = 0
total = 0
minNum = 0
maxNum = 0
average = 0
diff = 0


print("This program accepts a set of numbers and calculates the average, ")
print("smallest term, largest term, and difference between the set of numbers. ")
print(" ")

# Prompt user to input numbers as float values.
num = (input("Input a number or enter 9999 to finish: "))
num = float(num)

# Set sentinal value to exit.
if num == 9999:
   print("You entered 9999. Program terminated. ")
   print(" ")
   
else:
    
# Open loop for user to input numbers indefinitely.
   while num != 9999:
      numList.append(num)
      num = (input("Input another number or enter 9999 to finish: "))
      num = float(num) 

# Get the length (total of inputs) for user-inputted list of nums using len function:
   length = len(numList)
   
# Get total to calculate the average:
   total = sum(numList)
   average = float(total/length)
   
# Round average output to 2 decimal places:
   average = round(average, 2)
   
# Get largest num, smallest num, find difference between them:
   minNum = min(numList)
   maxNum = max(numList)
   diff = maxNum - minNum

# Print results to user.
   print(" ")
   print("The average of the numbers is: ", average)
   print("The smallest number in the set is: ", minNum)
   print("The largest number in the set is: ", maxNum)
   print("The difference of the smallest and largest values is ", diff)


