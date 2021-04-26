class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

	def add(self, animal):
		self.animals.append(animal)

	def report(self):
		print(f"{self.attraction_name} is where you'll find animals such as")
		for animal in self.animals:
			print(f"* {animal")


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy slithering things to cuddle"
        self.animals = list()

	def add(self, animal):
		self.animals.append(animal)

	def report(self):
		print(f"{self.attraction_name} is where you'll find slitherings such as")
		for animal in self.animals:
			print(f"* {animal")


class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy wetlanders to cuddle"
        self.animals = list()

	def add(self, animal):
		self.animals.append(animal)

	def report(self):
		print(f"{self.attraction_name} is where you'll find wetlanders such as")
		for animal in self.animals:
			print(f"* {animal")


