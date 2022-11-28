class Character:

    def __init__(self, name, health, attackpower):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.attackpower = attackpower

    def __repr__(self):
        return f"character: {self.name=:11}   {self.max_health=:4}     {self.current_health=:4}     {self.attackpower=:3}"

    def hit(self, other):
        print("\n", self.name, "hits", other.name, "for", self.attackpower, "damage", "\n")
        other.get_hit(self.attackpower)

    def get_hit(self, attackpower):
        self.current_health -= attackpower

    def get_healed(self, healpower):
        self.current_health += healpower


class Healer(Character):

    def __init__(self, name, health, healpower):
        super().__init__(name, health, 0)
        self.healpower = healpower

    def heal(self, other):
        print("\n", self.name, "heals", other.name, "for", self.healpower, "damage", "\n")
        other.get_healed(self.healpower)


hero1 = Character("Greg", 80, 10)
hero2 = Character("Also Greg", 80, 10)
hero3 = Healer("Greg as well", 80, 7)
print(hero1)
print(hero2)
print(hero3)
hero1.hit(hero2)
print(hero2)
hero2.hit(hero1)
print(hero1)
hero1.hit(hero2)
print(hero2)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)
hero1.hit(hero3)
print(hero3)
hero2.hit(hero1)
print(hero1)
hero3.heal(hero1)
print(hero1)
input()