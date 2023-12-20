from random import randint
from typing import Union

from equipments_classes import Armor, Weapon, Navigator, Damage, HealingDrone
from helpers.custom_exceptions import FreeSlotError, TotalVolumeError, EquipmentWornOutError
from helpers.info_messages import spaceship_data_messages, \
    spaceship_characteristic_message, \
    spaceship_actions, \
    EQUIPMENT_WORN_OUT_MESSAGE
from helpers.secondary_functions import validate_attribute, display
from helpers.variables import ship_health_values, \
    ship_spaciousness_values, \
    ship_accuracy_values, \
    ship_armor_slot_values, \
    ship_weapon_slot_values, \
    ship_navigation_slot_values, \
    ship_drone_slot_values, \
    WEAPON_EQUIPMENT_TYPE, \
    NAVIGATOR_EQUIPMENT_TYPE, \
    ARMOR_EQUIPMENT_TYPE


class Spaceship:
    def __init__(self, name: str,
                 spaciousness: int,
                 accuracy: int,
                 slot_for_armor: list or None = None,
                 slot_for_weapons: list or None = None,
                 slot_for_navigation_devices: list or None = None,
                 slot_for_healing_drones: list or None = None) -> None:
        parameters = [spaciousness,
                      accuracy,
                      slot_for_armor,
                      slot_for_weapons,
                      slot_for_navigation_devices,
                      slot_for_healing_drones]
        self.validator(args=parameters)
        self.name = name
        self.spaciousness = spaciousness
        self.accuracy = accuracy
        self.health = ship_health_values.get("max_val")
        self.slot_for_armor = slot_for_armor if slot_for_armor else []
        self.slot_for_weapons = slot_for_weapons if slot_for_weapons else []
        self.slot_for_navigation_devices = slot_for_navigation_devices if slot_for_navigation_devices else []
        self.slot_for_healing_drones = slot_for_healing_drones if slot_for_healing_drones else []
        self.defence = self.calculate_defence_value() if self.slot_for_armor else 0
        self.spaceship_set_equipment_false_info = []

    @staticmethod
    def validator(args: list) -> None:
        spaciousness, \
            accuracy, \
            slot_for_armor, \
            slot_for_weapons, \
            slot_for_navigation_devices, \
            slot_for_healing_drones = args[0], args[1], args[2], args[3], args[4], args[5]
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
        if slot_for_healing_drones:
            validate_attribute(attribute=slot_for_healing_drones,
                               min_val=ship_drone_slot_values.get("min_qty"),
                               max_val=ship_drone_slot_values.get("max_qty"),
                               message=spaceship_data_messages.get("drone_slot_error_message"))

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

    def set_healing_drones(self, drone_object: HealingDrone) -> None:
        if len(self.slot_for_healing_drones) == ship_drone_slot_values.get("max_qty"):
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=drone_object)
        self.slot_for_healing_drones.append(drone_object)

    def check_spaceship_capacity(self, equipment: Union[Armor, Weapon, Navigator, HealingDrone]) -> None:
        if sum([self.get_total_occupied_volume_of_equipment(), equipment.taken_capacity]) >= self.spaciousness:
            raise TotalVolumeError()

    def get_total_occupied_volume_of_equipment(self) -> int or float:
        armors_taken_capacity_amount = sum([armor.taken_capacity for armor in self.slot_for_armor])
        weapons_taken_capacity_amount = sum([weapon.taken_capacity for weapon in self.slot_for_weapons])
        navigation_devices_taken_capacity_amount = sum(
            [navigation_device.taken_capacity for navigation_device in self.slot_for_navigation_devices])
        healing_drones_taken_capacity_amount = sum(
            [drone.taken_capacity for drone in self.slot_for_healing_drones])
        return sum(
            [armors_taken_capacity_amount,
             weapons_taken_capacity_amount,
             navigation_devices_taken_capacity_amount,
             healing_drones_taken_capacity_amount])

    def attack(self, ship_of_attack) -> None:
        for weapon in self.slot_for_weapons:
            if not isinstance(weapon, bool):
                display(spaceship_actions.get("set_navigation") % self.name)
                accuracy_amount = self.accuracy + self.get_navigation_devices_accuracy_amount()
                hit_probability = randint(1, 100)
                if hit_probability >= accuracy_amount:
                    display(spaceship_actions.get("is_shooting") % (self.name, weapon.name, weapon.weapon_type))
                    damage_obj = self.get_equipment_action_data(equipment=weapon,
                                                                message=EQUIPMENT_WORN_OUT_MESSAGE.format(weapon.name,
                                                                                                          WEAPON_EQUIPMENT_TYPE))
                    if isinstance(damage_obj, Damage):
                        ship_of_attack.defend(damage_obj=damage_obj)
                else:
                    display(spaceship_actions.get("set_navigation_false"))

    def get_navigation_devices_accuracy_amount(self) -> int or float:
        return sum(
            [self.get_equipment_action_data(equipment=navigation_device,
                                            message=EQUIPMENT_WORN_OUT_MESSAGE.format(navigation_device.name,
                                                                                      NAVIGATOR_EQUIPMENT_TYPE))
             for navigation_device in self.slot_for_navigation_devices])

    def defend(self, damage_obj: Damage) -> None:
        damage, damage_type = damage_obj.damage, damage_obj.dmg_type
        defence_amount = self.defence + self.get_armor_defence_amount(dmg_type=damage_type)
        if defence_amount < damage:
            self.health -= (damage - defence_amount)

    def get_armor_defence_amount(self, dmg_type: str) -> int or float:
        amount = 0
        for armor in self.slot_for_armor:
            if armor.armor_type == dmg_type:
                display(spaceship_actions.get("uses_armor") % (self.name, armor.name, armor.armor_type))
                armor_action_data = self.get_equipment_action_data(equipment=armor,
                                                                   message=EQUIPMENT_WORN_OUT_MESSAGE.format(armor.name,
                                                                                                             ARMOR_EQUIPMENT_TYPE))
                amount += armor_action_data
                break
        else:
            display(spaceship_actions.get("uses_basic_armor") % self.name)
        return amount

    def __str__(self) -> str:
        ship_characteristics = spaceship_characteristic_message % (self.name,
                                                                   self.spaciousness,
                                                                   self.accuracy,
                                                                   round(self.health),
                                                                   self.defence)
        return ship_characteristics

    def get_equipment_action_data(self, equipment: Union[Armor, Weapon, Navigator],
                                  message: str) -> int or float or Damage:
        response = 0
        try:
            response = equipment.action()
        except EquipmentWornOutError:
            display(message)
            if isinstance(equipment, Weapon):
                self.slot_for_weapons.remove(equipment)
                self.slot_for_weapons.append(False)
        return response
