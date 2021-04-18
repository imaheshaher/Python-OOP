class Container:
	def __init__(self,id,length,breadth,height,pricePerSqrft):
		self.id=id
		self.length=length
		self.breadth=breadth
		self.height=height
		self.pricePerSqrft=pricePerSqrft

	def volume(self):
		v=self.length*self.breadth*self.height
		return v


class PackagingCompany(Container):
	def __init__(self,containerLlist):
		self.containerLlist=containerLlist
		self.larg=0
		self.obj=None
	def findContainerCost(self,id):
		for i in self.containerLlist:
			if i.id==id:
				super().__init__(i.id,i.length,i.breadth,i.height,i.pricePerSqrft)
				v=self.volume()
				c=i.pricePerSqrft*v
				return c
			return None
	def findLargestContainer(self):
		for i in self.containerLlist:
			super().__init__(i.id,i.length,i.breadth,i.height,i.pricePerSqrft)
			v=self.volume()
			if v>self.larg:
				self.larg=v
				self.obj=i

		return self.obj





list =[]
ob1=Container(1,2,3,4,5)
ob2=Container(2,3,3,4,5)
ob3=Container(3,4,3,4,5)
list=[ob1,ob2,ob3]

ob=PackagingCompany(list)
a=ob.findContainerCost(1)
print(a)

b=ob.findLargestContainer()
print(b.__dict__)

