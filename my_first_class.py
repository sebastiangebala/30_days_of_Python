class Worker():
	company = "Linux Co."
	job = "IT Programer"
	absence = 0
	expected_days = 25
	working_days = 25
	amount = 3000
	def get_worker_details(self):
		return self.company, self.job, self.absence, self.working_days, self.amount
	def count_amount(self):
		return ((self.working_days - self.absence) * self.amount)/self.expected_days
	def amount_plus_extra(self, plus_extra):
		return (((self.working_days - self.absence) * self.amount)/self.expected_days) + plus_extra

class Boss(Worker):
	job = "boss"
	amount = 5000