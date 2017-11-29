import bpy
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

def main(context, filepath):
    
    bpy.ops.import_anim.bvh(filepath)

class importFBXfile(Operator, ImportHelper):
    """Tooltip"""
    bl_idname = "object.importbvhanimdata"
    bl_label = "Import Human Skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    #Ham dieu kien de chay tien trinh (Phai co)
    def poll(cls, context):  
        return true
    # Ham thi hanh phuong thuc dieu khien tien trinh
    def execute(self, self.filepath, context):
        main(context, self.filepath)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(importFBXfile)

def unregister():
    bpy.utils.unregister_class(importFBXfile)

if __name__ == "__main__":
    register()
    # test call