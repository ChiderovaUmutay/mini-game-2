from random import uniform, randint

from custom_exceptions import EquipmentWornOutError
from secondary_functions import validate_attribute


class Equipment:
    def __init__(self, name, taken_capacity):
        validate_attribute(attribute=taken_capacity,
                                 min_val=30,
                                 max_val=100,
                                 message="The range of occupied volume should be from 30 to 100")
        self.name = name
        self.wear_condition = 0
        self.taken_capacity = taken_capacity


    def action(self):
        if self.wear_condition >= 100:
            raise EquipmentWornOutError()
        else:
            self.wear_condition += 10

    def calculate_equipment_efficiency(self, equipment):
        calculated_damage = equipment - (equipment * self.wear_condition) / 100
        return calculated_damage

    def __str__(self):
        equipment_characteristics = f"Equipment name: {self.name}\n" \
                                    f"Wear condition of equipment: {self.wear_condition}\n" \
                                    f"Taken capacity of equipment: {self.taken_capacity}"
        print(equipment_characteristics)


class Weapon(Equipment):

    def __init__(self, name, taken_capacity, min_damage, critical_hit_chance):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=min_damage,
                                 min_val=5,
                                 max_val=40,
                                 message="The number of units of minimum damage should be from 5 to 40")
        validate_attribute(attribute=critical_hit_chance,
                                min_val=1,
                                max_val=70,
                                message="The number of units of critical chance should be from 1 to 70")
        self.min_damage = min_damage
        self.critical_hit_chance = critical_hit_chance
        self.max_damage = self.min_damage + (self.min_damage * 40) / 100

    def action(self):
        damage = round(uniform(self.min_damage, self.max_damage), 1)
        if damage <= self.critical_hit_chance:
            critical_damage = (self.max_damage * 40) / 100
            print("critical_damage")
            return self.get_calculated_damage(critical_damage)
        elif damage <= 15:
            return 0
        else:
            return self.get_calculated_damage(damage)

    def __str__(self):
        super().__str__()
        damage_info = f"The number of weapon minimum damage units: {self.min_damage}\n" \
                      f"The number of weapon maximum damage units: {self.max_damage}\n" \
                      f"The number of weapon critical hit chance units: {self.critical_hit_chance}"
        print(damage_info)

    def get_calculated_damage(self, damage):
        calculated_damage = self.calculate_equipment_efficiency(damage)
        super().action()
        return calculated_damage



class Armor(Equipment):

    def __init__(self, name, taken_capacity, defence):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=defence,
                                min_val=1,
                                max_val=10,
                                message="The range of the number of protection units should be from 1 to 10")
        self.defence = defence
    def action(self):
        calculated_defence = self.calculate_equipment_efficiency(self.defence)
        super().action()
        return calculated_defence


    def __str__(self):
        super().__str__()
        print(f"The number of armor protection units: {self.defence}")


class Navigator(Equipment):

    def __init__(self, name, taken_capacity, accuracy):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=accuracy,
                                min_val=5,
                                max_val=40,
                                message="The range of the number of accuracy units should be from 5 to 40")
        self.accuracy = accuracy
    def action(self):
        electromagnetic_surge_probability = randint(1, 100)
        if electromagnetic_surge_probability <= 20:
            self.accuracy /= 2
        calculated_accuracy = self.calculate_equipment_efficiency(self.accuracy)
        return calculated_accuracy

    def __str__(self):
        super().__str__()
        print(f"The number of navigator accuracy units: {self.accuracy}")