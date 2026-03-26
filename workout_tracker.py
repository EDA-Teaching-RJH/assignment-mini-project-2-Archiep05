import csv
import os
from models import Exercise
from datetime import datetime

class WorkoutSession:
    def __init__(self, exercise, sets, reps, weight_per_set, total_weight, date=None):
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weight_per_set = weight_per_set  
        self.total_weight = total_weight
        self.date = date or datetime.now().strftime("%d/%m/%Y")
    
class WorkoutLog:
    def __init__(self, filename="workout_data.csv"):
        self.filename = filename
        self.sessions = []
        self.load_from_csv()

    def log_session(self, session):
        self.sessions.append(session)
        self.save_to_csv(session)

    def save_to_csv(self, session):
        file_exists = os.path.exists(self.filename)
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["date", "exercise", "muscle_group",
                                 "equipment", "sets", "reps","weight_per_set", "total_weight"])

            writer.writerow([
                session.date,
                session.exercise.name,
                session.exercise.muscle_group,
                session.exercise.equipment,
                session.sets,
                session.reps,
                session.weight_per_set,
                session.total_weight
            ])

    def load_from_csv(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.sessions.append(row)
    
    def get_pr(self, exercise_name, weight):
        best_reps=0
        for session in self.sessions:
            if isinstance(session, dict):
                if (session["exercise"] == exercise_name and
                        float(session["weight_per_set"]) == float(weight)):
                    if int(session["reps"]) > best_reps:
                        best_reps = int(session["reps"])
        return best_reps
    def get_cumulative_weight(self, exercise_name=None):
       
        total = 0

        for session in self.sessions:
            if isinstance(session, dict):
                if exercise_name is None or session["exercise"] == exercise_name:
                    total += float(session["total_weight"])

        return total               


    
  