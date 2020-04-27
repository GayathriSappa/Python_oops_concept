class Pokemon:
	
	pokemon= " "
	
	def __init__(self,name,level):
		self._name=name
		if self._name =="":
			raise ValueError("name cannot be empty")
		self._level= level
		if self._level <= 0:
			raise ValueError("level should be > 0")
		
	@property
	def name(self):
		return self._name
		
	@property 
	def level(self):
		return self._level
		
class Electric_Pokemon(Pokemon):
	sound=""
	runn=""
	
	
	@classmethod
	def make_sound(cls):
		print(cls.sound)
	
	@classmethod
	def run(cls):
		print(cls.runn)
	
class String(Pokemon):
	def __str__(self):
		return str(self._name) + ' - ' + "Level "+ str(self._level) 
	
class Water_Pokemon(Pokemon):
	swimm=""
	
	@classmethod
	def swim(cls):
		print(cls.swimm)
		
class Flying_Pokemon(Pokemon):
	flys=""
	
	@classmethod
	def fly(cls):
		print(cls.flys)
		
class Pikachu(Electric_Pokemon,String):
	sound="Pika Pika"
	runn="Pikachu running..."
	
	def attack(self):
		x=self._level*10
		print("Electric attack with {} damage".format(x))
		self._level +=1

class Squirtle(Water_Pokemon,Electric_Pokemon,String):
	sound="Squirtle...Squirtle"
	swimm="Squirtle swimming..."
	runn="Squirtle running..."
	
	def attack(self):
		x=self._level*9
		print("Water attack with {} damage".format(x))
		self._level +=1

class Pidgey(Electric_Pokemon,Flying_Pokemon,String):
	sound="Pidgey...Pidgey"
	flys="Pidgey flying..."
	
	def attack(self):
		x=self._level*5
		print("Air attack with {} damage".format(x))
		self._level +=1
	
class Swanna(Electric_Pokemon,Flying_Pokemon,Water_Pokemon,String):
	sound="Swanna...Swanna"
	flys="Swanna flying..."
	swimm="Swanna swimming..."
	
	def attack(self):
		x=self._level*9
		y=self._level*5
		print("Water attack with {} damage".format(x))
		print("Air attack with {} damage".format(y))
		self._level +=1
	
class Zapdos(Electric_Pokemon,Flying_Pokemon,String):
	sound="Zap...Zap"
	flys="Zapdos flying..."
	
	def attack(self):
		x=self._level*10
		y=self._level*5
		print("Electric attack with {} damage".format(x))
		print("Air attack with {} damage".format(y))
		self._level +=1
	
class Island:
	
	island_list=[]	
	def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
		self._name=name
		self._max_no_of_pokemon=max_no_of_pokemon
		self._total_food_available_in_kgs=total_food_available_in_kgs
		self._pokemon_left_to_catch=0
	@property
	def name(self):
	    return self._name
	@property
	def max_no_of_pokemon(self):
	    return self._max_no_of_pokemon
	@property
	def total_food_available_in_kgs(self):
	    return self._total_food_available_in_kgs
	@property
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
		
	def __str__(self):
		return "{} {} {} {} {} {} {}".format(self.name,'-',self.pokemon_left_to_catch,"pokemon",'-',self.total_food_available_in_kgs,"food")
		
	def add_pokemon(self,pokemon):
		self.island_list.append(pokemon)
		if self._pokemon_left_to_catch<self._max_no_of_pokemon:
			self._pokemon_left_to_catch+=1
		else:
			print("Island at its max pokemon capacity")
		
	def get_all_islands(self):
		return "{} {} {} {} {} {} {}".format(self.name,'-',self.pokemon_left_to_catch,"pokemon",'-',self.total_food_available_in_kgs,"food")

class Trainer:
	
	def __init__(self,name):
		
		self._name=name
		self._experience=1
		self._max_food_in_bag=10*self._experience
		self._food_in_bag=0
		self.pokemon_list=[]
		self._current_island=""
	@property 
	def name(self):
		return self._name
	
	@property 
	def experience(self):
		return self._experience

	@property 
	def max_food_in_bag(self):
		return self._max_food_in_bag

	@property 
	def food_in_bag(self):
		return self._food_in_bag
	
	
	def move_to_island(self,island):
		self._current_island=island
		self.island=island
	@property 
	def current_island(self):
		if  self._current_island == " ":
			print("You are not on any island")
		else:
			return self._current_island
	
	def catch(self,pokemon):
		if self._experience>=100*pokemon.level:
			print("You caught {}".format(pokemon.name))
			self._experience+=20
		else:
			print("You need more experience to catch {}".format(pokemon.name))
      
	
	def collect_food(self):
		self._food_in_bag +=self._max_food_in_bag
		self.island._total_food_available_in_kgs -=self._food_in_bag
	
	def __str__(self):
		return self._name
