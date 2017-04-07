def create_message(one_name, one_amount):
	message = '''Hi {name_key}!
	we just send you {amount_key}$US.
	Thank you for your cooperation.'''
	one_name = one_name[:1].upper() + one_name[1:].lower()
	final_message = message.format(name_key=one_name, amount_key=one_amount)
	return final_message

#bad one
def create_messages_2(name_list, amount_list):
	message = '''Hi {name_key}!
	we just send you {amount_key}$US.
	Thank you for your cooperation.'''
	final_messages = []
	if len(name_list) == len(amount_list):
		for item in name_list:
			final_name = item[:1].upper() + item[1:].lower()
			final_amount = amount_list[0]
			final_message = message.format(name_key=final_name, amount_key=final_amount)
			final_amount = amount_list.pop(0)		#not to smart man!
			final_messages.append(final_message)
		return final_messages
	else:
		return "Some Error Appeared :("


#better one
def create_messages(name_list, amount_list):
	message = '''Hi {name_key}!
	we just send you {amount_key}$US.
	Thank you for your cooperation.'''
	final_messages = []
	if len(name_list) == len(amount_list):
		i = 0
		for item in name_list:
			final_name = item[:1].upper() + item[1:].lower()
			final_amount = amount_list[i]
			final_message = message.format(name_key=final_name, amount_key=final_amount)
			final_messages.append(final_message)
			i += 1
		return final_messages	
	else:
		return "Some Error Appeared :("