# Filename: ?
# FILE WRITTEN: 1/20/2015 - 2/8/2015
# File Author: Gilberto Villela
#
# The purpose of this code is to read the .adt data from Meyers
# # and return the instantaneous data at each point we staged
# # such as time, pressure, clean rate, slurry rate, clean job, concentration


import csv # Importing the CSV module

# The purpose of this file is to read a text

# Ask user for filename
#filename = raw_input("Enter filename (.txt)")
# filename = 'Stage 8.txt'

# Ask the user for the clean bbls stage column
#clean_stg_bbls_column = int(raw_input("Enter column of clean stage bbls in the file above: ")
clean_stg_bbls_column = 75 # Set as a constant for testing purposes

# Ask the user for Wellhead A and Wellhead B pressure columns
#wellhead_A_column = int(raw_input("Enter column of Wellhead A pressure in the file above: ")
#wellhead_B_column = int(raw_input("Enter column of Wellhead B pressure in the file above: ")
wellhead_A_column = 109 # Set as constant for testing purposes
wellhead_B_column = 110 # Set as constant for testing purposes

# Ask the user for the slurry rate column
#slurry_rate_column = int(raw_input("Enter column of slurry rate in the file above: ")
slurry_rate_column = 81 # Set as a constant for testing purposes

# Ask the user for the clean bbls job total column
#clean_job_bbls_column = int(raw_input("Enter column of clean job bbls in the file above: ")
clean_job_bbls_column = 78 # Set as a constant for testing purposes

# Ask the user for the Auger PPA column
#Auger PPA_column = int(raw_input("Enter column of Auger PPA in the file above: ")
Auger_PPA_column = 90 # Set as a constant for testing purposes

# Open reading stream from file provided by user. Set to read only. 'r'
readstream = open('Stage 8.txt','r')
#print readstream

line_count = 0
previous_item = 0
total_steps = 0
steps_list = []										# Defining empty list for future use
individual_step = []
print "Time", "Wellhead A", "Slurry Rate", "Clean Job"
datareader = csv.reader(readstream, delimiter=";")		# Creates a list of a list the exterior list is of each line of data.
														# Each line of data is the second, interior list. They are string as a default
for row in datareader:									# For-loop that counts the 'row's of the exterior list as iterations
#	if (row[clean_stg_bbls_column] < previous_item):	# Will check if the current clean_stg_bbls counter entry is lower to the previous
	if (float(row[clean_stg_bbls_column]) < previous_item):				# Will check if the current clean_stg_bbls counter entry is lower than 1
		total_steps = total_steps + 1					# If it is lower, count the pass to totalize step count
		'''
		print row[0].rjust(8),
		print '%.0f' % float(row[wellhead_A_column].rjust(7)), 
		print '%.1f' % float(row[slurry_rate_column].rjust(4)),
		print '%.0f' % float(row[clean_job_bbls_column].rjust(6)),
		print '%.2f' % float(row[Auger_PPA_column].rjust(1))
		'''
		'''
		steps_list[line_count] = [row[0],
			float(row[wellhead_A_column]),
			float(row[slurry_rate_column]),
			float(row[clean_job_bbls_column]),
			float(row[Auger_PPA_column])]
		'''
		
		# About to try append on the following code. I am adding items to each inside list called 'individual_step'
		individual_step.append(row[0])
		individual_step.append(row[wellhead_A_column])
		individual_step.append(row[slurry_rate_column])
		individual_step.append(row[clean_job_bbls_column])
		individual_step.append(row[Auger_PPA_column])
		steps_list.append(individual_step)
		print total_steps, " - ", individual_step
		individual_step = []
	line_count = line_count + 1							# Counts the number of lines of data
	previous_item = float(row[clean_stg_bbls_column])	# Saves the previous clean stg bbls counter as the current one for the next test
#	print row[clean_stg_bbls_column]					# Print the clean_stg_bbls counter entry


#print type(float(row[clean_stg_bbls_column]))			# Debugging step
print "There are", line_count, "lines of data."
print "We staged", total_steps, "times."

# print steps_list                         # Displays the entire list of lists
	
# Start reading from the beginning of the file.
#readstream.seek(0)

# Read the 1st line of the file and the new line character '\n' and
#..... save it as 'read_line_p'
#read_line_p = readstream.readline()

#print len(read_line_p), "characters"	# Print the length of the 1st line string
#iter = 0
#count_semicolon = 0
#count_other = 0


# This for-loop is to count the number of semicolons in each line of code. This will help us locate the correct columnar value
#for iter in range(len(read_line_p)):
#	if (read_line_p[iter] == ';'):
#		count_semicolon = count_semicolon + 1

# Next I want to capture the string of relevance (clean stage)



########
# Next in line is be able to ENTER the column where the clean stage is, turn it into a number, n.
# My value is between the (n-1)th and nth column
# I check that value:
#.....if it's a non-zero, nothing happens. OR store it to some array
#.....if it's a zero, trigger the act of writing the relevant data in a new file 'summary table.txt', Then move on?
#	TIME, PRESSURE, RATE, CLEAN JOB, CONCENTRATION perhaps more?
# Writing the above is the next step.
# THEN, I must displaying the 'summary table.txt' in some GUI (Ask Arthur Jack).
'''
print count_semicolon, "semicolons"				# Debugging step
print "read line"						# Debugging step
#print read_line_p						# Print 'read_line_p'
'''
'''
# Read the REMAINING of the file from where we left off last
#..... and save it to 'read_p'
read_p = readstream.read()
print "read"							# Debugging step
print read_p							# Print 'read_p'
'''
'''
# Determine where in the file is the cursor located.
#..... Save that value to tell_p
tell_p = readstream.tell()
print "tell"
print tell_p
'''
# Close the reading stream. Always close the reading stream.

readstream.close()
print "close"


# Next, practice readline.
# Then, count the semicolons in the adt file.
# Next, work on resume.
# Next, Submit application.