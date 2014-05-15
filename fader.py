class Fade(object):
	def __init__(self, steps, startcolor=None, endcolor=None):
		if startcolor is None:
			startcolor = (0,0,0)
		if endcolor is None:
			endcolor = (255,255,255)
		red_step = ((endcolor[0]-startcolor[0])+1)/steps
		green_step = ((endcolor[1]-startcolor[1])+1)/steps
		blue_step = ((endcolor[2]-startcolor[2])+1)/steps
		self.red = range(startcolor[0]+red_step-1, endcolor[0]+red_step,
						 red_step)
		self.green = range(startcolor[1]+green_step-1, endcolor[1]+green_step,
						   green_step)
		self.blue = range(startcolor[2]+blue_step-1, endcolor[2]+blue_step,
						  blue_step)
		self.index = 0
		return

	def __iter__(self):
		return self

	def next(self):
		try:
			result = (int(round(self.red[self.index])),
					  int(round(self.green[self.index])),
					  int(round(self.blue[self.index])))
		except IndexError:
			raise StopIteration
		self.index += 1
		return result
