import csv
import os

def write_header (filepath, *args):
	if not os.path.isfile(filepath):
		my_header = []
		for item in args:
			my_header.append(item)
		with open(filepath, 'w+') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(my_header)
	else:
		return "Watch out! This file is no empty! Try different csv name!"

def how_many_items_in_header(filepath):
	with open (filepath, 'r') as csvfile:
		real_list = []
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		for item in reader_list[0]:
			real_list.append(item)
		return len(real_list)

def how_many_rows(filepath):
	if os.path.isfile(filepath):
		with open (filepath, 'r') as csvfile:
			row_list = []
			reader = csv.reader(csvfile)
			reader_list = list(reader)
			for item in reader_list:
				row_list.append(item)
			return len(row_list) - 1		#header is not a row
	else:
		return "Wrong file name! It do not exist!"

def add_row (filepath, *args):
	if os.path.isfile(filepath):
		my_new_row = []
		for item in args:
			my_new_row.append(item)
		if len(my_new_row) == how_many_items_in_header(filepath):
			with open(filepath, 'a') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(my_new_row)
		else:
			return "Hey, your row is to short or to long! Header is different!"
	else:
		return "Wrong file name! It do not exist!"

def choose_row(filepath, row_num):
	if os.path.isfile(filepath):
		if row_num <= how_many_rows(filepath) and row_num is not 0:
			with open (filepath, 'r') as csvfile:
				reader = csv.reader(csvfile)
				reader_list = list(reader)
				selected_row = reader_list[row_num]
				return len(selected_row)
		elif row_num == 0:
			return "If you wanna change header use change_header!"
		else:
			return "Wooooah! There is not so many rows here!"
	else:
		return "Wrong file name! It do not exist!"

def row_content(filepath, row_num):
	if os.path.isfile(filepath):
		if row_num <= how_many_rows(filepath) and row_num is not 0:
			with open (filepath, 'r') as csvfile:
				reader = csv.reader(csvfile)
				reader_list = list(reader)
				selected_row = reader_list[row_num]
				return selected_row
		elif row_num == 0:
			return "If you wanna change header use change_header!"
		else:
			return "Wooooah! There is not so many rows here!"
	else:
		return "Wrong file name! It do not exist!"

