import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation

# Define radii
r_B = 9  # radius of circle B (larger)
r_A = 3  # radius of circle A (smaller), which is 1/3 of B

# Set up static visualization first
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title(f'SAT Circle revolution problem')
ax.set_aspect('equal')
ax.grid(True)

# Initial position of Circle A
initial_A_center = (-(r_B+r_A), 0)
circle_A_anim = Circle(initial_A_center, r_A, fill=False, color='orange', label='Circle A (radius=1)')
ax.add_patch(circle_A_anim)

# Draw the path of center A (a circle with radius r_B + r_A)
circle_path = Circle((0, 0), r_B + r_A, fill=False, color='orange', linestyle='--', 
                    alpha=0.2, label='Path of center A')
ax.add_patch(circle_path)

# Draw Circle B in the animation
circle_B_anim = Circle((0, 0), r_B, fill=False, color='blue', label='Circle B (radius=3)')
ax.add_patch(circle_B_anim)

# Mark the center of circle A
center_A_point, = ax.plot([], [], 'ro', markersize=5)

# Mark a point on the circumference of circle A
touch_point_marker, = ax.plot([], [], 'o', markersize=5, label='Circle A orientation point')

# Path traced by the center of A
center_path_line, = ax.plot([], [], '-', alpha=0.3)
center_path_points = []

# Add a legend
ax.legend(loc='upper right')

# Set limits for animation
ax.set_xlim(-r_B*2, r_B*2)
ax.set_ylim(-r_B*2, r_B*2)

# Animation update function
def update(frame):
    # Calculate progress (0 to 1) for one complete revolution around B
    progress = frame / 100
    angle = progress * 2 * np.pi
    
    # Calculate new center position for A
    center_x = -(r_B + r_A) * np.cos(angle)
    center_y = (r_B + r_A) * np.sin(angle)
    
    # Update circle A position
    circle_A_anim.center = (center_x, center_y)
    center_A_point.set_data(center_x, center_y)
    
    # Track the path of the center
    center_path_points.append((center_x, center_y))
    if len(center_path_points) > 1:
        xs, ys = zip(*center_path_points)
        center_path_line.set_data(xs, ys)
    
    # Calculate angle of A's rotation
    rotation_angle = angle * -((r_B + r_A) / r_A)
    
    # Calculate position of the point on circumference of A
    point_x = center_x + r_A * np.cos(rotation_angle)
    point_y = center_y + r_A * np.sin(rotation_angle)
    touch_point_marker.set_data(point_x, point_y)
    
    return circle_A_anim, center_A_point, touch_point_marker, center_path_line

# Create animation
ani = animation.FuncAnimation(fig, update, frames=101, interval=60, blit=True)

plt.tight_layout()
plt.show()