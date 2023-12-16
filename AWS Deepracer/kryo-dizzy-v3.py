import math
def reward_function(params):
    # Read input variables
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])  # absolute steering angle
    progress = params['progress']
    steps = params['steps']
    is_offtrack = params["is_offtrack"]
    waypoints = params['waypoints'] 
    closest_waypoints = params['closest_waypoints'] 
    heading = params['heading'] 

    time_limit = 180  # 3 minutes in seconds
    reward = 10

    # Set the maximum distance from the center to one-third of the track width
    max_distance_from_center = track_width / 3
    
    # Calculate the reward based on the distance from the center
    reward -= (distance_from_center / max_distance_from_center)

    # Penalize if the car goes off track or is too slow
    if not all_wheels_on_track or speed < 1.0:
        reward -= 2.0

    # Increase the reward for staying on the center line and having low steering angles
    center_line_threshold = 0.06 * track_width
    steering_threshold = 10.0  # in degrees
    
    reward -= distance_from_center/center_line_threshold
    
    if not all_wheels_on_track and is_offtrack:
        reward  -= steering_angle/steering_threshold


    # Calculate the direction of the centerline based on the closest waypoints 
    next_point = waypoints[closest_waypoints[1]] 
    prev_point = waypoints[closest_waypoints[0]] 
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians 
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - 
    prev_point[0]) 
    # Convert to degree 
    track_direction = math.degrees(track_direction) 
    # Calculate the difference between the track direction and the heading direction of the car 
    direction_diff = abs(track_direction - heading) 
    if direction_diff > 180: 
        direction_diff = 360 - direction_diff 
    # Penalize the reward if the difference is too large 
    DIRECTION_THRESHOLD = 7.0 
    if direction_diff > DIRECTION_THRESHOLD: 
        reward *= 0.37 

    # Additional factors to encourage faster completion and efficient steps usage
    progress_reward = progress / steps

    # Apply a time-based reward to encourage completion within the time limit
    if progress_reward > 0 and steps > 0:
        time_penalty = steps / time_limit
        reward += (progress_reward - time_penalty)

    return float(reward)
