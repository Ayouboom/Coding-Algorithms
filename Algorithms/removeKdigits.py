class RemoveKdigits:
	def removeKdigits(self, num, k):
		"""
		:type num: str
		:type k: int
		:rtype: str
		"""
		res = ""
		num  = list(num)
		last = 1
		while k > 0 and last < len(num):
			if num[last-1] <= num[last]:
				last += 1
			elif num[last-1] > num[last]:
				del num[last-1]
				last -= 1
				if last == 0:
					last += 1
				k -= 1
		if k > 0:
			num = num[0:-k]
		if len(num) > 0:
			pointer  = 0
			while len(num[pointer:]) > 1 and num[pointer] == '0':
				pointer += 1
			return ''.join(num[pointer:])
		return '0'