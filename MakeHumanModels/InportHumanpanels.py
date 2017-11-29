import bpy
from bpy.types import Panel

class importHumanPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Import Models" 
    bl_idname = "OBJECT_HumanModel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = 'objectmode'
    bl_category = '3DBuildModels'

    def draw(self, context):
        layout = self.layout

        

        row = layout.row()
        row.label(text="Import Human", icon='WORLD_DATA')

        

        row = layout.row()
        row.operator('import_scene.fbx', text = 'Import Human Models')
        row = layout.row()
        row.operator('import_scene.fbx', text = 'Import Cloth')
        row = layout.row()
        row.operator('import_anim.bvh', text = 'Import Anim Data')
        
        # row = layout.row()
        # row.label(text="Working!", icon='WORLD_DATA')
        
        # obj = context.object
        # rowa = layout.row()
        # rowa.label(text="Active object is: " + obj.name)
        # rowa = layout.row()
        # rowa.prop(obj, "name")


        # row = layout.row()
        # row.operator('object.move_x', text = 'Enable Motion Tracking')
        # row = layout.row()
        # row.operator('object.move_x', text = 'Make Pingroup')
        # row = layout.row()
        # row.operator('object.move_x', text = 'Enable Cloth Sims')
        # row = layout.row()
        # row.operator('object.move_x', text = 'Save Cloth Anim Data')
        # row = layout.row()
        # row.operator('object.move_x', text = 'Export All')


def register():
    bpy.utils.register_class(importHumanPanel)


def unregister():
    bpy.utils.unregister_class(importHumanPanel)


if __name__ == "__main__":
    register()