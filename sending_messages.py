class SendMessage():
	users_list = []
	messages_list = []
	message = '''Hi {key_name}!,
	we just sent you {key_amount} US$.
	Appreciate that you cooperate with us!
	Greetings,
	Bastek'''
	def add_user(self, name, amount, email=None):
		name = name[:1].upper() + name[1:].lower()
		amount = "%.2f"%(amount)
		details_dict = {
			'name':name,
			'amount':amount
		}
		if email is not None:
			details_dict['email'] = email
		self.users_list.append(details_dict)
	def get_details(self):
		return self.users_list
	def sent_messages(self):
		if len(self.users_list) > 0:
			for item in self.users_list:
				name = item['name']
				amount = item['amount']
				message = self.message.format(key_name=name, key_amount=amount)
				self.messages_list.append(message)
			return self.messages_list
		else:
			return 'There is no one to send to'