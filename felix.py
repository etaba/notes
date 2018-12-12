import threading

class elevator:
	def __init__(self,name):
		self.destinations = []
		self.floor = 0
		self.name = name
		threading.Timer(1,self.run).start()

	def eta(self, floor):
		if len(self.destinations) == 0:
			dist = abs(self.floor - floor)
		else:
			dist = abs(self.floor - self.destinations[0])
			for i,dest in enumerate(self.destinations[1:]):
				dist += abs(self.destinations[i] - dest)
			dist += abs(self.destinations[-1] - floor)
		print(f'{self.name} has eta {dist}')
		return dist * 5

	def call(self,floor):
		self.destinations.append(floor)


	def run(self):
		threading.Timer(1,self.run).start()
		print(f'{self.name} on {self.floor}')
		if len(self.destinations) > 0:
			if self.destinations[0] > self.floor:
				self.floor += 1
			elif self.destinations[0] < self.floor:
				self.floor -= 1
			else:
				#arrived
				print(f'{self.name} arrived at {self.floor}!')
				del self.destinations[0]

def call_fastest(e1,e2,floor):
	if e1.eta(floor) < e2.eta(floor):
		e1.call(floor)
	else:
		e2.call(floor)

e1 = elevator('Elevator 1')
e2 = elevator('Elevator 2')

while True:
	floor = input('')
	call_fastest(e1,e2,int(floor))