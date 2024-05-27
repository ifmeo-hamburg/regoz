import numpy as np
import adcpreader

filename = 'raw/WR2_AUTO_600KHZ_0_002_001_23-05-11_064011.PD0'

# Define reader, sink, info
reader = adcpreader.rdi_reader.PD0()
sink = adcpreader.rdi_writer.DataStructure()
info = adcpreader.rdi_writer.Info(pause=False)

# Define processing pipeline
pipeline = reader | info | sink

# Process the pipeline
pipeline.process(filename)

# Accessing the available keys
print("Keys:")
print(sink.keys())
print("")

# Get NaN value (assume, that last entry of ensemble 1 is NaN - TODO fix this)
nan_value = sink.data['velocity_starboard'][0][-1]

# Extracting data for velocity transformation
velocity_starboard = np.array(sink.data['velocity_starboard'])
velocity_forward = np.array(sink.data['velocity_forward'])
velocity_up = np.array(sink.data['velocity_up'])

heading = np.array(sink.data['Heading'])
pitch = np.array(sink.data['Pitch'])
roll = np.array(sink.data['Roll'])

# Set NaN values to NaN
velocity_starboard = np.where(velocity_starboard == nan_value, np.nan, velocity_starboard)
velocity_forward = np.where(velocity_forward == nan_value, np.nan, velocity_forward)
velocity_up = np.where(velocity_up == nan_value, np.nan, velocity_up)

# Assuming heading, pitch, and roll are in degrees, convert to radians
heading_rad = np.deg2rad(heading)
pitch_rad = np.deg2rad(pitch)
roll_rad = np.deg2rad(roll)

# Transformation from instrument to earth coordinates
def transform_to_earth(vel_starboard, vel_forward, vel_up, heading, pitch, roll):
    # Rotation matrix for heading
    R_heading = np.array([
        [np.cos(heading), -np.sin(heading), 0],
        [np.sin(heading), np.cos(heading), 0],
        [0, 0, 1]
    ])
    
    # Combine the velocities
    velocity_instr = np.array([vel_starboard, vel_forward, vel_up])
    
    # Transform velocities
    velocity_earth = np.dot(R_heading, velocity_instr)
    
    return velocity_earth

# Calculate east and north velocities for each ensemble
east_velocity = []
north_velocity = []
up_velocity = []

for i in range(len(velocity_starboard)):
    vel_earth = transform_to_earth(
        velocity_starboard[i],
        velocity_forward[i],
        velocity_up[i],
        heading_rad[i],
        pitch_rad[i],
        roll_rad[i]
    )
    east_velocity.append(vel_earth[0])
    north_velocity.append(vel_earth[1])
    up_velocity.append(vel_earth[2])

# Convert to numpy arrays
east_velocity = np.array(east_velocity)
north_velocity = np.array(north_velocity)
up_velocity = np.array(up_velocity)


# Print velocity data for ensemble 1
print("East Velocity for first ensemble:\n", east_velocity[0])
print("North Velocity for first ensemble:\n", north_velocity[0])
print("Up Velocity for first ensemble:\n", up_velocity[0])

# Calculate the magnitude
magnitude = np.sqrt(east_velocity**2 + north_velocity**2)

# Calculate the direction in radians
direction_radians = np.arctan2(north_velocity, east_velocity)

# Convert direction to degrees
direction_degrees = np.degrees(direction_radians)

# Ensure directions are in the range [0, 360)
direction_degrees = (direction_degrees + 360) % 360

# Print results
print("Magnitude:")
print(magnitude)

print("\nDirection in degrees:")
print(direction_degrees)
