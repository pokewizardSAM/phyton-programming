import math 


def reward_function(params):
    # Read input variables
    track_width = params['track_width']
    heading  = params["heading"]
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    # steering_angle = abs(params['steering_angle'])  # absolute steering angle
    waypoints = params["waypoints"]
    closest_waypoints = params['closest_waypoints']
    x = params["x"]
    y = params["y"]
    time_limit = 180  # 3 minutes in seconds


    progress = params['progress']
    steps = params['steps']


    final_reward = 1e-2

    if all_wheels_on_track:
        final_reward += 1
    if distance_from_center > track_width/3:
        acceptable_distance = 0.1
        scaling_factor = 1 / acceptable_distance
        final_reward = 1 - distance_from_center * scaling_factor
    
    rabbit = [0,0]
    pointing = [0,0]
        
    # Reward when yaw (heading ) is pointed to the next waypoint IN FRONT.
    
    # Find nearest waypoint coordinates
    next_waypoint = waypoints[closest_waypoints[1]]
    rabbit_x = next_waypoint[0]
    rabbit_y = next_waypoint[1]
    rabbit = [rabbit_x, rabbit_y]

    
    radius = math.hypot(x - rabbit[0], y - rabbit[1])
    
    pointing[0] = x + (radius * math.cos(heading))
    pointing[1] = y + (radius * math.sin(heading))
    
    vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])
    
    # Max distance for pointing away will be the radius * 2
    # Min distance means we are pointing directly at the next waypoint
    # We can setup a reward that is a ratio to this max.
    
    if vector_delta == 0:
        final_reward += 1
    else:
        final_reward += ( 1 - ( vector_delta / (radius * 2)))

    if speed < 1.0:
        final_reward -= speed*0.2

    progress_reward = progress / steps

    if progress_reward > 0 and steps > 0:
        time_penalty = steps / time_limit
        reward += (progress_reward - time_penalty)
    return final_reward
    