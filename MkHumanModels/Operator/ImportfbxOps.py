import bpy

def main(context):
    bpy.ops.import_scene.fbx(filepath="//home//aqphungngoc//Projects//makeHuman//femaletestcm.fbx")

class importFBXfile(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importFBXfile"
    bl_label = "importFBXfile"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(importFBXfile)

def unregister():
    bpy.utils.unregister_class(importFBXfile)

if __name__ == "__main__":
    register()
    # test call