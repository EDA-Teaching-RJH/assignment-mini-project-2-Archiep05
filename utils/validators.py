import re

def is_valid_name(name):
    pattern = r"^[a-zA-Z\s]+$"
    return bool(re.match(pattern, name))

def is_valid_weight(weight):
    pattern = r"^\d+(\.\d+)?$"
    return bool(re.match(pattern, weight))

def is_valid_reps(reps):
    pattern = r"^\d+$"
    return bool(re.match(pattern, reps))

def is_valid_sets(sets):
    pattern = r"^\d+$"
    return bool(re.match(pattern, sets))

