# STECH-Capstone Project: Pyrate

by R. G. Blaine

**Pyrate** is a roguelike game developed using Python v2.7.8, Pygame, and the Doryen library (libtcod).

# Synopsis

"Pyrate" is an archaic spelling of the word "pirate." (Pirates being known rogues and scalliwags.)  It is also a play on words of "Python."

The game provides a GUI that allows the user to take on the role of a heroic frog trapped in a dungeon and fighting enemies such as crabs, ravens, and pythons in an attempt to escape said dungeon.

The game automatically saves the players progress when the player exits the game and, upon launching the game, allows the player to load a previously saved game or start anew.  In the spirit of roguelikes, however, the player has but one life.  Upon dying (or winning the game), the player's save file is erased.  When the player dies, a legacy text file is generated that contains all of the in-game messages generated during the game.

In lieu of using an inheritance scheme for objects, I opted to use a component scheme.  The main type of in-game object is called an "actor" and represents any object in the game that can be move and/or interact.  Component objects are created and attached to the actor object to denote different types of objects.  For example, creature components add the ability to attack, take damage, and "die."  Item commponents allow the actor object to be "used" in order to activate various abilities.  When "attaching" a component to the actor object, the actor is instructed that the component belongs to it the component is instructed that it belongs to the actor.

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



# Motivation

???

# Installation

???

# API Reference

???

# Tests

???

# Contributors

???


