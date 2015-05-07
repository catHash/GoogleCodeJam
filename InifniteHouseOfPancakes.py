#import copy

def recursive_split(values,target_numsplits):
	global numsplits
	#print("values: " + str(values) + " numsplits : " + str(numsplits) + " target_numsplits " + str(target_numsplits))
	#if max(values) < len(values):
	#	return numsplits + int(max(values))
	if numsplits >= target_numsplits:
		print("return 1")
		return numsplits + int(max(values))
	#if int(max(values))%2 > 0:
		#print("does not devide even")
		#new_numbers = (int(max(values))-1)/2
	if int(max(values))%2 == 0:
		new_numbers = int(max(values))/2
		values[values.index(max(values))] = new_numbers
		values.append(new_numbers)
		numsplits = numsplits + 1
		#values2 = copy.deepcopy(values)
		recursive_split(values,target_numsplits)
	print("return 2, values: " + str(values) + " numsplits " + str(numsplits))
	return numsplits + int(max(values))
	
	

with open('B-small.in', 'r') as openfileobject:
	i = 0
	j = 0
	lowest_time = 0
	for line in openfileobject:
		values = line.split()
		if i == 0:
			T = values[0]
		if i > 0:
			if i%2 == 0:#pancake stacks
				j = j + 1
				lowest_time = max(values)
				values_sum = 0
				for x in values:
					for y in x:
						values_sum = values_sum + int(y)
				print("default time: " + str(max(values)))
				for x in range(1,1000000):
					if int(x) > values_sum:
						break
					numsplits = 0
					total_time = recursive_split(values, x)
					if total_time < lowest_time:
						lowest_time = total_time
					print("case # " + str(j) + " num splits: " + str(x) + " time: " + str(total_time))
			
				print("LINE: ", line)
					#print("num values: ", str(len(values)))
		#print("Case #" + str(j) + ": " + str(lowest_time))
		i = i + 1

