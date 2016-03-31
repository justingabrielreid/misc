#!/usr/bin/python

#computing the atgc content of a DNA string 


class Base_counter(object):
	def __init__(self, DNA):
		self.DNA = DNA
		self.no_c = 0
		self.no_a = 0
		self.no_g= 0
		self.no_t= 0
	
	def c_counter(self):
		for base in self.DNA:	
			if base == 'c':
				self.no_c = self.no_c + 1 
		return self.no_c
	
	def g_counter(self):
		for base in self.DNA:	
			if base == 'g':
				self.no_g+=1 
		return self.no_g
	
	def a_counter(self):
		for base in self.DNA:	
			if base == 'a':
				self.no_a+=1 
		return self.no_a
	
	def t_counter(self):
		for base in self.DNA:	
			if base == 't':
				self.no_a+=1 
		return self.no_t
	
	def gc_percentage(self):
		return self.no_c + self.no_g / float(len(self.DNA))
	
	def at_percentage(self):
		return self.no_a + self.no_t / float(len(self.DNA))
	
	def g_percentage(self):
		return self.no_g / float(len(self.DNA))
	
	def a_percentage(self):
		return self.no_a / float(len(self.DNA))
	
	def t_percentage(self):
		return self.no_t / float(len(self.DNA))
	
	def c_percentage(self):
		return self.no_c / float(len(self.DNA))		

def main():
	dna= 'gcgctat'
	analyzer = Base_counter(dna)
	
	print analyzer.no_c
	print analyzer.c_counter()
	print analyzer.c_percentage()

if __name__ == '__main__':
	main()
	
	
		
		
