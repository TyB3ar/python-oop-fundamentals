# Task 2: Event Management System Enhanced
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0 # class variable to tally participants 
        
    def add_participant(self):
        self.participant_count += 1 # adds one to count when called 
        print(f"Participant added, current participant total: {self.participant_count}")  
    
    def participant_count(self):
        return self.participant_count 
    
first_event = Event('Coding Temple Seminar', '09-25') 
first_event.add_participant() # adds participant for first event
first_event.add_participant() # adds participant for first event
first_event.add_participant() # adds participant for first event

print(f"Current Total Participant Count: {first_event.participant_count}") # print current event count 

