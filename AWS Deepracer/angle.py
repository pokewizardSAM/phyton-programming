import math
waypoints = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
closest_waypoints = [10,11]
# Initialize the reward with typical value
reward = 1.0
# Calculate the direction of the centerline based on the closest waypoints
next_point = waypoints[closest_waypoints[1]]
prev_point = waypoints[closest_waypoints[0]]
# Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
# Convert to degree
track_direction = math.degrees(track_direction)

print(track_direction)