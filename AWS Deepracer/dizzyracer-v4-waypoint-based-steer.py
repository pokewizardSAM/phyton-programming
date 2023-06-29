import math

def reward_function(params):
    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']
    steps = params['steps']
    time_limit = 180  # 3 minutes in seconds

    # Set the maximum distance from the center to one-third of the track width
    max_distance_from_center = track_width / 3

    # Calculate the reward based on the distance from the center
    reward = 1.0 - (distance_from_center / max_distance_from_center)

    # Penalize if the car goes off track or is too slow
    if not all_wheels_on_track or speed < 1.0:
        reward = -1.0

    # Calculate the direction of the centerline based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radians using arctan2(dy, dx)
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert track direction to degrees
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    # Additional factors to encourage faster completion and efficient steps usage
    progress_reward = progress / steps

    # Apply a time-based reward to encourage completion within the time limit
    if progress_reward > 0 and steps > 0:
        time_penalty = steps / time_limit
        reward += (progress_reward - time_penalty)

    return float(reward)
