from utils.gym_library import calculate_total_weight

class Exercise:
    def __init__(self, name, equipment, muscle_group):
        self.name = name
        self.equipment = equipment        
        self.muscle_group = muscle_group  

    def get_total_weight(self, weight, bodyweight=None):
       return calculate_total_weight(weight, self.equipment, bodyweight)

    def __str__(self):
        return f"{self.name} ({self.muscle_group} - {self.equipment})"


class ChestExercise(Exercise):
   def __init__(self, name, equipment):
        super().__init__(name, equipment, "Chest")


class BackExercise(Exercise):
    def __init__(self, name, equipment):
        super().__init__(name, equipment, "Back")


class BicepsExercise(Exercise):
    def __init__(self, name, equipment):
        super().__init__(name, equipment, "Biceps")


class TricepsExercise(Exercise):
    def __init__(self, name, equipment):
        super().__init__(name, equipment, "Triceps")


class ShouldersExercise(Exercise):
    def __init__(self, name, equipment):
        super().__init__(name, equipment, "Shoulders")


class LegsExercise(Exercise):
    def __init__(self, name, equipment):
        super().__init__(name, equipment, "Legs")
