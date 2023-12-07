class EquipmentWornOutError(Exception):
    pass


class Equipment:
    def __init__(self, name, taken_capacity, wear_condition=0):
        self.validate_attribute(attribute=taken_capacity,
                                 min_val=30,
                                 max_val=100,
                                 message="The range of occupied volume should be from 30 to 100")
        self.name = name
        self.wear_condition = wear_condition
        self.taken_capacity = taken_capacity

    @staticmethod
    def validate_attribute(attribute, min_val, max_val, message):
        bool_val = min_val <= attribute <= max_val
        if bool_val is False:
            raise ValueError(message)

    def action(self):
        if self.wear_condition >= 100:
            raise EquipmentWornOutError()
        else:
            self.wear_condition += 10

    def calculate_damage_taking_into_account_wear(self, damage):
        calculated_damage = damage - (damage * self.wear_condition) / 100
        return round(calculated_damage)

    def __str__(self):
        equipment_characteristics = f"Equipment name: {self.name}\n" \
                                    f"Equipment wear condition: {self.wear_condition}\n" \
                                    f"Equipment taken capacity: {self.taken_capacity}"
        print(equipment_characteristics)