class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, moves):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attackstat = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves  # List of tuples (move_name, power)
    def display_stats(self):
        moves_str = ', '.join([f"{move[0]} ({move[1]})" for move in self.moves])
        return (f"{self.name} - HP: {self.current_hp}/{self.max_hp}, "
                f"Attack: {self.attackstat}, Defense: {self.defense}, Speed: {self.speed}\n"
                f"Moves: {moves_str}")
    def take_damage(self, amount):
        self.current_hp = max(0,self.current_hp-amount)
    def is_fainted(self):
        return self.current_hp <= 0
    def attack(self, target, move_index):
        power = self.moves[move_index][1]
        damage=int(power*self.attackstat/target.defense)
        target.take_damage(damage)
        