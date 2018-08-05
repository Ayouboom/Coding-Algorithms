"""
Author: Ayoub Omari
Date : 07/07/2018


HashTable implementation

Main operations:
	* test if we have reached 2/3 of the size & resize (*4 if our size<5K elements for e.g and *2 otherwise)
	* change the position of elements when resizing (i think !- since we will take more bits we will end up with new indexes) 
	* collision handling - we have to find the mathematical function that gives the next position (we can start by the linear approach,
				quadratic approach, and the double hashing)

some additional stuff learned:
	-> position = self.getNextPosition(key, position)	# stateful function hh & one line & called many times => no function :D 
	-> Linear probing for example would run into an infinite loop if we were not resizing before the table is full

DONE:
	-> HashTable with linear probing in collision handling
	-> HashTable with resizing
	-> put handles the case of update instead of insert
	-> delete method
	-> compute max and avg number of collisions for look up (put and get use the same look up)


TODO:
	-> keys : tables + objects + see if there are other types to handle in converting to bytes
	-> implement & compare different probing approaches
			in doubt, we display the graphs for put and get operations
			i think get makes less search
	-> compare time performance 
	

	-> Final : compare ACTUAL performance with python dictionary
	-> see why/how java is doing both hash table separate chaining and open addressing
	-> an animation in the terminal to see an image of all operations :D (@see Brandon Rhodes to learn sthg)
"""
import hashlib, struct, time

class HashTable:

	def __init__(self):
		# self.size = 8
		self.size = 1 << 20
		self.table = [None] * self.size
		self.nbElements = 0
		self.maxNbCollisions = 0
		self.totNbCollisions = 0


	def put(self, key, value):
		"""
		put the (key, value) pair in the hash table
		"""
		if 3*self.nbElements >= 2*self.size:
			self.resize()

		position = self.getPosFromKey(key)
		offset = 1
		hash1 = self.hash(key)
		hash2 = self.hash2(key)

		# while self.isOccupied(position):
		while self.table[position] is not None and self.table[position].alive:
			
			if self.table[position].key == key:		# case of updating not inserting
				self.table[position].value = value
				return

			# print("inserting ", key, ": position ", position, " is occupied")
			# position = (hash1 + offset) % self.size 		# linear probing
			if offset % 2:		#quadratic probing	: alternating the sign so as to reach all possible indices in table(@stackoverflow)
				position = (hash1 + offset*offset) % self.size 		
			else:
				position = (hash1 - offset*offset) % self.size 		

			# if offset % 2:		
			# 	position = (hash1 + offset*hash1) % self.size
			# else:
			# 	position = (hash1 - offset*hash1) % self.size

			offset += 1

		self.updateMaxNbCollisions(offset-1)
		self.totNbCollisions += offset-1


		# print("inserting ", key, "in the position", position)
		self.table[position] = Slot(self.hash(key), key, value)
		self.nbElements += 1


	def get(self, key):
		"""
		get the value of the key in the hashtable
		"""
		position = self.getPosFromKey(key)
		offset = 1
		hash1 = self.hash(key)
		hash2 = self.hash2(key)

		while self.table[position] is not None and self.table[position].key != key:
			# position = (hash1 + offset) % self.size # linear probing
			if offset % 2:		#quadratic probing	: alternating the sign so as to reach all possible indices in table(@stackoverflow)
				position = (hash1 + offset*offset) % self.size 		
			else:
				position = (hash1 - offset*offset) % self.size
			# position = (hash1 + offset*hash2) % self.size 		# double hashing probing
			offset += 1

		if self.isOccupied(position):
			return self.table[position].value

	def updateMaxNbCollisions(self, nb):
		if nb > self.maxNbCollisions:
			self.maxNbCollisions = nb



	def getPosFromKey(self, key):
		hash_ = self.hash(key)
		return hash_ % self.size


	def isOccupied(self, position):
		return self.table[position] is not None and self.table[position].alive


	def getNextPosition(self, key, currentPos):
		"""
		In case there is a collision, return another position that hopefully is not full
		"""
		# linear probing
		# return (currentPos+1) % self.size


	def delete(self, key):
		"""
		deleting the slot associated with the key key
		"""
		position = self.getPosFromKey(key)
		offset = 1
		hash1 = self.hash(key)
		hash2 = self.hash2(key)

		while self.table[position] is not None and self.table[position].key != key:
			# position = (hash1 + offset) % self.size 	# linear probing
			if offset % 2:		#quadratic probing	: alternating the sign so as to reach all possible indices in table(@stackoverflow)
				position = (hash1 + offset*offset) % self.size 		
			else:
				position = (hash1 - offset*offset) % self.size
			# position = (hash1 + offset*hash2) % self.size 		# double hashing probing
			offset += 1

		if self.table[position] is not None:
			self.table[position].alive = False	# case more than one consecutive call to delete of the same key we just restore False
			self.nbElements -= 1


	def hash(self, key):
		if type(key) is int:
			hashedKey = hashlib.md5(bytearray(struct.pack("i", key)))
		elif type(key) is str:
			hashedKey = hashlib.md5(bytes(key, 'utf-8'))
		elif type(key) is float:
			hashedKey = hashlib.md5(bytearray(struct.pack("f", key)))
		elif type(key) is bool:
			hashedKey = hashlib.md5(bytes([int(key)]))
		else:
			print("type ", type(key), " is not so far supported")
			exit(1)
		return int(hashedKey.hexdigest(), 16)


	def hash2(self, key):
		if type(key) is int:
			hashedKey = hashlib.sha1(bytearray(struct.pack("i", key)))
		elif type(key) is str:
			hashedKey = hashlib.sha1(bytes(key, 'utf-8'))
		elif type(key) is float:
			hashedKey = hashlib.sha1(bytearray(struct.pack("f", key)))
		elif type(key) is bool:
			hashedKey = hashlib.sha1(bytes([int(key)]))
		else:
			print("type ", type(key), " is not so far supported")
			exit(1)
		return int(hashedKey.hexdigest(), 16)


	def resize(self):
		# print("\nresizing the hashtable from ", self.size, end='')
		if self.size < 5000:
			self.size = self.size * 4
		else:
			self.size = self.size * 2
		# print(" to ", self.size)

		
		table = self.table
		self.table = [None] * self.size
		self.nbElements = 0
		for slot in table:
			if slot is not None:
				self.put(slot.key, slot.value)


	def getSize(self):
		return self.nbElements

	def getAllocatedSize(self):
		return self.size

	def __str__(self):
		toStr = '{'
		for slot in self.table:
			if slot is not None:
				toStr += '('+str(slot.key)+':'+str(slot.value)+'), '
		return toStr[:-2]+'}'


	def printTable(self):
		print("\n")
		self.printHeader()
		for i, slot in enumerate(self.table):
			print(" ", "-"*41)
			if slot is not None:
				self.printPieceOfSlot(i)
				self.printPieceOfSlot(slot.key)
				self.printPieceOfSlot(slot.value)
			else:
				self.printPieceOfSlot(i)
				for _ in range(2):
					self.printPieceOfSlot()
			print("|")


	def printHeader(self):
		print("|", " "*2, "index", " "*2, "|", " "*3, "key", " "*3, "|", " "*2, "value", " "*2, "|")


	def printPieceOfSlot(self, value=None):
		print("|", end="")
		if value is None:
			print(" "*13, end="")
		elif value//10 == 0:
			print(" "*5, value, " "*5, end="")
		elif value//100 == 0:
			print(" "*4, value, " "*5, end="")
		elif value//1000 == 0:
			print(" "*4, value, " "*4, end="")




class Slot:

	def __init__(self, hash_, key, value):
		self.alive = True
		self.hash = hash_
		self.key = key
		self.value = value


# Testing

hashtable_ayoub = HashTable()
hashtable_python = dict()


start = time.time()
for i in range(1000000):
	hashtable_ayoub.put(i, i)
	# hashtable_python[i] = i
end = time.time()
print(end-start)
# print(hashtable_python[5000])
# print("Average number of collisions : ", hashtable.totNbCollisions/hashtable.nbElements)
# hashtable.printTable()


# print("Number of elements : ", hashtable.getSize())
# print("Allocated memory size : ", hashtable.getAllocatedSize())