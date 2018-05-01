# STECH-Capstone Project: Pyrate (roguelike)

by R. G. Blaine

**Pyrate** is a roguelike game developed using Python v2.7.8 (32-bit), Pygame, and the Doryen library (libtcod).

# Synopsis

"Pyrate" is an archaic spelling of the word "pirate." (Pirates being known rogues and scalliwags.)  It is also a play on words of "Python."

The game provides a GUI that allows the user to take on the role of a heroic frog trapped in a dungeon and fighting enemies such as crabs, ravens, and pythons in an attempt to escape said dungeon.

The game automatically saves the players progress when the player exits the game and, upon launching the game, allows the player to load a previously saved game or start anew.  In the spirit of roguelikes, however, the player has but one life.  Upon dying (or winning the game), the player's save file is erased.  When the player dies, a legacy text file is generated that contains all of the in-game messages generated during the game.

In lieu of using an inheritance scheme for objects, I opted to use a component scheme.  The main type of in-game object is called an "actor" and represents any object in the game that can move and/or interact in the game.  Component objects are created and attached to the actor object to denote different types of objects.  For example, creature components add the ability to attack, take damage, and "die."  Item commponents allow the actor object to be "used" in order to activate various abilities.  When "attaching" a component to the actor object, the actor is instructed that the component belongs to it the component is instructed that it belongs to the actor.

# Installation

As it stands, installation of the game requires that Python v2.7.8 (32-bit) as well as the pygame and libtcodpy modules be installed in the Python site packages directory. (These modules are included in the site-packages.zip file.)  To run the program, open it in Idle or another IDE and run it from there.

# Code Example

The actor object is the primary object in the game. The creature component was, by far, the most complicated one.  When an actor object is constructed, an optional creature argument is passed (defaulting to None) and attached to the actor object.

Actor Object:

```python
class objActor:

	'''
	any game element that can move/interact with other elements
	'''

	global LOS_MAP

	def __init__(self, x, y, nameObject, animationKey,
		animationDuration = 1.0,
		xpVal = 0,
		depth = 0,
		status = None,

		creature = None,
		ai = None,
		container = None,
		item = None,
		equipment = None,
		stairs = None):

		# map address
		self._x = x
		self._y = y

		self._xpValue = xpVal
		self._depth = depth
		self._status = status

		self._nameObject = nameObject

		# sprite
		self._animationKey = animationKey
		self._animation = ASSETS.animDict[self._animationKey]
		self._animationDuration = animationDuration / 1.0
		self._flickerSpeed = self._animationDuration / len(self._animation) # individual frame duration
		self._flickterTimer = 0.0
		self._spriteCounter = 0

		# creature component
		self.creature = creature
		if self.creature:
			self.creature.owner = self

		# ai component
		self.ai = ai
		if self.ai:
			self.ai.owner = self

		# container component
		self.container = container
		if self.container:
			self.container.owner = self

		# item component
		self.item = item
		if self.item:
			self.item.owner = self

		# equipment component
		self.equipment = equipment
		if self.equipment:
			self.equipment.owner = self

			self.item = compItem()
			self.item.owner = self

		# stairs component
		self.stairs = stairs
		if self.stairs:
			self.stairs.owner = self

	@property
	def _displayName(self):
		if self == PLAYER:
			return "Player"


		if self.creature and self._nameObject != "fly":
			return (self.creature._nameInstance + " the " + self._nameObject)
		
		if self.item:
			if self.equipment and self.equipment._equipped:
				return (self._nameObject + " (" + self.equipment._slot + ")")
			else:
				return (self._nameObject)


	def draw(self):
		if doryen.map_is_in_fov(LOS_MAP, self._x, self._y):
			SURFACE_MAP.blit(self._animation[self._spriteCounter], (self._x * const.TILE_WIDTH, self._y * const.TILE_HEIGHT))
			if len(self._animation) > 1:
				if CLOCK.get_fps() > 0.0:
					self._flickterTimer += 1 / CLOCK.get_fps()
				if self._flickterTimer >= self._flickerSpeed:
					self._flickterTimer = 0.0
					if self._spriteCounter >= len(self._animation) - 1:
						self._spriteCounter = 0
					else:
						self._spriteCounter += 1


	def distanceFrom(self, other):

		'''
		returns the distance between self and other calculated via pythagorean theorem
		'''

		diffX = other._x - self._x
		diffY = other._y - self._y

		return math.sqrt(diffX ** 2 + diffY ** 2)

	def moveTowards(self, other):

		'''

		'''

		diffX = other._x - self._x
		diffY = other._y - self._y

		moveX = 0
		moveY = 0

		if diffX != 0:
			moveX = diffX / abs(diffX)

		if diffY != 0:
			moveY = diffY / abs(diffY)

		self.creature.move(moveX, moveY)


	def moveAwayFrom(self, other):

		'''

		'''

		diffX = -(other._x - self._x)
		diffY = -(other._y - self._y)

		moveX = 0
		moveY = 0

		if diffX != 0:
			moveX = diffX / abs(diffX)

		if diffY != 0:
			moveY = diffY / abs(diffY)

		self.creature.move(moveX, moveY)

	def animDestroy(self):

		'''

		'''

		self._animation = None

	def animInit(self):

		'''

		'''

		self._animation = ASSETS.animDict[self._animationKey]
```

Creature Component:

```python

class compCreature:

	'''
	have health and can die
	can damage other objects by attacking them
	'''

	def __init__(self, nameInstance,
		baseAttack = 3,
		baseDefense = 0,
		health = 10,
		deathFunction = None,
		deathAnimKey = "SPR_CORPSE_RAVEN",
		levelCurrent = 1,
		xpCurrent = None):

		self._nameInstance = nameInstance

		self._baseAttack = baseAttack
		self._baseDefense = baseDefense

		self._maxHealth = health
		self._health = health

		self.deathFunction = deathFunction
		self._deathAnimKey = deathAnimKey

		self._levelCurrent = levelCurrent

		if xpCurrent:
			self._xpCurrent = xpCurrent
		else:
			self._xpCurrent = self._levelCurrent * (self._levelCurrent - 1) * 50

		self._xpNextLevel = self._levelCurrent * (self._levelCurrent + 1) * 50

	def attack(self, target):

		damage = self._power

		gameMessage(self.owner._displayName + " attacks " + target._displayName + "!",
			const.COLOR_ATTACK)

		# if the target is a turtle, chance to break player's weapon
		if self.owner == PLAYER and target._nameObject == "turtle" and doryen.random_get_int(0, 1, 100) <= const.BREAK_CHANCE:

			allEquippedItems = self.owner.container._equippedItems
			if allEquippedItems:
				for item in allEquippedItems:
					if item.equipment._slot  == 'main hand':
						gameMessage("Your sword broke!", const.COLOR_RED)
						self.owner.container._inventory.remove(item)

		# if the attacker is a turtle, chance to break player's shield
		if self.owner._nameObject == "turtle" and target == PLAYER and doryen.random_get_int(0, 1, 100) <= const.BREAK_CHANCE:

			allEquippedItems = target.container._equippedItems

			if allEquippedItems:
				for item in allEquippedItems:
					if item.equipment._slot  == 'off hand':
						gameMessage("Your shield broke!", const.COLOR_RED)
						target.container._inventory.remove(item)

		target.creature.takeDamage(damage)

		if damage > 0 and self.owner is PLAYER:
			hitSound = ASSETS.SFX_HIT_LIST[doryen.random_get_int(0, 0, len(ASSETS.SFX_HIT_LIST) - 1)]
			pygame.mixer.Sound.play(hitSound)

		# if the creature died, gain xp
		if target.creature == None:
			self._xpCurrent += target._xpValue
			# if enough xp, level up
			if self._xpCurrent >= self._xpNextLevel and self._levelCurrent < const.PLAYER_LEVEL_MAX:
				self.levelUp()


	def takeDamage(self, damage):
		damageTaken = max(1, damage - self._defense)
		gameMessage(self.owner._displayName + " takes " + str(damageTaken) + " damage!",
			const.COLOR_DAMAGE)
		self._health -= damageTaken

		if (self._health <= 0) and (self.deathFunction):
			self.deathFunction(self.owner, self._deathAnimKey)

	def healDamage(self, value):
		if value > (self._maxHealth - self._health):
			value = (self._maxHealth - self._health)
		self._health += value
		gameMessage(self.owner._displayName + " is healed for " + str(value) + " points",
			const.COLOR_HEAL)

	def move(self, xDiff, yDiff):
		tileIsWall = GAME._mapCurrent[self.owner._x + xDiff][self.owner._y + yDiff]._impassable

		target = mapCheckForCreature(self.owner._x + xDiff, self.owner._y + yDiff, self.owner)

		if target:
			self.attack(target)

		if not tileIsWall and target == None:
			self.owner._x += xDiff
			self.owner._y += yDiff

	def levelUp(self):
		self._levelCurrent += 1
		self._xpNextLevel += self._levelCurrent * 100
		self._maxHealth += doryen.random_get_int(0, 1, const.LVL_UP_HP_MAX)
		self._health = self._maxHealth
		if self._levelCurrent % 3 == 0:
			self._baseAttack += 1
		if self._levelCurrent % 5 == 0:
			self._baseDefense += 1
		gameMessage(self.owner._displayName + " is now level " + str(self._levelCurrent) +"!",
			const.COLOR_LEVEL_UP)

	@property
	def _power(self):

		equipmentBonusList = []
		if self.owner.container:
			equipmentBonusList = [obj.equipment._attackBonus for obj in self.owner.container._equippedItems]

		equipmentBonusTotal = 0
		for bonus in equipmentBonusList:
			equipmentBonusTotal += bonus

		totalDamage = self._baseAttack + equipmentBonusTotal

		return totalDamage

	@property
	def _defense(self):

		equipmentBonusList = []
		if self.owner.container:
			equipmentBonusList = [obj.equipment._defenseBonus for obj in self.owner.container._equippedItems]

		equipmentBonusTotal = 0
		for bonus in equipmentBonusList:
			equipmentBonusTotal += bonus

		totalDefense = self._baseDefense + equipmentBonusTotal
		return totalDefense

```

# Motivation

My motivation for this project stems from my love of programming and of games. The orginal PC game, Rogue, was a huge inspiration for me to become a programmer.

# API Reference

The title and credits screen includes GUI buttons to continue a saved game, start a new game, quit the game, and to open the options sub-menu.

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/TitleScreen.PNG "Title Screen")

The options sub-menu has GUI sliders to control the volume of game sound effects and music and a button to save these preferences to a file. (Saved preferences are automatically loaded when the game is run.)

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/OptionsMenu.PNG "Options Menu")

Here is a screenshot of actual gameplay.  The player (a frog) is near the center of the screen.  Map tiles and objects in the player's visible radius (8 tiles, with line of sight blocked by walls) are displayed in the "lighted" area.  Explored map tiles that are not visible are shaded darker.  On the right side of the screen, from the top down, are displayed:

* The player's current / maximum health

* The player's level, and current xp / xp needed to reach the next level

* The level of the dungeon map that the player is currently exploring

* A mini-map that shows explored tiles (and highlights currently visible tiles)

* A list of recent in-game messages

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/GameScreen.PNG "Game Screen")

The Help menu (H) lists the in-game commands and gives some advice on playing the game.

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/HelpMenu.PNG "Help Menu")

The Pause menu (P) pauses the game and gives the player the option to resume gameplay (P or ESCAPE) or to save and quit to the main menu (Q).

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/PauseMenu.PNG "Pause Menu")

The Inventory menu (I) lists all of the items the player is currently carrying.  Equipped items have the equipment slot indicated next to them.  (Each slot - main hand, off hand, and neck - can hold only one item.)

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/InventoryMenu.PNG "Inventory Menu")

The legacy text file (generated when the player dies or wins the game) lists all of the in-game messages the player recieved.

![alt text](https://github.com/Blaine-Rob5000/STECH-Capstone/blob/Images/LegacyFile.PNG "Legacy File")

# Tests

Testing the game is simply a matter of playing it.  I have thoroughly tested the game and believe the code to be sound and functioning as intended.  The constants file contains several variables that can be used to tweak gameplay and a flag to signal certain debug messages to print during gameplay.

# Contributors

The program is an original creation of me (Robin G. Blaine) and, as such, I claim it as my intellectual property.  However, certain elements were provided by other parties with the provision that they recieve credit.

* Graphics are courtesy of DragonDePlatino and DawnBringer:

	https://opengameart.org/content/dawnlike-16x16-universal-rogue-like-tileset-v181

* Music from Jukedeck - create your own at http://jukedeck.com

I also wish to extend a special thanks to Michael Coates, the self-proclaimed "Terrible Programmer" for his YouTube tutorial on pygame, the doryen library, and roguelike game programming.

Others who wish to modify the program may do so freely, provided that:

1. All proper credit is given to myself and the contributers listed above

2. The program may only be distributed free of charge and not "for profit"
