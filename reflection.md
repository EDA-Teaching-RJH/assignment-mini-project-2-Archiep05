# Develop journal - Gym tracker mini prject 2 

~~~OOP - workshop 9 
I made an exersice base class that contained 6 subclasses , one for each muscle group eg BackExercise . i used super().__init__ to pass values up to the exercise base class meaning each subclass was able to set its own muscle group.

~~~Libraries - workshop 7
i used built in libraries like datetime . i also made my own cutoms library in utils/gym_librARYB which has lists of preset exercises and calculate volume functions. i set it up using an __init__ file.


An issue i ran into was getting a Modulenotfound errror when i was running my tests . i wasnt sure why it was happening because the utils folder was there . after some poking around i realised that i was running the file from within the tests folder so python was looking for it there rather than in the root of the project . i fixed it by running python -m unittest tests/test_tracker.py from the root directory instead

Next time id write the tests first so i can spot bugs earlier. id also write out a solid plan of exaclt what funtions i want as i had to go back and change them.And id also add a feature to maybe view the full workout history or add a super set option .
