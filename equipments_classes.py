from random import uniform, randint

from helpers.custom_exceptions import EquipmentWornOutError
from helpers.info_messages import equipment_data_messages, weapon_data_messages, armor_data_messages, \
    navigator_data_messages
from helpers.secondary_functions import validate_attribute


class Equipment:
    def __init__(self, name: str, taken_capacity: int) -> None:
        validate_attribute(attribute=taken_capacity,
                           min_val=30,
                           max_val=100,
                           message=equipment_data_messages.get("taken_capacity_error_message"))
        self.name = name
        self.wear_condition = 0
        self.taken_capacity = taken_capacity

    def action(self) -> None:
        if self.wear_condition >= 100:
            raise EquipmentWornOutError()
        else:
            self.wear_condition += 10

    def calculate_equipment_efficiency(self, equipment: int or float) -> int or float:
        calculated_damage = equipment - (equipment * self.wear_condition) / 100
        return calculated_damage

    def __str__(self) -> None:
        print(equipment_data_messages.get("info_message").format(self.name,
                                                                 self.wear_condition,
                                                                 self.taken_capacity))


class Weapon(Equipment):

    def __init__(self, name: str, taken_capacity: int, min_damage: int, critical_hit_chance: int) -> None:
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=min_damage,
                           min_val=5,
                           max_val=40,
                           message=weapon_data_messages.get("min_damage_error_message"))
        validate_attribute(attribute=critical_hit_chance,
                           min_val=1,
                           max_val=70,
                           message=weapon_data_messages.get("critical_hit_chance_error_message"))
        self.min_damage = min_damage
        self.critical_hit_chance = critical_hit_chance
        self.max_damage = self.min_damage + (self.min_damage * 40) / 100

    def action(self) -> int or float:
        damage = round(uniform(self.min_damage, self.max_damage), 1)
        if damage <= self.critical_hit_chance:
            critical_damage = (self.max_damage * 40) / 100
            return self.get_calculated_damage(critical_damage)
        elif damage <= 15:
            return 0
        else:
            return self.get_calculated_damage(damage)

    def __str__(self) -> None:
        super().__str__()
        print(weapon_data_messages.get("info_message").format(self.min_damage,
                                                              self.max_damage,
                                                              self.critical_hit_chance))

    def get_calculated_damage(self, damage: int or float) -> int or float:
        calculated_damage = self.calculate_equipment_efficiency(damage)
        super().action()
        return calculated_damage


class Armor(Equipment):

    def __init__(self, name: str, taken_capacity: int, defence: int):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=defence,
                           min_val=1,
                           max_val=10,
                           message=armor_data_messages.get("defense_error_message"))
        self.defence = defence

    def action(self) -> int or float:
        calculated_defence = self.calculate_equipment_efficiency(self.defence)
        super().action()
        return calculated_defence

    def __str__(self) -> None:
        super().__str__()
        print(armor_data_messages.get("info_message").format(self.defence))


class Navigator(Equipment):

    def __init__(self, name: str, taken_capacity: int, accuracy: int):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=accuracy,
                           min_val=5,
                           max_val=40,
                           message=navigator_data_messages.get("accuracy_error_message"))
        self.accuracy = accuracy

    def action(self) -> int or float:
        electromagnetic_surge_probability = randint(1, 100)
        if electromagnetic_surge_probability <= 20:
            self.accuracy /= 2
        calculated_accuracy = self.calculate_equipment_efficiency(self.accuracy)
        return calculated_accuracy

    def __str__(self) -> None:
        super().__str__()
        print(navigator_data_messages.get("info_message").format(self.accuracy))