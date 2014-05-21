from Tkinter import *
from fader import Fade

def dec2hex(t):
	result = "#"
	for each in t:
		hnum = hex(each)
		if len(hnum) == 3:
			result += '0' + hnum[2]
		else:
			result += hnum[2] + hnum[3]
	return result

class Demo(object):
	def __init__(self, root):
		self.root = root
		self.fade = Fade(256) #default 0-255
		self.label = Label(root, text="text", fg="#000000", font=("Arial", 54))
		self.label.pack()
		Button(root, text="Reset", command=self.reset).pack()
		self.fade_more()

	def reset(self):
		self.fade.reset()
		self.fade_more()

	def fade_more(self):
		try:
			current = self.fade.next()
			self.label.config(fg=dec2hex(current)) #configures text to next color
			self.label.pack()
			root.after(100, self.fade_more)
		except StopIteration:
			return

root = Tk()
r = Demo(root)
root.mainloop()