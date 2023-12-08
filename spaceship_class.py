from random import randint
from typing import Union

from equipments_classes import Armor, Weapon, Navigator
from helpers.custom_exceptions import FreeSlotError, TotalVolumeError, EquipmentWornOutError
from helpers.info_messages import spaceship_data_messages, \
    spaceship_characteristic_message, \
    SPACESHIP_EQUIPMENTS_LIST_HEADER
from helpers.secondary_functions import validate_attribute, display
from helpers.variables import ship_health_values, \
    ship_spaciousness_values, \
    ship_accuracy_values, \
    ship_armor_slot_values, \
    ship_weapon_slot_values, \
    ship_navigation_slot_values, \
    wear_condition_values


class Spaceship:
    def __init__(self, name: str,
                 spaciousness: int,
                 accuracy: int,
                 slot_for_armor: list or None = None,
                 slot_for_weapons: list or None =None,
                 slot_for_navigation_devices: list or None =None) -> None:
        parameters = [spaciousness, accuracy, slot_for_armor, slot_for_weapons, slot_for_navigation_devices]
        self.validator(args=parameters)
        self.name = name
        self.spaciousness = spaciousness
        self.accuracy = accuracy
        self.health = ship_health_values.get("max_val")
        self.slot_for_armor = [] if slot_for_armor is None else slot_for_weapons
        self.slot_for_weapons = [] if slot_for_weapons is None else slot_for_weapons
        self.slot_for_navigation_devices = [] if slot_for_navigation_devices is None else slot_for_navigation_devices
        self.defence = self.calculate_defence_value() if self.slot_for_armor else 0
        self.spaceship_set_equipment_false_info = []
    @staticmethod
    def validator(args: list) -> None:
        spaciousness, \
            accuracy, \
            slot_for_armor, \
            slot_for_weapons, \
            slot_for_navigation_devices = args[0], args[1], args[2], args[3], args[4]
        validate_attribute(attribute=spaciousness,
                           min_val=ship_spaciousness_values.get("min_val"),
                           max_val=ship_spaciousness_values.get("max_val"),
                           message=spaceship_data_messages.get("spaciousness_error_message"))
        validate_attribute(attribute=accuracy,
                           min_val=ship_accuracy_values.get("min_val"),
                           max_val=ship_accuracy_values.get("max_val"),
                           message=spaceship_data_messages.get("accuracy_error_message"))
        if slot_for_armor:
            validate_attribute(attribute=slot_for_armor,
                               min_val=ship_armor_slot_values.get("min_qty"),
                               max_val=ship_armor_slot_values.get("max_qty"),
                               message=spaceship_data_messages.get("armor_slot_error_message"))
        if slot_for_weapons:
            validate_attribute(attribute=slot_for_weapons,
                               min_val=ship_weapon_slot_values.get("min_qty"),
                               max_val=ship_weapon_slot_values.get("max_qty"),
                               message=spaceship_data_messages.get("weapon_slot_error_message"))
        if slot_for_navigation_devices:
            validate_attribute(attribute=slot_for_navigation_devices,
                               min_val=ship_navigation_slot_values.get("min_qty"),
                               max_val=ship_navigation_slot_values.get("max_qty"),
                               message=spaceship_data_messages.get("navigation_slot_error_message"))

    def calculate_defence_value(self) -> int or float:
        return (1 / (self.spaciousness * len(self.slot_for_armor))) * 10 ** 4

    def set_armor(self, armor_object: Armor) -> None:
        if len(self.slot_for_armor) == ship_armor_slot_values.get("max_qty"):
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=armor_object)
        self.slot_for_armor.append(armor_object)

    def set_weapon(self, weapon_object: Weapon) -> None:
        if len(self.slot_for_weapons) == ship_weapon_slot_values.get("max_qty"):
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=weapon_object)
        self.slot_for_weapons.append(weapon_object)

    def set_navigation_devices(self, navigation_object: Navigator) -> None:
        if len(self.slot_for_navigation_devices) == ship_navigation_slot_values.get("max_qty"):
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=navigation_object)
        self.slot_for_navigation_devices.append(navigation_object)

    def check_spaceship_capacity(self, equipment: Union[Armor, Weapon, Navigator]) -> None:
        if sum([self.get_total_occupied_volume_of_equipment(), equipment.taken_capacity]) >= self.spaciousness:
            raise TotalVolumeError()

    def get_total_occupied_volume_of_equipment(self) -> int or float:
        armors_taken_capacity_amount = sum([armor.taken_capacity for armor in self.slot_for_armor])
        weapons_taken_capacity_amount = sum([weapon.taken_capacity for weapon in self.slot_for_weapons])
        navigation_devices_taken_capacity_amount = sum(
            [navigation_device.taken_capacity for navigation_device in self.slot_for_navigation_devices])
        return sum(
            [armors_taken_capacity_amount, weapons_taken_capacity_amount, navigation_devices_taken_capacity_amount])

    def attack(self, ship_of_attack) -> None:
        for weapon in self.slot_for_weapons:
            if weapon.wear_condition < wear_condition_values.get("max_val"):
                accuracy_amount = self.accuracy + self.get_navigation_devices_accuracy_amount()
                hit_probability = randint(1, 100)
                if hit_probability >= accuracy_amount:
                    damage = self.get_equipment_action_data(equipment=weapon, message="Weapon equipment is worn out")
                    ship_of_attack.defend(damage)
                continue
        else:
            print("All weapons are worn out")

    def get_navigation_devices_accuracy_amount(self) -> int or float:
        return sum(
            [self.get_equipment_action_data(equipment=navigation_device, message="Navigation equipment is worn out")
             for navigation_device in self.slot_for_navigation_devices])

    def defend(self, damage: int or float) -> None:
        defence_amount = self.defence + self.get_armor_defence_amount()
        if defence_amount < damage:
            self.health -= (damage - defence_amount)

    def get_armor_defence_amount(self) -> int or float:
        return sum([self.get_equipment_action_data(equipment=armor, message="Armor equipment is worn out")
                    for armor in self.slot_for_armor])

    @staticmethod
    def get_equipment_action_data(equipment: Union[Armor, Weapon, Navigator], message: str) -> int or float or None:
        response = 0
        try:
            response = equipment.action()
        except EquipmentWornOutError:
            print(message)
        return response

    def __str__(self) -> None:
        ship_characteristics = spaceship_characteristic_message % (self.name,
                                                                   self.spaciousness,
                                                                   self.accuracy,
                                                                   self.health,
                                                                   self.defence)
        ship_weapons_characteristics = self.get_equipment_characteristics(slot_data=self.slot_for_weapons)
        ship_armors_characteristics = self.get_equipment_characteristics(slot_data=self.slot_for_armor)
        ship_navigations_characteristics = self.get_equipment_characteristics(slot_data=self.slot_for_navigation_devices)
        equipment_dont_set_on_ship_data = self.get_didnt_fit_equipments_info(self.spaceship_set_equipment_false_info)\
            if self.spaceship_set_equipment_false_info else None
        display(f"{ship_characteristics}\n"
                f"{SPACESHIP_EQUIPMENTS_LIST_HEADER}\n"
                f"{ship_weapons_characteristics}\n"
                f"{ship_armors_characteristics}\n"
                f"{ship_navigations_characteristics}\n"
                f"{'~' * (len(self.name) + 28)}\n\n")

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