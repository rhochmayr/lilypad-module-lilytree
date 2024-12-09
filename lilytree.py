import bpy
import sys

# Function to normalize a value from a range (0-255) to a desired range (min_val, max_val)
def normalize(value, min_val, max_val):
    return min_val + (value / 255) * (max_val - min_val)

# Get arguments passed from the command line
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

# Input the Ethereum address with 0x
eth_address = argv[0] # e.g. "0x40B38765696e3d5d8d9d834D8AaD4bB6e418E489"

print(f"eth_address: {eth_address }") 

# Remove '0x' prefix if it exists
if eth_address.startswith("0x"):
    eth_address = eth_address[2:]  # Remove the first two characters

# Ensure the Ethereum address has 40 characters
if len(eth_address) != 40:
    raise ValueError("Ethereum address must have exactly 40 hex characters after '0x'.")


# Split the Ethereum address into 20 groups of 2 characters
hex_pairs = [eth_address[i:i+2] for i in range(0, len(eth_address), 2)]

# Convert hex pairs to integers (0-255)
values = [int(pair, 16) for pair in hex_pairs]

# Print the Ethereum address breakdown
print("\n--- Ethereum Address Breakdown ---")
print(f"{'Index':<6} {'Hex Pair':<11} {'Decimal'}")
print("-" * 26)
for i, (pair, value) in enumerate(zip(hex_pairs, values)):
    print(f"[{i:02}]   [{pair:<2}]   ->   {value:>3}")

# Ensure the object is active and in Object Mode
obj = bpy.data.objects.get("Tree")
bpy.context.view_layer.objects.active = obj

if obj is None:
    print("No active object selected.")
else:
    if obj.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Get the modifier
    mod = obj.modifiers.get("Fantasy_Tree_Gen")

    if mod:
        print("Modifier found. Updating inputs...")

        # Update modifier values
        print("Setting default input values...")
        
        # Trunk Settings
        mod["Input_5"] = 21  # [Base Count] - Number of trunk curves (Range: 3-25)
        mod["Input_6"] = 250 # [Tree Seed] - Random Seed of the overall trunk (Range: 0-1000)
        mod["Input_7"] = 64 # [ Trunk Resolution ] - Resolution of the tree along the curve (Range: 8-256)
        mod["Input_10"] = 32 # [ Resolution ] - Resolution controlling the roundness/bevel of the curve (Range: 8-64)
        mod["Input_8"] = 0.392 # [ Tree Distortion ] - Changes how much the tree is distorted (Range: 0.000-1.000)
        mod["Input_28"] = 0.500 # [ Distortion Roughness ] - Change the roughness of the distortion (Range: 0.000-1.000)
        mod["Input_9"][0] = 0.000 # [  Trunk Noise X] - Change the noise vector for different distortions (Range: 0.000)
        mod["Input_9"][1] = -0.560 # [  Trunk Noise Y] - Change the noise vector for different distortions (Range: -10.000-10.000)
        mod["Input_9"][2] = 8.930 # [  Trunk Noise Z] - Change the noise vector for different distortions (Range: -10.000-10.000)
        
        # Branches Settings
        mod["Input_12"] = True # [ Angle Based ] - Split the branches based on defined angle (Range: True/False)
        mod["Input_13"] = 19.620 # [ Split Angle ] - Angle for splitting the branches (Range: 0.000-45.000)
        mod["Input_14"] = 1.500 # [ Branch Length ] - Length of the branches (Range: 1.000-3.000)
        mod["Input_15"] = 12 # [ Branch Count ] - Maximum Number of Branches to be split (Range: 3-15)
        mod["Input_16"] = 389 # [ Branch Seed ] - Random Seed for Branch generation (Range: 0-1000)
        mod["Input_17"] = True # [ Leaves ] - Toggles leaves on and off (Range: True/False)
        mod["Input_19"] = False # [ Leaves Block ] - Make the leaves appear dense with low density (Range: True/False)
        mod["Input_26"] = 296 # [ Leaves Seed ] - Random seed for leaf generation (Range: 0-1000)
        mod["Input_4"][0] = 0.432 # [ Leaves Color R ] - Color of the leaves RGB Channel Red (Range: 0.000-1.000)
        mod["Input_4"][1] = 0.082 # [ Leaves Color G ] - Color of the leaves RGB Channel Green (Range: 0.000-1.000)        
        mod["Input_4"][2] = 0.393 # [ Leaves Color B ] - Color of the leaves RGB Channel Blue (Range: 0.000-1.000)        
        mod["Input_20"] = 300 # [ Leaves Density ] - Density of the leaves (Range: 0-500)
        mod["Input_21"] = 0.100 # [ Leaves Scale ] - Sie of the leaves (Range: 0.050-0.150)
        mod["Input_22"] = 0.500 # [ Leaves Distortion ] - Distort the distribution of the leaves (Range: 0.000-1.000)
        mod["Input_23"][0] = 0.000 # [ Leaves Noise X ] - Change the noise vector for different distortions (Range: 0.000)
        mod["Input_23"][1] = -0.560 # [ Leaves Noise Y ] - Change the noise vector for different distortions (Range: -10.000-10.000)
        mod["Input_23"][2] = 8.930 # [ Leaves Noise Z ] - Change the noise vector for different distortions (Range: -10.000-10.000)        
        mod["Input_18"] = True # [ Vines ] - Toggle vines on and off (Range: True/False)
        mod["Input_24"] = -5.000 # [ Vine Gravity ] - How long the vine can hang (Range: -5.000-0.000)
        mod["Input_25"] = 573 # [ Vine Seed ] - Random seed for generating vines (Range: 0-1000)

        # Wind Settings
        mod["Input_32"] = True # [ Wind ] - Toggles wind on and off (Range: True/False)
        mod["Input_29"] = 1.000 # [ Wind Speed ] - Wind speed (Range: 0.750-1.250)
        
        # Falling Leaves Settings
        mod["Input_34"] = 2.500 # [ Density ] - Density of the falling leaves (Range: 0.000-5.000)
        mod["Input_35"] = 5.000 # [ Distance ] - How far the leaves travel (Range: 2.500-7.500)
        mod["Input_36"] = 0.500 # [ Spread ] - Spread of the leaves once they travel away from the tree (Range: 0.250-0.750)
        mod["Input_37"] = 0 # [ Seed ] - Random Seed (Range: 0-1000)
        mod["Input_38"] = 0.000 # [ Frame Offset ] - Offset to make the animation start early or later (Range: x-y)
        mod["Input_39"] = 0.150 # [ Particle Scale ] - Scale of the falling leaves (Range: 1.5xInput_21)
        mod["Input_40"] = 10.000 # [ Particle Rotation Speed ] - Speed of random rotation of the leaves (Range: 10.000)
        mod["Input_41"] = True # [ Scale Fade ] - xxx (Range: True/False)
        mod["Input_42"] = 1.000 # [ Turbulunce Strength ] - Strength of noise turbulance (Range: 1.000)
        mod["Input_43"] = 0.530 # [ Turbulence Scale ] - Scale of turbulence noise (Range: 0.530)
        mod["Input_44"] = 1.000 # [ Speed ] - Speed multiplier for leaves (Range: 1.000)        

        print("\n--- Updating Modifiers Based on Ethereum Address ---")

        # Print updates in a readable format
        print(f"[Base Count]            : {int(normalize(values[0], 3, 25))}  (Range: 3-25)")
        print(f"[Tree Seed]             : {int(normalize(values[1], 0, 1000))}  (Range: 0-1000)")        
        print(f"[Trunk Resolution]      : {int(normalize(values[2], 8, 256))}  (Range: 8-256)")        
        print(f"[Resolution]            : {int(normalize(values[3], 8, 64))}  (Range: 8-64)")        
        print(f"[Tree Distortion]       : {normalize(values[4], 0.000, 1.000):.3f}  (Range: 0.000-1.000)")
        print(f"[Trunk Noise Y]         : {normalize(values[5], -10.000, 10.000):.3f}  (Range: -10.000 to 10.000)")
        print(f"[Trunk Noise Z]         : {normalize(values[6], -10.000, 10.000):.3f}  (Range: -10.000 to 10.000)")
        print(f"[Split Angle]           : {normalize(values[7], 0.000, 45.000):.3f}  (Range: 0.000-45.000)")
        print(f"[Branch Length]         : {normalize(values[8], 1.000, 3.000):.3f}  (Range: 1.000-3.000)")
        print(f"[Branch Count]          : {int(normalize(values[9], 3, 15))}  (Range: 3-15)")
        print(f"[Branch Seed]           : {int(normalize(values[10], 0, 1000))}  (Range: 0-1000)")
        print(f"[Leaves Seed]           : {int(normalize(values[11], 0, 1000))}  (Range: 0-1000)")
        print(f"[Leaves Color R]        : {normalize(values[12], 0.000, 1.000):.3f}  (Range: 0.000-1.000)")
        print(f"[Leaves Color G]        : {normalize(values[13], 0.000, 1.000):.3f}  (Range: 0.000-1.000)")
        print(f"[Leaves Color B]        : {normalize(values[14], 0.000, 1.000):.3f}  (Range: 0.000-1.000)")
        print(f"[Leaves Noise Y]        : {normalize(values[15], -10.000, 10.000):.3f}  (Range: -10.000 to 10.000)")
        print(f"[Leaves Noise Z]        : {normalize(values[16], -10.000, 10.000):.3f}  (Range: -10.000 to 10.000)")
        print(f"[Vines Toggle]          : {'True' if values[17] > 127 else 'False'}")
        print(f"[Vine Gravity]          : {normalize(values[18], -5.000, 0.000):.3f}  (Range: -5.000 to 0.000)")
        print(f"[Vine Seed]             : {int(normalize(values[19], 0, 1000))}  (Range: 0-1000)")        
                
        # Apply values to modifiers       
        mod["Input_5"] = int(normalize(values[0], 3, 25))        # Base Count (3-25)
        mod["Input_6"] = int(normalize(values[1], 0, 1000))      # Tree Seed (0-1000)
        mod["Input_7"] = int(normalize(values[2], 8, 256))       # Trunk Resolution (8-256)
        mod["Input_10"] = int(normalize(values[3], 8, 64))       # Resolution (8-64)
        mod["Input_8"] = normalize(values[4], 0.000, 1.000)      # Tree Distortion (0.000-1.000)

        mod["Input_9"][1] = normalize(values[5], -10.000, 10.000)  # Trunk Noise Y
        mod["Input_9"][2] = normalize(values[6], -10.000, 10.000)  # Trunk Noise Z

        mod["Input_13"] = normalize(values[7], 0.000, 45.000)    # Split Angle (0.000-45.000)
        mod["Input_14"] = normalize(values[8], 1.000, 3.000)     # Branch Length (1.000-3.000)
        mod["Input_15"] = int(normalize(values[9], 3, 15))       # Branch Count (3-15)
        mod["Input_16"] = int(normalize(values[10], 0, 1000))    # Branch Seed (0-1000)

        mod["Input_26"] = int(normalize(values[11], 0, 1000))    # Leaves Seed (0-1000)
        mod["Input_4"][0] = normalize(values[12], 0.000, 1.000)  # Leaves Color R
        mod["Input_4"][1] = normalize(values[13], 0.000, 1.000)  # Leaves Color G
        mod["Input_4"][2] = normalize(values[14], 0.000, 1.000)  # Leaves Color B

        mod["Input_23"][1] = normalize(values[15], -10.000, 10.000)  # Leaves Noise Y
        mod["Input_23"][2] = normalize(values[16], -10.000, 10.000)  # Leaves Noise Z
        mod["Input_18"] = values[17] > 127                       # Vines Toggle (True/False)
        mod["Input_24"] = normalize(values[18], -5.000, 0.000)   # Vine Gravity (-5.000 to 0.000)
        mod["Input_25"] = int(normalize(values[19], 0, 1000))    # Vine Seed (0-1000)

        print("\n--- Modifier Updates Complete ---")

        # Forcefully invalidate the object's data-block
        obj.data.update()

        # Force the Dependency Graph to evaluate everything
        depsgraph = bpy.context.evaluated_depsgraph_get()
        depsgraph.update()

        # Redraw the entire viewport
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()

        print("Modifier inputs updated and viewport refreshed.")
    else:
        print("Modifier 'Fantasy_Tree_Gen' not found.")

# Set up render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.preferences.addons['cycles'].preferences.get_devices()
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.scene.cycles.samples = 512  # Increased samples for better quality
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = f"/outputs/lilytree_0x{eth_address}.png"

# Render the scene
bpy.ops.render.render(write_still=True)