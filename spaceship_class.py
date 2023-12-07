from helpers.custom_exceptions import FreeSlotError, TotalVolumeError
from helpers.info_messages import spaceship_data_messages
from helpers.secondary_functions import validate_attribute
from helpers.variables import ship_health_values, ship_spaciousness_values, ship_accuracy_values, \
    ship_armor_slot_values, ship_weapon_slot_values, ship_navigation_slot_values


class Spaceship:
    def __init__(self, spaciousness, accuracy, slot_for_armor, slot_for_weapons, slot_for_navigation_devices):
        parameters = [spaciousness, accuracy, slot_for_armor, slot_for_weapons, slot_for_navigation_devices]
        self.validator(args=parameters)
        self.spaciousness = spaciousness
        self.accuracy = accuracy
        self.health = ship_health_values.get("max_val")
        self.slot_for_armor = slot_for_armor
        self.slot_for_weapons = slot_for_weapons
        self.slot_for_navigation_devices = slot_for_navigation_devices
        self.defence = (1 / (self.spaciousness * len(self.slot_for_armor))) * 10 ** 4

    @staticmethod
    def validator(args):
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
        validate_attribute(attribute=slot_for_armor,
                           min_val=ship_armor_slot_values.get("min_qty"),
                           max_val=ship_armor_slot_values.get("max_qty"),
                           message=spaceship_data_messages.get("armor_slot_error_message"))
        validate_attribute(attribute=slot_for_weapons,
                           min_val=ship_weapon_slot_values.get("min_qty"),
                           max_val=ship_weapon_slot_values.get("max_qty"),
                           message=spaceship_data_messages.get("weapon_slot_error_message"))
        validate_attribute(attribute=slot_for_navigation_devices,
                           min_val=ship_navigation_slot_values.get("min_qty"),
                           max_val=ship_navigation_slot_values.get("max_qty"),
                           message=spaceship_data_messages.get("navigation_slot_error_message"))

    def set_armor(self, armor_object):
        if len(self.slot_for_armor) == ship_armor_slot_values.get("max_qty"):
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=armor_object)
        self.slot_for_armor.append(armor_object)

    def check_spaceship_capacity(self, equipment):
        if sum([self.get_total_occupied_volume_of_equipment(), equipment.taken_capacity]) >= self.spaciousness:
            raise TotalVolumeError()

    def get_total_occupied_volume_of_equipment(self):
        armors_taken_capacity_amount = sum([armor.taken_capacity for armor in self.slot_for_armor])
        weapons_taken_capacity_amount = sum([weapon.taken_capacity for weapon in self.slot_for_weapons])
        navigation_devices_taken_capacity_amount = sum([navigation_device.taken_capacity for navigation_device in self.slot_for_navigation_devices])
        return sum([armors_taken_capacity_amount, weapons_taken_capacity_amount, navigation_devices_taken_capacity_amount])