import math
import sys
import random 
from collections import defaultdict, Counter

class Order(): 
    def __init__(self,status, order_num, item_num,customer):
    	self.status = status
    	self.order_number = order_num
    	self.item_number = item_num
    	self.customer = customer
    	self.order_time = 10 

    def set_status(self, status): 
    	self.status = status

    def get_status(self): 
    	return self.status
    	

class Tailor():
    def __init__(self, is_booked, capacity):
        self.is_booked = False 
        self.time_capacity = capacity  # hours
        self.time_booked = 0 # hours
        self.order_objects = [] # order objects
        self.estimated_time = 0 #hours


    def add_order(self, order): 
    	self.order_objects.append(order)


class Measurements(): 
	def __init__(self, height, chest, shoulders, waist, hips, legs_lengh, neck_to_waist):
		self.height = height #cm
		self.chest = chest #cm
		self.shoulders = shoulders #cm
		self.waist = waist #cm
		self.hips = hips #cm
		self.legs_lengh = legs_lengh #cm
		self.neck_to_waist = neck_to_waist #cm


class Customer(): 
	def __init__(self, name, age, gender, measurements):
		self.name = name
		self.age = age 
		self.gender = gender 
		self.measurements = measurements
		self.orders = []

class ManagementSystem(): 
	def __init__(self):
		self.all_tailors_occupied = False 
		self.customers = defaultdict() 
		self.orders = [] 
		self.tailors = [] 

	def generateFakeOrders(self):
		
		for name in ['a','b','c','d','e','f','g']:
			age = random.choice([23,24,25,26,27,28]) 
			measure = random.choice([50,55,44])
			measurements = Measurements(measure,50,measure,50,measure,50,50)
			customer = Customer(name, age,"Female",measurements)
			self.customers[name] = customer
		print ("\nGenerating Orders...\n\n")
		print ("Number of Customers: ", len(self.customers))
		for i in range(2000): 
			if i < 100:
				cap = random.choice([20,30,10]) 
				tailor = Tailor(False, cap)
				self.tailors.append(tailor)
			
			item_num = random.choice([1,2,3])
			cust = random.choice(['a','b','c','d','e','f','g'])
			customer = self.customers[cust]
			order = Order("Created",i,item_num,customer)
			self.orders.append(order)

		print ("Number of tailors: ",len(self.tailors))
		print("Number of Orders:", len(self.orders))

	def order_analytics(self):
		items = [] 
		customers = [] 
		for order in self.orders: 
			items.append(order.item_number)
			customers.append(order.customer.name)
		cCustomer = Counter(customers)
		iOrders = Counter(items)
		print ("\n\n=====Order Analytics======")
		print ("Number of orders from each Customer: ",cCustomer)
		print ("Number of each order: ", iOrders)


	def serviceOrders(self): 

		 

if __name__ == "__main__":
	# tailor1 = Tailor(False, 20)
	# measurements1 = Measurements(50,50,50,50,50,50,50)
	# customer1 = Customer("Pooja","23","Female",measurements1)
	# order1 = Order("Created",1,1,customer1)
	
	# print (tailor1.time_capacity)
	# print (customer1.name)
	
	mgmt = ManagementSystem() 
	mgmt.generateFakeOrders()
	mgmt.order_analytics()



