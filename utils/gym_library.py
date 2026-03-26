


class MuscleGroup:

    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises
    
    def get_exercises(self):
        return self.exercises
    
    def add_custom_exercises(self, exercise_name):
        self.exercises.append(exercise_name)
    
    def __str__(self):
        return f"{self.name} ({len(self.exercises)} exercises)"

CHEST = MuscleGroup("Chest" ["Barbell Bench Press" "Barbell Bench Press","Dumbbell Bench Press",
    "Incline Barbell Bench Press",
    "Incline Dumbbell Bench Press","Chest Fly","Push Up"])

BACK = MuscleGroup("Back", ["Deadlift","Barbell Row","Dumbbell Row","Lat Pulldown",
  "Pull Up","Seated Cable Row"])

BICEPS = MuscleGroup("Biceps", ["Barbell Curl","Dumbbell Curl",
   "Hammer Curl","Preacher Curl",])

TRICEPS = MuscleGroup("Triceps", ["Tricep Pushdown","Skull Crusher","Overhead Tricep Extension",
"Dips","Close Grip Bench Press"])

SHOULDERS = MuscleGroup("Shoulders", ["Overhead Press","Dumbbell Lateral Raise","Front Raise",
"Arnold Press","Face Pull"])

LEGS = MuscleGroup("Legs", ["Barbell Squat","Leg Press","Bulgarian Split Squat",
"Leg Curl","Leg Extension","Calf Raise"])

ALL_GROUPS = [CHEST, BACK, BICEPS, TRICEPS, SHOULDERS, LEGS,]

def calculate_weight_total(weight,equipment,bodyweight=None):
    if equipment == "dumbbell":
        return weight * 2
    elif equipment == "barbell":
        return weight
    elif equipment == "bodyweight":
        if bodyweight is None:
            raise ValueError("Bodyweight must be provided for bodyweight exercises")
        return bodyweight
    elif equipment == "weighted_bodyweight":
        if bodyweight is None:
            raise ValueError("Bodyweight must be provided for weighted bodyweight exercises")
        return bodyweight + weight
    else:
        raise ValueError(f"Unknown equipment type: {equipment}")
    



       




