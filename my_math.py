def sum_num_and_avg(list_1):
	total_sum = 0
	total_num = 0
	avg = 0
	for item in list_1:
		if isinstance(item, float) or isinstance(item, int):
			total_sum += item
			total_num += 1
		else:
			pass
	return total_sum, total_num, total_sum/total_num

def sum_from_messy_list(list_1):
	total = 0
	for item in list_1:
		if isinstance(item, float) or isinstance(item, int):
			total += item
		else:
			pass
	return total

