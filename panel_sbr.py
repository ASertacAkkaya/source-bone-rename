import bpy

class VIEW3D_PT_source_bone_renamer(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_source_bone_renamer"
    bl_label = "Source Bone Renamer"
    bl_category = "Source Bone Renamer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("view3d.b2s", text="Blender to Source")
        row = layout.row()
        row.operator("view3d.s2b", text="Source to Blender")