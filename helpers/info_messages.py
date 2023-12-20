from helpers.variables import drone_efficiency_values

equipment_data_messages = {
    "taken_capacity_error_message": "The number of units of occupied volume should be from 30 to 100",
    "info_message": "\nEquipment name: {}\n"
                    "Wear condition of equipment: {}\n"
                    "Taken capacity of equipment: {}\n"
}

weapon_data_messages = {
    "min_damage_error_message": "The number of units of minimum damage should be from 5 to 40",
    "critical_hit_chance_error_message": "The number of units of critical chance should be from 1 to 70",
    "info_message": 'The weapon type is "{}"\n'
                    "The number of weapon minimum damage units: {}\n"
                    "The number of weapon maximum damage units: {}\n"
                    "The number of weapon critical hit chance units: {}\n"
}

armor_data_messages = {
    "defense_error_message": "The range of the number of protection units should be from 1 to 10",
    "info_message": 'The armor type is "{}"\n'
                    "The number of armor protection units: {}\n"
}

navigator_data_messages = {
    "accuracy_error_message": "The range of the number of accuracy units should be from 5 to 40",
    "info_message": "The number of navigator accuracy units: {}\n"
}

drone_data_messages = {
    "efficiency_error_message": f"The range of the number of efficiency units should be from "
                                f"{drone_efficiency_values.get('min_val')} to {drone_efficiency_values.get('max_val')}",
    "info_message": "The number of drone efficiency units: {}\n"
}

spaceship_data_messages = {
    "spaciousness_error_message": "The range of number of spaceship spaciousness units should be from 300 to 1000",
    "accuracy_error_message": "The range of the number of spaceship accuracy units must be from 0 to 5",
    "armor_slot_error_message": "The number of slots for the spaceship's hinged armor should be from 1 to 3",
    "weapon_slot_error_message": "The number of weapon slots for a spaceship should be from 1 to 3",
    "navigation_slot_error_message": "The number of slots for navigation devices for a spaceship should be from 1 to 2",
    "drone_slot_error_message": "The number of slots for healing drones for a spaceship should be from 0 to 2"
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
