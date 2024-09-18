class GameObject:
    def __init__(self, xpos, ypos, name, description, object_type, health=0, damage=0, defense=0):
        self.xpos = xpos 
        self.ypos = ypos
        self.name = name  
        self.description = description 
        self.object_type = object_type  
        self.health = health  
        self.damage = damage 
        self.defense = defense