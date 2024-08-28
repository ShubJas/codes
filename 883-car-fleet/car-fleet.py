from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Step 1: Sort cars by their starting position in ascending order
        # Sorting ensures that we process cars from the farthest to the nearest
        # to the target when iterating in reverse later.
        # The reason we sort is to simulate the scenario where the back cars can catch up
        # with the front cars (forming a fleet) if their time to the target is the same or less.
        time = [float(target - pos) / spd for pos, spd in sorted(zip(position, speed))]

        # This list comprehension computes the time each car will take to reach the target.
        # `target - pos` gives the distance each car needs to travel.
        # Dividing this by the car's speed (`spd`) gives the time taken by each car to reach the target.

        # Step 2: Initialize variables to track the fleet count and the current fleet time threshold
        fleet = fleetcount = 0
        
        # We iterate over the times in reverse order (from the car closest to the target to the farthest).
        # This allows us to check whether each car can form a new fleet or join an existing one.
        for t in reversed(time):
            # Step 3: Check if the current car's time is greater than the current fleet time threshold
            if t > fleet:
                # If the current car takes longer than the current fleet, it cannot catch up and must start a new fleet.
                fleetcount += 1  # Increment the fleet count as this car starts a new fleet.
                fleet = t        # Update the current fleet time to this car's time, as it is now the slowest car leading this fleet.

        # Step 4: Return the total number of fleets formed
        return fleetcount
