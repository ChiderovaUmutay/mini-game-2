from equipments_classes import Weapon, Armor, Navigator
from helpers.custom_exceptions import FreeSlotError, TotalVolumeError
from helpers.info_messages import spaceship_data_messages
from helpers.secondary_functions import validate_attribute


class Spaceship:
    def __init__(self, spaciousness, accuracy, slots_for_armor, slots_for_weapons, slot_for_navigation_devices):
        parameters = [spaciousness, accuracy, slots_for_armor, slots_for_weapons, slot_for_navigation_devices]
        self.validator(args=parameters)
        self.spaciousness = spaciousness
        self.accuracy = accuracy
        self.health = 1000
        self.slots_for_armor = slots_for_armor
        self.slots_for_weapons = slots_for_weapons
        self.slot_for_navigation_devices = slot_for_navigation_devices
        self.defence = (1 / (self.spaciousness * len(self.slots_for_armor))) * 10 ** 4

    @staticmethod
    def validator(args):
        spaciousness, \
            accuracy, \
            slots_for_armor, \
            slots_for_weapons, \
            slot_for_navigation_devices = args[0], args[1], args[2], args[3], args[4]
        validate_attribute(attribute=spaciousness,
                           min_val=300,
                           max_val=1000,
                           message=spaceship_data_messages.get("spaciousness_error_message"))
        validate_attribute(attribute=accuracy,
                           min_val=0,
                           max_val=5,
                           message=spaceship_data_messages.get("accuracy_error_message"))
        validate_attribute(attribute=slots_for_armor,
                           min_val=1,
                           max_val=3,
                           message=spaceship_data_messages.get("slots_for_armor_error_message"))
        validate_attribute(attribute=slots_for_weapons,
                           min_val=1,
                           max_val=4,
                           message=spaceship_data_messages.get("slots_for_weapons_error_message"))
        validate_attribute(attribute=slot_for_navigation_devices,
                           min_val=1,
                           max_val=2,
                           message=spaceship_data_messages.get("slot_for_navigation_devices_error_message"))

    def set_armor(self, armor_object):
        if len(self.slots_for_armor) == 3:
            raise FreeSlotError()
        self.check_spaceship_capacity(equipment=armor_object)
        self.slots_for_armor.append(armor_object)

    def check_spaceship_capacity(self, equipment):
        if sum([self.get_total_occupied_volume_of_equipment(), equipment.taken_capacity]) >= self.spaciousness:
            raise TotalVolumeError()

    def get_total_occupied_volume_of_equipment(self):
        armors_taken_capacity_amount = sum([armor.taken_capacity for armor in self.slots_for_armor])
        weapons_taken_capacity_amount = sum([weapon.taken_capacity for weapon in self.slots_for_weapons])
        navigation_devices_taken_capacity_amount = sum([navigation_device.taken_capacity for navigation_device in self.slot_for_navigation_devices])
        return sum([armors_taken_capacity_amount, weapons_taken_capacity_amount, navigation_devices_taken_capacity_amount])