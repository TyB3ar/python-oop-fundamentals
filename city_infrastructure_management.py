# Task 1: Vehicle Registration System 
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner
        
    def update_owner(self, new_owner):
        self.owner = new_owner 
        
    def display_details(self):
        print(f"Registration: {self.reg_num}, Type: {self.vehicle_type}, Owner: {self.owner}") 
               
driver1 = Vehicle('ABC-123', 'Sedan', 'Tyler')
driver1.display_details()

print(f"Updating Driver 1: ") 
driver1.update_owner('Arielle')
driver1.display_details() 
