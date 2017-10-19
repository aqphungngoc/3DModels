import bpy
from bpy.types import Operator

def main(context):
    bpy.ops.import_scene.fbx(filepath= "//home//aqphungngoc//Git//3DModels//MkHumanModels//Input//dress.fbx")
    

class importFBXfile(Operator):
    """Tooltip"""
    bl_idname = "object.importfbxcloth"
    bl_label = "Import Cloth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    #Ham dieu kien de chay tien trinh (Phai co)
    def poll(cls, context):  
        return true
    # Ham thi hanh phuong thuc dieu khien tien trinh
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