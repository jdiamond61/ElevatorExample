class Elevator:
    def __init__(self, start_floor):
        self.current_floor = start_floor
        self.total_travel_time = 0
        self.visited_floors = [start_floor]

    def move_to_floor(self, destination_floor):
        travel_distance = abs(destination_floor - self.current_floor)
        self.total_travel_time += travel_distance * 10  # Assuming constant travel time per floor
        self.current_floor = destination_floor
        self.visited_floors.append(destination_floor)

def simulate_elevator(start_floor, floors_to_visit):
    elevator = Elevator(start_floor)
    for floor in floors_to_visit:
        elevator.move_to_floor(floor)
    return elevator.total_travel_time, elevator.visited_floors

if __name__ == "__main__":
    # Example inputs: elevator start=12 floor=2,9,1,32
    start_floor = 12
    floors_to_visit = [2, 9, 1, 32]
    total_travel_time, visited_floors = simulate_elevator(start_floor, floors_to_visit)
    print("Total travel time:",total_travel_time, "floors visited:",", ".join(map(str, visited_floors)))
