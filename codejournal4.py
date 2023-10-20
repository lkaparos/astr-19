class MyFavoriteAnimal:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length=arm_length
		self.leg_length=leg_length
		self.num_eyes = num_eyes
		self.has_tail= has_tail
		self.is_furry=is_furry
	def describe (self):
		print(f"physical characteristics of sloth:")
		print(f"Arm length: {self.arm_length} feet")
		print(f"leg length: {self.leg_length} feet")
		print(f"number of eyes: {self.num_eyes}")
		print(f"has tail:{'yes' if self.has_tail else 'no'}")
		print(f"furry: {'Yes' if self.is_furry else 'no'}")

favorite_animal=MyFavoriteAnimal(2.5, 2.5, 2, True, True)
favorite_animal.describe()
