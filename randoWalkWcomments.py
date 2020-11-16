import bpy
import random

#Importantly, I'm using the 'bpy' module for Blender 3D. There's documentation online by the Blender Foundation
#This script will only work if you copy and paste the script into the scripting workspace in a '.blend' file

size_range = 30


bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.delete(use_global=False) 

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')
bpy.ops.mesh.merge(type='CENTER') #Adding a cube and then merging it into a single vertex

def calculateTransform():
    rand_num = random.randint(0,5)
    xyz_list = ['x','y','z']
    xyz_randomizer = random.choice(xyz_list) #here this is weird. But I want to select vertices and move them in a random direction, but always at 90 degrees
    if xyz_randomizer == 'x':
        return(rand_num,0,0)
    elif xyz_randomizer == 'y':
        return(0,rand_num,0)
    elif xyz_randomizer == 'z': #so this function will only return a new position with only one of x, y, z altered. This way you get a very blocky shape
        return (0,0,rand_num)

for i in range(1,size_range):
    xyz = calculateTransform()
    try:
        bpy.ops.mesh.select_random(percent=10, seed=10) #this will select random vertices in an object, and then extrude them to 'xyz'
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":xyz, "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
    except:
        print('No vertices randomly selected') #sometimes, randomly, no vertices are selected. Handled here
        pass
        
 #I use SIZE_RANGE in order to control complexity. I think 200 crashed my computer, but 50 creates a huge blocky object that, when wireframed in blender, looks pretty cool
