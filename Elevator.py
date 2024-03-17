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
    while True:
        try:
            start_floor = int(input("Enter the starting floor: "))
            floors_str = input("Enter the floors to visit (comma-separated): ")
            floors_to_visit = [int(floor) for floor in floors_str.split(",")]

            # Input validation
            if start_floor < 1 or any(floor < 1 for floor in floors_to_visit):
                raise ValueError("Floor numbers must be positive integers.")

            total_travel_time, visited_floors = simulate_elevator(start_floor, floors_to_visit)
            print("Total travel time:", total_travel_time)
            print("Floors visited in order:", visited_floors)
            break  # Exit the loop if input is valid
        except ValueError as e:
            print("Invalid input:", e)
