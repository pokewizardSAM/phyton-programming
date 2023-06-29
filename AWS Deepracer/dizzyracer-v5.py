def reward_function(params):
    # Read input variables
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = abs(params['steering_angle'])  # absolute steering angle
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

    # Increase the reward for staying on the center line and having low steering angles
    center_line_threshold = 0.05 * track_width
    steering_threshold = 15.0  # in degrees
    if distance_from_center <= center_line_threshold and steering_angle < steering_threshold:
        reward += 0.499

    if steering_angle >= steering_threshold and all_wheels_on_track:
        reward +=0.99
    else:
        reward -=0.3

    # Additional factors to encourage faster completion and efficient steps usage
    progress_reward = progress / steps

    # Apply a time-based reward to encourage completion within the time limit
    if progress_reward > 0 and steps > 0:
        time_penalty = steps / time_limit
        reward += (progress_reward - time_penalty)

    return float(reward)
