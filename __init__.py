# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Source Bone Renamer",
    "author" : "ASertacAkkaya",
    "description" : "A simple tool that renames your bones between source (L|R at the start) and Blender (L|R at the end) naming schemes.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Armature > Names, View 3D > Source Bone Renamer",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from .op_b2s import VIEW3D_OT_b2s
from .op_s2b import VIEW3D_OT_s2b
from .panel_sbr import VIEW3D_PT_source_bone_renamer

classes = (
    VIEW3D_OT_b2s, 
    VIEW3D_OT_s2b, 
    VIEW3D_PT_source_bone_renamer,
)

def rename_menu(self, context):
    self.layout.separator()
    self.layout.operator(VIEW3D_OT_b2s.bl_idname)
    self.layout.operator(VIEW3D_OT_s2b.bl_idname)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_edit_armature_names.append(rename_menu)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    bpy.types.VIEW3D_MT_edit_armature_names.remove(rename_menu)

