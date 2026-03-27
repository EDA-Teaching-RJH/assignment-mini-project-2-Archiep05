import re
from models import Exercise, ChestExercise, BackExercise, BicepsExercise
from models import TricepsExercise, ShouldersExercise, LegsExercise
from workout_tracker import WorkoutLog, WorkoutSession
from utils.gym_library import ALL_GROUPS, calculate_volume
from utils.validators import is_valid_name, is_valid_weight, is_valid_reps, is_valid_sets

MUSCLE_CLASS_MAP = {
    "Chest": ChestExercise,
    "Back": BackExercise,
    "Biceps": BicepsExercise,
    "Triceps": TricepsExercise,
    "Shoulders": ShouldersExercise,
    "Legs": LegsExercise}

def get_user_bodyweight():
    while True:
        bw = input("Enter your bodyweight (kg): ").strip()
        if is_valid_weight(bw):
            return float(bw)
        print("Invalid bodyweight. Please enter a positive number e.g 80 or 80.5")

def welcome():
    print("=" * 40)
    print("        WELCOME TO GYMSTONE")
    print("=" * 40)
    bodyweight = get_user_bodyweight()
    print(f"\nBodyweight set to {bodyweight}kg. Lets get to lifting!\n")
    return bodyweight

def select_muscle_group():
    print("\n--- SELECT MUSCLE GROUP ---")
    for i, group in enumerate(ALL_GROUPS, 1):
        print(f"{i}. {group.name}")

    while True:
        choice = input("\nChoose a muscle group: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(ALL_GROUPS):
            return ALL_GROUPS[int(choice) - 1]
        print("Invalid. Please enter a number from the list.")

def select_exercise(muscle_group):
    print(f"\n--- {muscle_group.name.upper()} EXERCISES ---")
    exercises = muscle_group.get_exercises()

    for i, exercise in enumerate(exercises, 1):
        print(f"{i}. {exercise}")
    print(f"{len(exercises) + 1}. Add custom exercise")

    while True:
        choice = input("\nChoose an exercise: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(exercises):
                return exercises[choice - 1]
            elif choice == len(exercises) + 1:
                return add_custom_exercise(muscle_group)
        print("Invalid. Please enter a number from the list.")

def add_custom_exercise(muscle_group):
    while True:
        name = input("Enter custom exercise name: ").strip()
        if is_valid_name(name):
            muscle_group.add_custom_exercise(name)
            print(f"{name} added to {muscle_group.name}!")
            return name
        print("Invalid. Use letters and spaces only.")

def select_equipment():
    print("\n--- SELECT EQUIPMENT ---")
    print("1. Barbell")
    print("2. Dumbbell")
    print("3. Bodyweight")
    print("4. Weighted Bodyweight")

    while True:
        choice = input("\nChoose equipment type: ").strip()
        if choice == "1":
            return "barbell"
        elif choice == "2":
            return "dumbbell"
        elif choice == "3":
            return "bodyweight"
        elif choice == "4":
            return "weighted_bodyweight"
        print("Invalid. Please enter 1, 2, 3 or 4.")

def get_sets_reps_weight(equipment, bodyweight):
    while True:
        sets = input("How many sets? ").strip()
        if is_valid_sets(sets):
            sets = int(sets)
            break
        print("Invalid. Please enter a whole positive number e.g 3")

    while True:
        reps = input("How many reps per set? ").strip()
        if is_valid_reps(reps):
            reps = int(reps)
            break
        print("Invalid. Please enter a whole positive number e.g. 10")
    
    if equipment == "bodyweight":
        print(f"Using your bodyweight of {bodyweight}kg")
        return sets, reps, 0, bodyweight

    elif equipment == "weighted_bodyweight":
        while True:
            weight = input("How much extra weight are you adding (kg)? ").strip()
            if is_valid_weight(weight):
                weight = float(weight)
                total = bodyweight + weight
                print(f"Total weight: {bodyweight}kg bodyweight + {weight}kg = {total}kg")
                return sets, reps, weight, total

    elif equipment == "dumbbell":
        while True:
            weight = input("Weight of one dumbbell (kg)? ").strip()
            if is_valid_weight(weight):
                weight = float(weight)
                total = weight * 2
                print(f"Total weight: {weight}kg x 2 dumbbells = {total}kg")
                return sets, reps, weight, total

    else:
        while True:
            weight = input("Total barbell weight (kg)? ").strip()
            if is_valid_weight(weight):
                weight = float(weight)
                return sets, reps, weight, weight

def log_workout(log, bodyweight):
    
    muscle_group = select_muscle_group()
    exercise_name = select_exercise(muscle_group)
    equipment = select_equipment()
    sets, reps, weight_per_set, total_weight = get_sets_reps_weight(equipment, bodyweight)

    exercise_class = MUSCLE_CLASS_MAP[muscle_group.name]
    exercise = exercise_class(exercise_name, equipment)
    volume = calculate_volume(sets, reps, total_weight)

    session = WorkoutSession(exercise, sets, reps, weight_per_set, total_weight)
    log.log_session(session)

    print(f"\n✓ Logged! Total volume for this exercise: {volume}kg")

def view_prs(log):
    exercise_name = input("\nEnter exercise name to check PR: ").strip()

    if not is_valid_name(exercise_name):
        print("Invalid exercise name.")
        return

    weight = input("At what weight (kg)? ").strip()
    if not is_valid_weight(weight):
        print("Invalid weight.")
        return
    
    best_reps = log.get_pr(exercise_name, float(weight))
    if best_reps == 0:
        print(f"\nNo PR found for {exercise_name} at {weight}kg.")
    else:
        print(f"\nPR for {exercise_name} at {weight}kg: {best_reps} reps")
    
def view_cumulative_weight(log):
    print("\n--- CUMULATIVE WEIGHT LIFTED ---")
    print("1. Overall total")
    print("2. For a specific exercise")
    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        total = log.get_cumulative_weight()
        print(f"\nTotal weight lifted across all exercises: {total}kg")

    elif choice == "2":
        exercise_name = input("Enter exercise name: ").strip()
        if not is_valid_name(exercise_name):
            print("Invalid exercise name.")
            return
        total = log.get_cumulative_weight(exercise_name)
        print(f"\nTotal weight lifted for {exercise_name}: {total}kg")

    else:
        print("Invalid choice.")
    
def update_bodyweight(bodyweight):
    print(f"\nCurrent bodyweight: {bodyweight}kg")
    while True:
        new_bw = input("Enter new bodyweight (kg): ").strip()
        if is_valid_weight(new_bw):
            new_bw = float(new_bw)
            print(f"Bodyweight updated to {new_bw}kg!")
            return new_bw
        print("Invalid. Please enter a positive number e.g. 80 or 75.5")

def main_menu(log, bodyweight):
    while True:
        print("\n" + "=" * 40)
        print("             MAIN MENU")
        print("=" * 40)
        print("1. Log a workout")
        print("2. View my PRs")
        print("3. View cumulative weight lifted")
        print("4. Update my bodyweight")
        print("5. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            log_workout(log, bodyweight)
        elif choice == "2":
            view_prs(log)
        elif choice == "3":
            view_cumulative_weight(log)
        elif choice == "4":
            bodyweight = update_bodyweight(bodyweight)
        elif choice == "5":
            print("\nWell done today, See you next session!")
            break
        else:
            print("Invalid choice. Please enter a number from 1-5.")

if __name__ == "__main__":
    log = WorkoutLog()
    bodyweight = welcome()
    main_menu(log, bodyweight)



