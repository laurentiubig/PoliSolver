
#!/usr/bin/python

import sys
import re

polinom = sys.argv[1][:]
def find_abs(x):
	if x > 0:
		return x
	return -x
def find_sqrt(x):
	val = x
	while True:
		last = val
		val = (val + x/val) * 0.5
		if find_abs(val-last) < 1e-9:
			break
	return val
def find_biggest_grade(s):
	i = 0
	maxim = -1
	for i in range(0,len(s)):
		if s[i] == 'X' and s[i+2] > maxim:
			maxim = s[i+2]
	return maxim
polinom = polinom.replace(' ','')
rr_before_equal = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",polinom[0:polinom.find('=')])
rr_after_equal = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",polinom[polinom.find('='):len(polinom)])
grades =[0,0,0,0,0,0,0,0]
existing_grades = [0,0,0,0,0,0]
if len(rr_before_equal)%2 == 0:
	for i in range(0,len(rr_before_equal),2):
		grades[int(rr_before_equal[i+1])] = float(rr_before_equal[i]) if '.' in rr_before_equal[i] else int(rr_before_equal[i])
		existing_grades[int(rr_before_equal[i+1])] = 1
if len(rr_after_equal)%2 == 0:
	for i in range(0,len(rr_after_equal),2):
		grades[int(rr_after_equal[i+1])] -= float(rr_after_equal[i]) if '.' in rr_after_equal[i] else int(rr_after_equal[i])
		existing_grades[int(rr_after_equal[i+1])] = 1
polinom = ''
for i in range(len(existing_grades)):
	if existing_grades[i] == 1:
		if not polinom == '':
			if grades[i] >= 0:
				polinom += '+ '
		polinom += str(grades[i])+ ' * ' + 'X^' + str(i)+' '
polinom += '= 0'
print "Reduced form :",polinom
print "Polynomial degree :",find_biggest_grade(polinom)
if int(find_biggest_grade(polinom)) > 2:
	print "The polynomial degree is strictly greater than 2, I can't solve it."
else:
	delta = grades[1] * grades[1] - 4 * grades[2] * grades[0]
	print 'The discriminant is:',delta
	print 'Now we must compare the discriminant to 0'
	if delta > 0:
		if not existing_grades[2] == 0:
			print "Discriminant is strictly positive, the two solutions are:"
			x1 = (-grades[1] + find_sqrt(delta))/(2*grades[2])
			x2 = (-grades[1] - find_sqrt(delta))/(2*grades[2])
			print x2
			print x1
		elif existing_grades[1] == 0 and existing_grades[2] == 0:
			print "The equation has the degree 0"
			print "The solution is 0"
		else:
			print "Discriminant is strictly positive!"
			print "The solution is:"
			sol = (float(grades[0]))/(float(-1*grades[1]))
			print sol
	elif delta == 0:
		print 'The discriminant is equal to 0'
		all_numbers_solution = 0
		for i in range(0,3):
			if grades[i] == 0:
				all_numbers_solution += 1
		if all_numbers_solution == 3 :
			print 'All the real numbers are solutions to the given equation'
		elif existing_grades[2] == 0 and existing_grades[1] == 1:
			print 'The equation has the solution',-grades[0]/grades[1]
		elif existing_grades[2] == 0 and existing_grades[1] == 0:
			print 'The equation has the degree 0 so it is impossible to solve'
		else:
			print 'The equation has only one solution:'
			print -grades[1]/(2*grades[2])
	else:
		print 'The discriminant is strictly smaller than 0'
		print 'The given equation does not have any real solution'
		print 'The complex solutions are:'
		rez1 = str(-grades[1] + find_sqrt(-delta)) + 'i' + '/' + str(2*grades[2])
		rez2 = str(-grades[1] - find_sqrt(-delta)) + 'i' + '/' + str(2*grades[2])
		print rez1
		print rez2
