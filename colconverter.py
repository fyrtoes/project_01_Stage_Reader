# GCAV Information
# 1/22/2015 FINISHED on 1/25/2015
# The purpose of this program is to convert the column index from Meyer's into a number. A = 1, B = 2, etc.

'''
print "\n"

# Here is where I will ask the user to provide the column, from where I will store it.
column = raw_input('Enter the column index (a, b, ac, etc.):')

# I will print back what the user selected
print 'Hello, the column you entered is: ', column, "\n"
'''

# In function form
def columnconverter(column):

	#Here I take the size of the column entered for good coding.
	length = len(column)

	#Here I have the map that I will be working off of. a = 0 due to the array organization.
	map = 'abcdefghijklmnopqrstuvwxyz'
	map2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	## variables for 1st for-loop
	# initialize 'i' and 'j' just in case. 
	i = 0 # Index of column[i]. Goes through each letter in the column
	j = 0 # Compares column[i] to each letter to all alphabet
	flag_success = False
	j_var = []

	## variables for 2nd for-loop
	i2 = 0  		# needed for the second for-loop iteration counter
	j2 = 0			# maybe wont need it
	sum = 0 		# Final sum of the index
	b = len(map)	# how many elements does 'map' contain? 26
	n = len(column) # how many elements does 'column' contain? User-dependent

	############## 1st for-loop ############
	# This version of the for loop will convert each letter in the of the 'column' variable into an number in an array.
	# i is the iteration
	# len(map) is the size of the character array above called "map"
	# range(len(map)) crates an array out of the integer value that is "len(map)"
	#       This will permit the for-loop to operate, since it requires an array of numbers
	#########################################
	for i in range(len(column)): # run the for-loop as many times as there are characters in the 'column' variable
		while ((j < len(map)) and (flag_success == False)): # run while-loop as many times as there are characters in our 'map' no need for more,
															#.....because there are no more letters in the alphabet.
															# The other condition is our exit flag. We exit when we succeed. Must reset in the for-loop.
			if (map[j] == column[i]):		# If these do match.
				j_var.append( j + 1 )		# Include the numerical value (1-26) in the array called j_var
				flag_success = True			# trigger flag to exit while-loop, or else we are stuck succeeding forever
			elif (map2[j] == column[i]):	# If these do match.
				j_var.append( j + 1 )		# Include the numerical value (1-26) in the array called j_var
				flag_success = True			# trigger flag to exit while-loop, or else we are stuck succeeding forever
			else:
				j = j + 1					# counter to accomplish two things: 1) increase the index, comparing the next letter in 'map'
											# 2) Counter to exit a perpetually failing while-loop
		if (j >= len(map) ):							# if statement in case goober enters a non-alphabetical symbol
			print "***********", column[i], "is not a letter ***********"	# error message to goober
		j = 0											# must restart j for the re-enabling of the next while-loop
		flag_success = False							# must reset for the re-enabling of the next while-loop


	############## 2nd for-loop ############
	# This loop will take j_var array and use each as the coefficient of the base conversion polynomial:
	# SIGMASUM (n, itersum = 0), L(_itersum) * (b**(n-itersum)),
	# where L is the j_var index for that particular itersum iteration, b and n can be found on lines 29-30
	########################################
	for i2 in range(len(j_var)):
		sum = sum + ( j_var[i2] * ( b ** ( n - i2 - 1 ) ) )
	return sum
print columnconverter(column)