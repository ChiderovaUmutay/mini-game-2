from random import choice, randint

from equipments_classes import Weapon, Armor, Navigator, HealingDrone
from helpers.custom_exceptions import TotalVolumeError
from helpers.info_messages import EQUIPMENT_CREATION_HEADER, \
    EQUIPMENT_BATCH_HEADER, \
    SPACESHIP_CREATION_HEADER, \
    SPACESHIP_SET_EQUIPMENTS_FALSE_MESSAGE, \
    GAME_START_MESSAGE, \
    GAME_ROUND_INFO_MESSAGE, \
    SPACESHIP_MOVE_MESSAGE, \
    SPACESHIP_EQUIPMENTS_LIST_HEADER, \
    SPACESHIP_SET_EQUIPMENTS_FALSE_HEADER, \
    GAME_RESULTS_MESSAGE, \
    SPACESHIP_HEALTH_INFO, \
    INPUT_MESSAGE, \
    FAREWELL_MESSAGE
from helpers.secondary_functions import display
from helpers.variables import taken_capacity_values, \
    weapon_damage_values, \
    weapon_critical_hit_values, \
    armor_defence_values, \
    navigator_accuracy_values, \
    drone_efficiency_values, \
    list_of_weapon_names, \
    list_of_armor_names, \
    list_of_navigation_names, \
    list_of_drones_names, \
    name_of_the_first_ship, \
    name_of_the_second_ship, \
    ship_spaciousness_values, \
    ship_accuracy_values, \
    ship_weapon_slot_values, \
    ship_armor_slot_values, \
    ship_navigation_slot_values, \
    ship_drone_slot_values, \
    equipments_types, \
    WEAPON_EQUIPMENT_TYPE, \
    ARMOR_EQUIPMENT_TYPE, \
    NAVIGATOR_EQUIPMENT_TYPE, \
    DRONE_EQUIPMENT_TYPE
from spaceship_class import Spaceship


class Application:
    def __init__(self):
        self.weapons = []
        self.armors = []
        self.navigation_devices = []
        self.healing_drones = []
        self.spaceship_1 = None
        self.spaceship_2 = None

    def create_equipments(self):
        display(EQUIPMENT_CREATION_HEADER)
        list_of_weapon_names_copy = list_of_weapon_names.copy()
        list_of_armor_names_copy = list_of_armor_names.copy()
        list_of_navigation_names_copy = list_of_navigation_names.copy()
        list_of_healing_drones_names_copy = list_of_drones_names.copy()
        for i in range(1, 21):
            display(EQUIPMENT_BATCH_HEADER % i)
            list_of_weapon_names_copy = self.create_weapon(names_list=list_of_weapon_names_copy)
            list_of_armor_names_copy = self.create_armor(names_list=list_of_armor_names_copy)
            list_of_navigation_names_copy = self.create_navigation(names_list=list_of_navigation_names_copy)
            list_of_healing_drones_names_copy = self.create_drone(names_list=list_of_healing_drones_names_copy)

    def create_weapon(self, names_list: list) -> list:
        weapon_name = choice(names_list)
        names_list.remove(weapon_name)
        weapon_type = choice(equipments_types)
        taken_capacity = self.get_taken_capacity_random_value()
        min_damage = self.get_equipment_parameter_random_value(weapon_damage_values)
        critical_hit_chance = self.get_equipment_parameter_random_value(weapon_critical_hit_values)
        weapon = Weapon(name=weapon_name,
                        taken_capacity=taken_capacity,
                        weapon_type=weapon_type,
                        min_damage=min_damage,
                        critical_hit_chance=critical_hit_chance)
        display(weapon.__str__())
        self.weapons.append(weapon)
        return names_list

    def create_armor(self, names_list: list) -> list:
        armor_name = choice(names_list)
        names_list.remove(armor_name)
        armor_type = choice(equipments_types)
        taken_capacity = self.get_taken_capacity_random_value()
        defence = self.get_equipment_parameter_random_value(armor_defence_values)
        armor = Armor(name=armor_name, taken_capacity=taken_capacity, armor_type=armor_type, defence=defence)
        display(armor.__str__())
        self.armors.append(armor)
        return names_list

    def create_navigation(self, names_list: list) -> list:
        navigation_name = choice(names_list)
        names_list.remove(navigation_name)
        taken_capacity = self.get_taken_capacity_random_value()
        accuracy = self.get_equipment_parameter_random_value(navigator_accuracy_values)
        navigation = Navigator(name=navigation_name, taken_capacity=taken_capacity, accuracy=accuracy)
        display(navigation.__str__())
        self.navigation_devices.append(navigation)
        return names_list

    def create_drone(self, names_list: list) -> list:
        drone_name = choice(names_list)
        names_list.remove(drone_name)
        taken_capacity = self.get_taken_capacity_random_value()
        efficiency = self.get_equipment_parameter_random_value(drone_efficiency_values)
        drone = HealingDrone(name=drone_name, taken_capacity=taken_capacity, efficiency=efficiency)
        display(drone.__str__())
        self.healing_drones.append(drone)
        return names_list

    @staticmethod
    def get_taken_capacity_random_value():
        return randint(taken_capacity_values.get("min_val"), taken_capacity_values.get("max_val"))

    @staticmethod
    def get_equipment_parameter_random_value(parameter_values_dict):
        return randint(parameter_values_dict.get("min_val"), parameter_values_dict.get("max_val"))

    def create_spaceships(self):
        display(SPACESHIP_CREATION_HEADER)
        self.spaceship_1 = self.create_spaceship_object(name_of_the_first_ship)
        self.spaceship_2 = self.create_spaceship_object(name_of_the_second_ship)
        self.set_equipments(self.spaceship_1)
        self.set_equipments(self.spaceship_2)
        self.display_full_spaceship_info(self.spaceship_1)
        self.display_full_spaceship_info(self.spaceship_2)

    def create_spaceship_object(self, spaceship_name):
        spaciousness = self.get_equipment_parameter_random_value(ship_spaciousness_values)
        accuracy = self.get_equipment_parameter_random_value(ship_accuracy_values)
        return Spaceship(name=spaceship_name,
                         spaciousness=spaciousness,
                         accuracy=accuracy)

    def set_equipments(self, spaceship):
        equipment_types = [WEAPON_EQUIPMENT_TYPE, ARMOR_EQUIPMENT_TYPE, NAVIGATOR_EQUIPMENT_TYPE, DRONE_EQUIPMENT_TYPE]
        for equipment_type in equipment_types:
            self.call_spaceship_set_method(spaceship=spaceship, equipment_type=equipment_type)

    def call_spaceship_set_method(self, spaceship, equipment_type):
        equipment_slot_values, equipment_dataset, set_method = self.get_equipments_data_by_type(spaceship=spaceship,
                                                                                                equipment_type=equipment_type)
        for _ in range(equipment_slot_values.get("min_qty"),
                       equipment_slot_values.get("max_qty") + (1 if equipment_type != DRONE_EQUIPMENT_TYPE else 0)):
            equipment = choice(equipment_dataset)
            try:
                set_method(equipment)
                equipment_index = equipment_dataset.index(equipment)
                equipment_dataset.pop(equipment_index)
            except TotalVolumeError:
                spaceship.spaceship_set_equipment_false_info.append(
                    SPACESHIP_SET_EQUIPMENTS_FALSE_MESSAGE.format(spaceship.name,
                                                                  equipment.name,
                                                                  equipment_type))

    def get_equipments_data_by_type(self, spaceship, equipment_type):
        equipments_data = {
            WEAPON_EQUIPMENT_TYPE: [ship_weapon_slot_values, self.weapons, spaceship.set_weapon],
            ARMOR_EQUIPMENT_TYPE: [ship_armor_slot_values, self.armors, spaceship.set_armor],
            NAVIGATOR_EQUIPMENT_TYPE: [ship_navigation_slot_values, self.navigation_devices,
                                       spaceship.set_navigation_devices],
            DRONE_EQUIPMENT_TYPE: [ship_drone_slot_values, self.healing_drones, spaceship.set_healing_drones]
        }
        return equipments_data.get(equipment_type)

    def display_full_spaceship_info(self, spaceship) -> None:
        ship_weapons_characteristics = self.get_equipment_characteristics(slot_data=spaceship.slot_for_weapons)
        ship_armors_characteristics = self.get_equipment_characteristics(slot_data=spaceship.slot_for_armor)
        ship_navigations_characteristics = self.get_equipment_characteristics(
            slot_data=spaceship.slot_for_navigation_devices)
        ship_drones_characteristics = self.get_equipment_characteristics(slot_data=spaceship.slot_for_healing_drones)
        message_info = f"{spaceship.__str__()}\n" \
                       f"{SPACESHIP_EQUIPMENTS_LIST_HEADER}\n" \
                       f"{ship_weapons_characteristics}\n" \
                       f"{ship_armors_characteristics}\n" \
                       f"{ship_navigations_characteristics}\n" \
                       f"{ship_drones_characteristics}\n"
        if spaceship.spaceship_set_equipment_false_info:
            equipment_dont_set_on_ship_data = self.get_didnt_fit_equipments_info(
                spaceship.spaceship_set_equipment_false_info)
            message_info += f"{SPACESHIP_SET_EQUIPMENTS_FALSE_HEADER}{equipment_dont_set_on_ship_data}"
        message_info += f"{'~' * (len(spaceship.name) + 28)}\n\n"
        display(message_info)

    @staticmethod
    def get_equipment_characteristics(slot_data: list) -> str:
        equipments_characteristics = ""
        for equipment in slot_data:
            equipments_characteristics += equipment.__str__()
        return equipments_characteristics

    @staticmethod
    def get_didnt_fit_equipments_info(message_data):
        didnt_fit_equipments_info = ""
        for message in message_data:
            didnt_fit_equipments_info += message
        return didnt_fit_equipments_info

    def run(self) -> None:
        round_num = 0
        display(GAME_START_MESSAGE)
        while round_num <= 20:
            round_num += 1
            display(GAME_ROUND_INFO_MESSAGE % round_num)
            display(SPACESHIP_MOVE_MESSAGE % self.spaceship_1.name)
            self.spaceship_1.attack(self.spaceship_2)
            display(SPACESHIP_HEALTH_INFO.format(self.spaceship_2.name, round(self.spaceship_2.health)))
            if self.spaceship_2.health > 0:
                display(SPACESHIP_MOVE_MESSAGE % self.spaceship_2.name)
                self.spaceship_2.attack(self.spaceship_1)
                display(SPACESHIP_HEALTH_INFO.format(self.spaceship_1.name, round(self.spaceship_1.health)))
            if (self.spaceship_1.health <= 0 or self.spaceship_2.health <= 0) or (
                    not any(self.spaceship_1.slot_for_weapons) and not any(self.spaceship_2.slot_for_weapons)):
                self.display_game_results()
                break

    def display_game_results(self):
        winner = self.spaceship_1.name if self.spaceship_1.health > self.spaceship_2.health else self.spaceship_2.name
        game_over_message = GAME_RESULTS_MESSAGE % (self.spaceship_1.name, round(self.spaceship_1.health),
                                                    self.spaceship_2.name, round(self.spaceship_2.health),
                                                    winner)
        display(game_over_message)


def create_app_object():
    app_obj = Application()
    app_obj.create_equipments()
    app_obj.create_spaceships()
    return app_obj


if __name__ == "__main__":
    app = create_app_object()
    # app.run()
    # try:
    #     while True:
    #         response = input(INPUT_MESSAGE)
    #         if response != "y":
    #             display(FAREWELL_MESSAGE)
    #             break
    #         app = create_app_object()
    #         app.run()
    # except KeyboardInterrupt:
    #     display(FAREWELL_MESSAGE)
