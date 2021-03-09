import bpy
import re

class VIEW3D_OT_s2b(bpy.types.Operator):
    bl_idname = "view3d.s2b"
    bl_label = "Source To Blender"
    bl_description = "Renames your bones from Source to Blender naming schemes."
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
                bone.name = re.sub("^ValveBiped.Bip01_(?P<bone_direction>[LR])_(?P<bone_area>.+)$", "ValveBiped.Bip01_\g<bone_area>.\g<bone_direction>", bone.name)