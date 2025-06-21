# peachtree_castle_ursina.py
# Python 3.13 with Ursina
# Creates a simple representation of Peach's Castle with a 600x400 window.

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the application
app = Ursina()

# --- Configuration ---
window.title = "Peach's Castle"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True
window.size = (600, 400) # Set the requested window size

# --- Colors ---
WALL_COLOR = color.rgb(255, 215, 220) # A light, peachy-pink for walls
ROOF_COLOR = color.rgb(200, 30, 30)   # A classic red for the roofs
TOWER_COLOR = color.rgb(255, 180, 185) # A slightly different pink for towers
WINDOW_FRAME_COLOR = color.white
STAINED_GLASS_COLOR = color.gold

# --- Build the Castle ---

# 1. Main Keep (the central building)
main_keep = Entity(
    model='cube',
    color=WALL_COLOR,
    scale=(12, 6, 10),
    position=(0, 3, 0),
    collider='box'
)
main_keep_roof = Entity(
    model='pyramid',
    color=ROOF_COLOR,
    scale=(13, 4, 11),
    position=(0, 6, 0),
    rotation_y=45
)

# 2. Four Corner Towers
corner_positions = [(-7, 6, -6), (7, 6, -6), (-7, 6, 6), (7, 6, 6)]
for pos in corner_positions:
    tower = Entity(
        model='cube',
        color=TOWER_COLOR,
        scale=(4, 12, 4),
        position=(pos[0], pos[1] / 2, pos[2]), # Position is centered, so Y is half of height
        collider='box'
    )
    roof = Entity(
        model='pyramid',
        color=ROOF_COLOR,
        scale=(4.5, 3, 4.5),
        position=(pos[0], pos[1] + 1.5, pos[2]) # Place roof on top
    )

# 3. Central Main Tower
central_tower = Entity(
    model='cube',
    color=TOWER_COLOR,
    scale=(7, 12, 7),
    position=(0, 10, 0), # Y is 6 (keep) + 6 (half of tower height) - 2 overlap
    collider='box'
)
central_tower_roof = Entity(
    model='pyramid',
    color=ROOF_COLOR,
    scale=(7.5, 4, 7.5),
    position=(0, 16, 0) # Place roof on top of central tower
)

# 4. The Iconic Stained-Glass Window
window_pos_z = central_tower.z - (central_tower.scale_z / 2) - 0.01 # Place on front face
stained_glass = Entity(
    parent=central_tower, # Attach to the central tower
    model='quad',
    color=STAINED_GLASS_COLOR,
    scale=(0.5, 0.5, 1), # Scale relative to parent
    position=(0, 0.25, -0.51) # X, Y, Z position relative to parent center
)

# 5. Ground and Sky
ground = Entity(
    model='plane',
    scale=100,
    color=color.rgb(100, 200, 100), # A nice green
    texture='white_cube',
    texture_scale=(50,50),
    collider='mesh'
)
sky = Sky()

# --- Player and Execution ---
player = FirstPersonController(
    position=(0, 2, -20), # Start in front of the castle
    speed=8
)

# Start the engine
app.run()
