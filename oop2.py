class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth

	def square(self):
		return "hello"
		return self.length*self.breadth




class Calculate(Rectangle):
	def __init__(self,id,list):
		self.id=id
		self.list=list
	def calcsq(self):
		for i in self.list:
			# super().__init__(i.length,i.breadth)
			v=self.square()
			print(v)

l=[]
ob=Rectangle(10,20)
ob2=Rectangle(20,30)
l.append(ob)
l.append(ob2)
cob=Calculate(1,l)
cob.calcsq()




