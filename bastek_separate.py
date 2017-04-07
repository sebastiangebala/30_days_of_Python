def separate_num_and_str(list_1):
	list_num = []
	list_str = []
	for item in list_1:
		if item == True or item == False:
			pass
		elif isinstance(item, int):
			list_num.append(item)
		elif isinstance(item, str):
			list_str.append(item)
		else:
			pass
	return list_num, list_str

def separate_and_sort(list_1):
	list_num = []
	list_str = []
	for item in list_1:
		if item == True or item == False:
			pass
		elif isinstance(item, int):
			list_num.append(item)
		elif isinstance(item, str):
			first_letter = item[:1].upper() + item[1:].lower()	#needed to be sorted
			list_str.append(first_letter)
		else:
			pass
	return sorted(list_num), sorted(list_str)

def separate_and_sort_clean(list_1):
	list_num = []
	list_str = []
	for item in list_1:
		if isinstance(item, int) or isinstance(item, float):
			list_num.append(int(item))		#full number
		elif isinstance(item, str):
			first_letter = item[:1].upper() + item[1:].lower()	#needed to be sorted
			list_str.append(first_letter)
		else:
			pass
	return sorted(list_num), sorted(list_str)

def clean_and_organize(*args):
	list_num = []
	list_str = []
	for item in args:
		if isinstance(item, int) or isinstance(item, float):
			list_num.append(int(item))		#full number
		elif isinstance(item, str):
			first_letter = item[:1].upper() + item[1:].lower()	#needed to be sorted
			list_str.append(first_letter)
		else:
			pass
	return sorted(list_num), sorted(list_str)

#wołając używamy clean_and_organize(*list_1, *list_2, *list_3) 
#to umożliwia nam przechodzenie po każdym elemencie listy