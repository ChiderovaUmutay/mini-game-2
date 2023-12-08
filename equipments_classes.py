from random import uniform, randint

from helpers.custom_exceptions import EquipmentWornOutError
from helpers.info_messages import equipment_data_messages, \
    weapon_data_messages, \
    armor_data_messages, \
    navigator_data_messages
from helpers.secondary_functions import validate_attribute
from helpers.variables import taken_capacity_values, \
    wear_condition_values, \
    weapon_damage_values, \
    weapon_critical_hit_values, \
    armor_defence_values, \
    navigator_accuracy_values, \
    MISFIRE_PERCENTAGE, \
    ELECTROMAGNETIC_SURGE_PERCENTAGE


class Equipment:
    def __init__(self, name: str, taken_capacity: int) -> None:
        validate_attribute(attribute=taken_capacity,
                           min_val=taken_capacity_values.get("min_val"),
                           max_val=taken_capacity_values.get("max_val"),
                           message=equipment_data_messages.get("taken_capacity_error_message"))
        self.name = name
        self.wear_condition = wear_condition_values.get("min_val")
        self.taken_capacity = taken_capacity

    def action(self) -> None:
        if self.wear_condition >= wear_condition_values.get("max_val"):
            raise EquipmentWornOutError()
        else:
            self.wear_condition += wear_condition_values.get("increasing_val")

    def calculate_equipment_efficiency(self, equipment: int or float) -> int or float:
        calculated_efficiency = equipment - (equipment * self.wear_condition) / 100
        return calculated_efficiency

    def __str__(self) -> str:
        equipment_characteristics = f"{equipment_data_messages.get('info_message').format(self.name, self.wear_condition, self.taken_capacity)}"
        return equipment_characteristics


class Weapon(Equipment):

    def __init__(self, name: str, taken_capacity: int, min_damage: int, critical_hit_chance: int) -> None:
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=min_damage,
                           min_val=weapon_damage_values.get("min_val"),
                           max_val=weapon_damage_values.get("max_val"),
                           message=weapon_data_messages.get("min_damage_error_message"))
        validate_attribute(attribute=critical_hit_chance,
                           min_val=weapon_critical_hit_values.get("min_val"),
                           max_val=weapon_critical_hit_values.get("max_val"),
                           message=weapon_data_messages.get("critical_hit_chance_error_message"))
        self.min_damage = min_damage
        self.critical_hit_chance = critical_hit_chance
        self.max_damage = self.min_damage + (self.min_damage * 40) / 100

    def action(self) -> int or float:
        damage = round(uniform(self.min_damage, self.max_damage), 1)
        if damage <= self.critical_hit_chance:
            critical_damage = (self.max_damage * 40) / 100
            return self.get_calculated_damage(critical_damage)
        elif damage <= MISFIRE_PERCENTAGE:
            return 0
        else:
            return self.get_calculated_damage(damage)

    def __str__(self) -> str:
        weapon_characteristics = f"{super().__str__()}{weapon_data_messages.get('info_message').format(self.min_damage, self.max_damage, self.critical_hit_chance)}"
        return weapon_characteristics

    def get_calculated_damage(self, damage: int or float) -> int or float:
        calculated_damage = self.calculate_equipment_efficiency(damage)
        super().action()
        return calculated_damage


class Armor(Equipment):

    def __init__(self, name: str, taken_capacity: int, defence: int):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=defence,
                           min_val=armor_defence_values.get("min_val"),
                           max_val=armor_defence_values.get("max_val"),
                           message=armor_data_messages.get("defense_error_message"))
        self.defence = defence

    def action(self) -> int or float:
        calculated_defence = self.calculate_equipment_efficiency(self.defence)
        super().action()
        return calculated_defence

    def __str__(self) -> str:
        armor_characteristics = f"{super().__str__()}{armor_data_messages.get('info_message').format(self.defence)}"
        return armor_characteristics


class Navigator(Equipment):

    def __init__(self, name: str, taken_capacity: int, accuracy: int):
        super().__init__(name, taken_capacity)
        validate_attribute(attribute=accuracy,
                           min_val=navigator_accuracy_values.get("min_val"),
                           max_val=navigator_accuracy_values.get("max_val"),
                           message=navigator_data_messages.get("accuracy_error_message"))
        self.accuracy = accuracy

    def action(self) -> int or float:
        electromagnetic_surge_probability = randint(1, 100)
        if electromagnetic_surge_probability <= ELECTROMAGNETIC_SURGE_PERCENTAGE:
            self.accuracy /= 2
        calculated_accuracy = self.calculate_equipment_efficiency(self.accuracy)
        super().action()
        return calculated_accuracy

    def __str__(self) -> str:
        navigator_characteristics = f"{super().__str__()}{navigator_data_messages.get('info_message').format(self.accuracy)}"
        return navigator_characteristics