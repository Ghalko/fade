class Fade(object):
	def __init__(self, steps, startcolor=None, endcolor=None):
		if startcolor is None or not isinstance(startcolor, tuple):
			startcolor = (0,0,0)
		if endcolor is None or not isinstance(endcolor, tuple):
			endcolor = (255,255,255)
		if len(startcolor) != len(endcolor):
			print "Indices do not match."
			return
		self.mlist = []
		for i in range(len(startcolor)):
			self.mlist.append(self.find_int(steps, startcolor[i],
											endcolor[i]))
		self.index = 0
		return

	def __iter__(self):
		return self

	def next(self):
		try:
			result = []
			for each in self.mlist:
				result.append(each[self.index])
		except IndexError:
			raise StopIteration
		self.index += 1
		result = tuple(result)
		return result

	def reset(self):
		self.index = 0

	def find_int(self, steps, start, end):
		ans = [start]
		step = float(end-start)/steps
		current = start + step
		for i in range(steps):
			ans.append(int(round(current)))
			current += step
		return ans
