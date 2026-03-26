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
    

    
  