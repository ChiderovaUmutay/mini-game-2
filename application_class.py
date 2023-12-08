from random import choice, randint

from equipments_classes import Weapon, Armor, Navigator
from helpers.custom_exceptions import TotalVolumeError
from helpers.variables import taken_capacity_values, \
    weapon_damage_values, \
    weapon_critical_hit_values, \
    armor_defence_values, \
    navigator_accuracy_values, \
    list_of_weapon_names, \
    list_of_armor_names, \
    list_of_navigation_names, \
    name_of_the_first_ship, \
    name_of_the_second_ship, \
    ship_spaciousness_values, \
    ship_accuracy_values, \
    ship_weapon_slot_values, \
    ship_armor_slot_values, \
    ship_navigation_slot_values, \
    WEAPON_EQUIPMENT_TYPE, \
    ARMOR_EQUIPMENT_TYPE, \
    NAVIGATOR_EQUIPMENT_TYPE
from spaceship_class import Spaceship


class Application:
    def __init__(self):
        self.weapons = []
        self.armors = []
        self.navigation_devices = []
        self.spaceship_1 = None
        self.spaceship_2 = None

    def create_equipments(self):
        list_of_weapon_names_copy = list_of_weapon_names.copy()
        list_of_armor_names_copy = list_of_armor_names.copy()
        list_of_navigation_devices_names_copy = list_of_navigation_names.copy()
        for _ in range(1, 21):
            list_of_weapon_names_copy = self.create_weapon(names_list=list_of_weapon_names_copy)
            list_of_armor_names_copy = self.create_armor(names_list=list_of_armor_names_copy)
            list_of_navigation_devices_names_copy = self.create_navigation(
                names_list=list_of_navigation_devices_names_copy)

    def create_weapon(self, names_list):
        weapon_name = choice(names_list)
        names_list.remove(weapon_name)
        taken_capacity = self.get_taken_capacity_random_value()
        min_damage = self.get_equipment_parameter_random_value(weapon_damage_values)
        critical_hit_chance = self.get_equipment_parameter_random_value(weapon_critical_hit_values)
        weapon = Weapon(name=weapon_name,
                        taken_capacity=taken_capacity,
                        min_damage=min_damage,
                        critical_hit_chance=critical_hit_chance)
        self.weapons.append(weapon)
        return names_list

    def create_armor(self, names_list):
        armor_name = choice(names_list)
        names_list.remove(armor_name)
        taken_capacity = self.get_taken_capacity_random_value()
        defence = self.get_equipment_parameter_random_value(armor_defence_values)
        armor = Armor(name=armor_name, taken_capacity=taken_capacity, defence=defence)
        self.armors.append(armor)
        return names_list

    def create_navigation(self, names_list):
        navigation_name = choice(names_list)
        names_list.remove(navigation_name)
        taken_capacity = self.get_taken_capacity_random_value()
        accuracy = self.get_equipment_parameter_random_value(navigator_accuracy_values)
        navigation = Navigator(name=navigation_name, taken_capacity=taken_capacity, accuracy=accuracy)
        self.navigation_devices.append(navigation)
        return names_list

    @staticmethod
    def get_taken_capacity_random_value():
        return randint(taken_capacity_values.get("min_val"), taken_capacity_values.get("max_val"))

    @staticmethod
    def get_equipment_parameter_random_value(parameter_values_dict):
        return randint(parameter_values_dict.get("min_val"), parameter_values_dict.get("max_val"))

    def create_spaceships(self):
        self.spaceship_1 = self.create_spaceship_object(name_of_the_first_ship)
        self.spaceship_2 = self.create_spaceship_object(name_of_the_second_ship)
        self.set_equipments(self.spaceship_1)
        self.set_equipments(self.spaceship_2)
        self.spaceship_1.__str__()
        self.spaceship_2.__str__()

    def create_spaceship_object(self, spaceship_name):
        spaciousness = self.get_equipment_parameter_random_value(ship_spaciousness_values)
        accuracy = self.get_equipment_parameter_random_value(ship_accuracy_values)
        return Spaceship(name=spaceship_name,
                         spaciousness=spaciousness,
                         accuracy=accuracy)

    def set_equipments(self, spaceship):
        equipment_types = [WEAPON_EQUIPMENT_TYPE, ARMOR_EQUIPMENT_TYPE, NAVIGATOR_EQUIPMENT_TYPE]
        for equipment_type in equipment_types:
            self.call_spaceship_set_method(spaceship=spaceship, equipment_type=equipment_type)

    def call_spaceship_set_method(self, spaceship, equipment_type):
        equipment_slot_values, equipment_dataset, set_method = self.get_equipments_data_by_type(spaceship=spaceship,
                                                                                                equipment_type=equipment_type)
        for _ in range(equipment_slot_values.get("min_qty"), equipment_slot_values.get("max_qty") + 1):
            equipment = choice(equipment_dataset)
            try:
                set_method(equipment)
            except TotalVolumeError:
                print(f"There is no free space left on the ship for this {equipment.name} {equipment_type}")

    def get_equipments_data_by_type(self, spaceship, equipment_type):
        equipments_data = {
            WEAPON_EQUIPMENT_TYPE: [ship_weapon_slot_values, self.weapons, spaceship.set_weapon],
            ARMOR_EQUIPMENT_TYPE: [ship_armor_slot_values, self.armors, spaceship.set_armor],
            NAVIGATOR_EQUIPMENT_TYPE: [ship_navigation_slot_values, self.navigation_devices,
                                       spaceship.set_navigation_devices],
        }
        return equipments_data.get(equipment_type)

    def run(self):
        round_num = 0
        while round_num <= 20:
            print(f"{'=' * 15}Round #{round_num}{'=' * 15}")
            round_num += 1
            print(f"{self.spaceship_1.name} spaceship is shooting 💥\n\n")
            self.spaceship_1.attack(self.spaceship_2)
            if self.spaceship_2.health > 0:
                print(f"{self.spaceship_2.name} spaceship is shooting 💥\n\n")
                self.spaceship_2.attack(self.spaceship_1)
                if self.spaceship_1.health < 0:
                    print(f"{self.spaceship_2.name} WON!")
                    break
            else:
                print(f"{self.spaceship_1.name} WON!")
                break
        else:
            print(f"{self.spaceship_1.name} spaceship health: {round(self.spaceship_1.health)}\n"
                  f"{self.spaceship_2.name} spaceship health: {round(self.spaceship_2.health)}")
            print("Game over!!!")


if __name__ == "__main__":
    app = Application()
    app.create_equipments()
    app.create_spaceships()
    app.run()
