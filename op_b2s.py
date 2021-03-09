import bpy
import re

class VIEW3D_OT_b2s(bpy.types.Operator):
    bl_idname = "view3d.b2s"
    bl_label = "Blender To Source"
    bl_description = "Renames your bones from Blender to Source naming schemes."
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if (bpy.context.mode not in ["EDIT_ARMATURE", "OBJECT"]):
            print("This addon can only be used in Object or Edit Armature modes!")
            return {'CANCELLED'}

        if (bpy.context.mode == "EDIT_ARMATURE"):
            self.rename_bones(context.visible_bones)
        elif (bpy.context.mode == "OBJECT"):
            for armature in bpy.data.armatures:
                bones = armature.bones
                self.rename_bones(bones)
        return {'FINISHED'}
    
    def rename_bones(self, bones):
        for bone in bones:
                bone.name = re.sub("^ValveBiped.Bip01_(?P<bone_area>.+)\.(?P<bone_direction>[LR])$", "ValveBiped.Bip01_\g<bone_direction>_\g<bone_area>", bone.name)
