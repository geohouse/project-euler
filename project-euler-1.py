#! usr/bin/python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Set the upper limit of the number of numbers to search through
upperLimit = 1000
# Initialize a variable to hold the value for the cumulative sum
sum = 0

# loop through the natural numbers from 0 to the upperLimit - 1. 
# This keeps the numbers searched below the upperLimit, like the question requires.
for num in range(upperLimit):
	# Check if the number is a multiple of 3 or 5 (evenly divisible by 3 or 5), and 
	# if so, add the number to the cumulative sum.
	if num % 3 == 0 or num % 5 == 0:
		sum += num

# Output the cumulative sum. This is the answer.
print("The sum is: {}".format(sum))
