from random import uniform


class EquipmentWornOutError(Exception):
    pass


class Equipment:
    def __init__(self, name, taken_capacity, wear_condition=0):
        self.validate_attribute(attribute=taken_capacity,
                                 min_val=30,
                                 max_val=100,
                                 message="The range of occupied volume should be from 30 to 100")
        self.name = name
        self.wear_condition = wear_condition
        self.taken_capacity = taken_capacity

    @staticmethod
    def validate_attribute(attribute, min_val, max_val, message):
        bool_val = min_val <= attribute <= max_val
        if bool_val is False:
            raise ValueError(message)

    def action(self):
        if self.wear_condition >= 100:
            raise EquipmentWornOutError()
        else:
            self.wear_condition += 10

    def calculate_damage_taking_into_account_wear(self, damage):
        calculated_damage = damage - (damage * self.wear_condition) / 100
        return round(calculated_damage)

    def __str__(self):
        equipment_characteristics = f"Equipment name: {self.name}\n" \
                                    f"Equipment wear condition: {self.wear_condition}\n" \
                                    f"Equipment taken capacity: {self.taken_capacity}"
        print(equipment_characteristics)


class Weapon(Equipment):

    def __init__(self, name, taken_capacity, min_damage, critical_hit_chance, wear_condition=0):
        super().__init__(name, taken_capacity, wear_condition=wear_condition)
        self.validate_attribute(attribute=min_damage,
                                 min_val=5,
                                 max_val=40,
                                 message="Minimum damage range should be from 5 to 40")
        self.validate_attribute(attribute=critical_hit_chance,
                                min_val=1,
                                max_val=70,
                                message="Critical damage range should be from 1 to 70")
        self.min_damage = min_damage
        self.critical_hit_chance = critical_hit_chance
        self.max_damage = self.min_damage + (self.min_damage * 40) / 100

    def action(self):
        damage = round(uniform(self.min_damage, self.max_damage))
        if damage <= self.critical_hit_chance:
            critical_damage = (self.max_damage * 40) / 100
            return self.get_calculated_damage(critical_damage)
        elif damage <= 15:
            return 0
        else:
            return self.get_calculated_damage(damage)

    def __str__(self):
        super().__str__()
        damage_info = f"Minimum damage: {self.min_damage}\n" \
                      f"Maximum damage: {self.max_damage}\n" \
                      f"Critical hit chance: {self.critical_hit_chance}"
        print(damage_info)

    def get_calculated_damage(self, damage):
        calculated_damage = self.calculate_damage_taking_into_account_wear(damage)
        super().action()
        return calculated_damage
