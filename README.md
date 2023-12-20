# Salam 👐🏻

### 📖 Repository description:

This repository features a mini-game that simulates a battle between spaceships. Information about the progress of the
battle is displayed in the console.

Below is a description of the task.

### 🎯 Purpose of the program:

I wrote this program to brush up on my basic knowledge of OOP. All further functionality works on the basic principles
of OOP.

## Task 📝

### Stage #1

```
Create a class called Equipment - a base class that will describe the additional equipment of a future spaceship. The Equipment class should have the following attributes:

Properties:
    ▫ wear_condition: the level of wear and tear on the equipment (maximum value - 100, default - 0). 
      The wear and tear of the equipment affect its effectiveness. 
      When the wear and tear level reaches 100, the equipment can no longer be used.
    ▫ taken_capacity: the occupied volume (30 - 100). Implement a check, raise a ValueError if the provided value is not within the specified range.
    ▫ name: the name.
    
Methods:
    ▫ action: With each use of any equipment, the wear and tear level increases by 10 units. 
      If the equipment is worn out, an EquipmentWornOutError exception must be raised. 
      This method should be called in the action methods of inheriting classes.
    ▫ Create a method that takes a value as an argument and returns this value, taking into account its wear and tear.
      Use this method in the action method in inheriting classes.
    
```

### Stage #2

```
Implementing Ship Component Classes:

    🔫 Weapon Class - a class describing the weapons installed on the spaceship. It should have the following attributes:
        
        Properties:
            ▫ All properties inherited from the base class of additional equipment.
            ▫ min_damage - minimum damage inflicted (from 5 to 40). Implement a check, raise a ValueError if the provided value is not within the specified range.
            ▫ max_damage - maximum damage inflicted (minimum damage + 40%).
            ▫ critical_hit_chance - chance of critical damage (from 1 to 70). Implement a check, raise a ValueError if the provided value is not within the specified range.
        
        Methods:
            ▫ Override the action method. The method should return the damage (int or float) that this weapon should inflict. 
              Damage is determined randomly within the range between the minimum and maximum damage of the weapon. 
              With the probability specified in the critical_hit_chance property, critical damage may be inflicted, the size of which exceeds the maximum damage by 40%. 
              With a 15% probability, the weapon may misfire, and no shot will occur.
         
         
    🛡 Armor Class - a class describing the spaceship's armor, which should have the following attributes:
        
        Properties:
            ▫ All properties inherited from the base class of additional equipment.
            ▫ defense - the amount of defense provided by this armor (1-10). Implement a check, raise a ValueError if the provided value is not within the specified range.
        
        Methods:
            ▫ Override the action method. The method should return the amount of defense that will be added to the spaceship's hull defense.
        
        
    🧭 Navigator Class - a class describing navigation equipment. It should have the following attributes:

        Properties:
             ▫ All properties inherited from the base class of additional equipment.
             ▫ accuracy - the number of units added to accuracy (5-40). Implement a check, raise a ValueError if the provided value is not within the specified range.
       
        Methods:
            ▫ Override the action method. The method should return the number of accuracy units added to the accuracy indicator. 
              With a 20% probability, an electromagnetic discharge may occur, creating interference on the radar, reducing its effectiveness by half.

```

### Stage #3

```

Create a class called Spaceship that describes a spacecraft. The spaceship has the following characteristics:
    
    Properties: 
        ▫ spaciousness: Capacity (from 300 to 1000) - responsible for the ability to accommodate additional equipment. 
          The total occupied volume of additional equipment cannot exceed the spaceship's capacity. 
          Implement a check, raise a ValueError if the provided value is not within the specified range.
        ▫ defense: Base defense of the spaceship without installed additional equipment. Calculated by the formula: (1 / (spaciousness * number_of_armor_slots)) * 10 ** 4.
        ▫ accuracy: Base accuracy of the spaceship without installed additional equipment (from 0 to 5).
        ▫ health: Technical condition of the spaceship. (Default value is 1000, minimum is 0). As damage is taken, the value should decrease. 
        ▫ The spaceship has slots for:
            Additional armor (1-3 slots);
            Weapons (1-4 slots);
            Navigation devices (1-2 slots).
    
    Methods:
        ▫ Implement methods for setting up all types of additional equipment. For each type of additional equipment, there should be a specific installation method. 
          The method should take an element of additional equipment of that type as an argument and place it in a free slot of that type. 
          Before placing the equipment in a free slot, check if there are available slots in the ship for that type of equipment and if the sum of the volume of that equipment and the volume of the installed equipment on the ship will not exceed the spaceship's capacity.
          If there are no free slots, throw a FreeSlotError exception, and if the volume is exceeded, throw a TotalVolumeError, creating these exceptions by inheriting from ValueError.
        ▫ attack - a method that sequentially fires all weapons installed on the ship. The method takes a target spaceship as an argument. 
          The method should determine the total accuracy (the sum of the indicators of all navigators on board and the accuracy of the spaceship itself). 
          Accuracy is determined before firing each weapon. The obtained accuracy value will determine the probability of hitting the target. 
          For each shot from a weapon, call the defend method.
        ▫ defend - a method through which the ship will receive damage, determine the total defense points (ship defense and the sum of defense provided by all additional equipment responsible for defense), and subtract the difference between the received damage and defense from the ship's condition. 
          Also, check that if the level of defense exceeds the received damage, the technical condition of the ship should not change.
    
    Catch errors that faulty equipment will throw and display a message.
    
```

### Stage #4

```

Create a class called Application. Implement a method that will run the main game loop.

Create 20 random types of equipment for each category. Create two spaceships with random values. 
Using lists with equipment, add weapons, armor, and navigation to the ship slots, checking (through error handling) that it fits the number of slots and the capacity of the spaceship. 
If there are free slots, check the entire list of equipment, as one of them may be suitable in terms of mass.

Next, initiate a battle between the two spaceships. 
Display information about each round: round number, information about the ships after the opponent's move, who is currently attacking, etc. Use the attack method for the ships.

After someone wins, display a message and suggest playing again. If no one wins within 20 rounds, the winner is the one whose ship is in a better technical condition.

```

### Stage #5

```

Modify the program so that weapons are of different types. Armor should now provide protection only against a specific type of damage.

Create a class called Damage, whose constructor will take two parameters: damage and its type. From the action method of the Weapon class objects, return not a number, but a Damage object. 
Modify the code where necessary to make it work correctly with Damage objects.

The base defense of the spaceship protects against any type of damage. 
Thus, for example, if the ship is equipped with armor that protects only against laser damage and the ship is attacked with a fragmentation weapon, the armor will not be considered in the damage calculation, only the base defense of the ship will be taken into account.

```

### Stage #6

```

Write a class HealingDrone that will inherit from the Equipment class. 
The drone operates on energy from electromagnetic radiation and works only if the ship has been damaged by an electromagnetic weapon. 

The drone will have one additional property, indicating its effectiveness (from 50 to 200). 
Add a slot for the drone in the ship class (the ship can have from 0 to 2 drones). 

Override the method of using the drone; it should return the number of units that will be restored to the ship when used 
(calculated by the formula: damage inflicted by the electromagnetic weapon * drone effectiveness / 100). 

Unlike all other additional equipment, each time the drone is used, its wear and tear increases by 20 units, not 10. 

Use the drone every time the ship is attacked.

```