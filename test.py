from os import getlogin
from psutil import virtual_memory
from psutil import getloadavg

# 1 задание
class PC_memory:
	def __init__(self, pc_id, memory_total, memory_used, memory_percent=None):
        	self.pc_id = pc_id
        	self.memory_total = memory_total
        	self.memory_used = memory_used
        	self.memory_percent = memory_percent
        	if self.memory_percent == None:
            		self.memory_percent = (memory_used / memory_total) * 100
	def show_used_percent(self):
        	print(f'PC with id {self.pc_id} used {self.memory_percent} percent of memory')

	def is_enough_memory(self):
		if (self.memory_percent < 10) or (self.memory_total - self.memory_used < 1073741824):
		return False
	else:
		return True

# 2 задание
class PC_advanced(PC_memory):
	def __init__(self, pc_id, memory_total, memory_used, ld_avg_1m,
	ld_avg_15m, memory_percent=None):
        	super().__init__(pc_id, memory_total, memory_used, memory_percent)
        	self.ld_avg_1m = ld_avg_1m
        	self.ld_avg_15m = ld_avg_15m
        
    # 3 задание
	def is_overloaded(self):
        	if (self.ld_avg_1m / self.ld_avg_15m > 3):
            		return True
		else:
			return False

	def __call__(self, string='memory'):
        	if string == 'memory':
			return self.is_enough_memory()
		elif string == 'load':
			return self.is_overloaded()
		else:
			return None

# 4 задание
exemplar = PC_advanced(getlogin(), virtual_memory()[0], virtual_memory()[3], getloadavg()[0], getloadavg()[2])

# 5 задание
print(exemplar.is_overloaded())

# 6 задание
print(exemplar())
