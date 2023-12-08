equipment_data_messages = {
    "taken_capacity_error_message": "The number of units of occupied volume should be from 30 to 100",
    "info_message": "\nEquipment name: {}\n"
                    "Wear condition of equipment: {}\n"
                    "Taken capacity of equipment: {}\n"
}

weapon_data_messages = {
    "min_damage_error_message": "The number of units of minimum damage should be from 5 to 40",
    "critical_hit_chance_error_message": "The number of units of critical chance should be from 1 to 70",
    "info_message": "The number of weapon minimum damage units: {}\n"
                    "The number of weapon maximum damage units: {}\n"
                    "The number of weapon critical hit chance units: {}\n"
}

armor_data_messages = {
    "defense_error_message": "The range of the number of protection units should be from 1 to 10",
    "info_message": "The number of armor protection units: {}\n"
}

navigator_data_messages = {
    "accuracy_error_message": "The range of the number of accuracy units should be from 5 to 40",
    "info_message": "The number of navigator accuracy units: {}\n"
}

spaceship_data_messages = {
    "spaciousness_error_message": "The range of number of spaceship spaciousness units should be from 300 to 1000",
    "accuracy_error_message": "The range of the number of spaceship accuracy units must be from 0 to 5",
    "armor_slot_error_message": "The number of slots for the spaceship's hinged armor should be from 1 to 3",
    "weapon_slot_error_message": "The number of weapon slots for a spaceship should be from 1 to 3",
    "navigation_slot_error_message": "The number of slots for navigation devices for a spaceship should be from 1 to 2"
}

EQUIPMENT_CREATION_HEADER = f"{'=' * 20}🛠 Equipment creation 🛠{'=' * 20}\n"
EQUIPMENT_BATCH_HEADER = f"{'~' * 10}%s batch of equipment{'~' * 10}\n"

equipment_header_characteristic = {
    "weapon": "🚀 Weapon 🚀\n",
    "armor": "🛡 Armor 🛡\n",
    "navigator": "🧭 Navigator 🧭\n"
}