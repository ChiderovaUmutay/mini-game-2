from helpers.variables import drone_efficiency_values, \
    taken_capacity_values, \
    weapon_damage_values, \
    weapon_critical_hit_values, \
    armor_defence_values, \
    navigator_accuracy_values, \
    ship_spaciousness_values, \
    ship_accuracy_values, \
    ship_armor_slot_values, \
    ship_weapon_slot_values, \
    ship_navigation_slot_values, \
    ship_drone_slot_values

equipment_data_messages = {
    "taken_capacity_error_message": f"The number of units of occupied volume should be from "
                                    f"{taken_capacity_values.get('min_val')} to {taken_capacity_values.get('max_val')}",
    "info_message": "\nEquipment name: {}\n"
                    "Wear condition of equipment: {}\n"
                    "Taken capacity of equipment: {}\n"
}

weapon_data_messages = {
    "min_damage_error_message": f"The number of units of minimum damage should be from "
                                f"{weapon_damage_values.get('min_val')} to {weapon_damage_values.get('max_val')}",
    "critical_hit_chance_error_message": f"The number of units of critical chance should be from "
                                         f"{weapon_critical_hit_values.get('min_val')} to {weapon_critical_hit_values.get('max_val')}",
    "info_message": 'The weapon type is "{}"\n'
                    "The number of weapon minimum damage units: {}\n"
                    "The number of weapon maximum damage units: {}\n"
                    "The number of weapon critical hit chance units: {}\n"
}

armor_data_messages = {
    "defense_error_message": f"The range of the number of defence units should be from "
                             f"{armor_defence_values.get('min_val')} to {armor_defence_values.get('max_val')}",
    "info_message": 'The armor type is "{}"\n'
                    "The number of armor protection units: {}\n"
}

navigator_data_messages = {
    "accuracy_error_message": f"The range of the number of accuracy units should be from "
                              f"{navigator_accuracy_values.get('min_val')} to {navigator_accuracy_values.get('max_val')}",
    "info_message": "The number of navigator accuracy units: {}\n"
}

drone_data_messages = {
    "efficiency_error_message": f"The range of the number of efficiency units should be from "
                                f"{drone_efficiency_values.get('min_val')} to {drone_efficiency_values.get('max_val')}",
    "info_message": "The number of drone efficiency units: {}\n"
}

spaceship_data_messages = {
    "spaciousness_error_message": f"The range of number of spaceship spaciousness units should be from "
                                  f"{ship_spaciousness_values.get('min_val')} to {ship_spaciousness_values.get('max_val')}",
    "accuracy_error_message": f"The range of the number of spaceship accuracy units must be from "
                              f"{ship_accuracy_values.get('min_val')} to {ship_accuracy_values.get('max_val')}",
    "armor_slot_error_message": f"The number of slots for the spaceship's hinged armor should be from "
                                f"{ship_armor_slot_values.get('min_qty')} to {ship_armor_slot_values.get('max_qty')}",
    "weapon_slot_error_message": f"The number of weapon slots for a spaceship should be from"
                                 f"{ship_weapon_slot_values.get('min_qty')} to {ship_weapon_slot_values.get('max_qty')}",
    "navigation_slot_error_message": f"The number of slots for navigation devices for a spaceship should be from "
                                     f"{ship_navigation_slot_values.get('min_qty')} to {ship_navigation_slot_values.get('max_qty')}",
    "drone_slot_error_message": f"The number of slots for healing drones for a spaceship should be from "
                                f"{ship_drone_slot_values.get('min_qty')} to {ship_drone_slot_values.get('max_qty')}"
}

equipment_header_characteristic = {
    "weapon": "\n🔫 Weapon 🔫\n",
    "armor": "\n🛡 Armor 🛡\n",
    "navigator": "\n🧭 Navigator 🧭\n",
    "drone": "\n⛑ Drone ⛑\n"
}

spaceship_actions = {
    "set_navigation": f'{"-" * 5}ACTION{"-" * 5}\n\n%s spaceship sets navigation device 🧭\n',
    "set_navigation_false": '⚠⚠⚠ Failed to set up navigation ⚠⚠⚠\n',
    "is_shooting": f'{"-" * 5}ACTION{"-" * 5}\n\n%s spaceship fires weapon "%s", which type is "%s" 🚀',
    "uses_armor": f'{"-" * 5}ACTION{"-" * 5}\n\n%s spaceship is uses armor "%s", which type is "%s" 🛡\n',
    "uses_basic_armor": f'{"-" * 5}ACTION{"-" * 5}\n\n%s spaceship has used basic armor 🛡\n',
    "uses_healing_drone": f'%s spaceship is uses healing drones ⛑\n',
}

spaceship_shooting_result = {
    "critical_hit": "\nCRITICAL HIT💥 CRITICAL HIT💥 CRITICAL HIT💥\n",
    "miss": "\nMISS 👎\n",
    "hit": "\nHIT💥 HIT💥 HIT💥\n"
}

spaceship_characteristic_message = f"{'~' * 10}🚀 %s 🚀{'~' * 10}\n" \
                                   "\nSpaceship spaciousness: %s\n" \
                                   "Spaceship accuracy: %s\n" \
                                   "Spaceship health: %s\n" \
                                   "Spaceship defence: %s\n"

EQUIPMENT_CREATION_HEADER = f"{'=' * 20}🛠 Equipments creation 🛠{'=' * 20}\n"
EQUIPMENT_BATCH_HEADER = f"{'~' * 10}%s batch of equipment{'~' * 10}\n"
EQUIPMENT_WORN_OUT_MESSAGE = '\n⚠⚠⚠ "{}" {} is worn out ⚠⚠⚠\n'

SPACESHIP_CREATION_HEADER = f"{'=' * 20}🛠 Spaceships creation 🛠{'=' * 20}\n"
SPACESHIP_EQUIPMENTS_LIST_HEADER = f"{'^' * 5} EQUIPMENTS {'^' * 5}\n"
SPACESHIP_SET_EQUIPMENTS_FALSE_HEADER = f"{'^' * 5} Equipments those doesn't fit {'^' * 5}\n"
SPACESHIP_SET_EQUIPMENTS_FALSE_MESSAGE = 'There is no free space left on the "{}" ship for this "{}" {}\n'
SPACESHIP_HEALTH_INFO = f"{'-' * 5}ATTACK RESULTS{'-' * 5}\n\n" \
                        "{} spaceship health: {} 💊💊💊\n"

GAME_START_MESSAGE = f"{'-' * 7}🕹💥🚀 THE GAME HAS BEGUN 🕹💥🚀{'-' * 7}\n"
GAME_ROUND_INFO_MESSAGE = f"\n{'=' * 20}Round #%s{'=' * 20}\n"
SPACESHIP_MOVE_MESSAGE = f"{'*' * 13} %s move {'*' * 13}\n"
GAME_RESULTS_MESSAGE = f"{'=' * 23}GAME RESULTS{'=' * 23}\n\n" \
                       f"%s spaceship health: %s\n" \
                       f"%s spaceship health: %s\n\n" \
                       f"{'=' * 19}" + "%s WON🏅" + f"{'=' * 19}\n"

INPUT_MESSAGE = "\n🕹 Let's play again (y/n)?\n"
FAREWELL_MESSAGE = "\nThe game has stopped.\nGood luck👋🏻"
