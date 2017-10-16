import bpy
from bpy.types import Panel

class SimpleToolPanel(Panel):
	bl_space_type ='VIEW3D'
	bl_region_type = 'TOOLS'
	bl_label = 'Tools Tab Label'
	bl_context = 'objectmode'
	bl_category = 'Mycube'
	
	def draw(self, context):
		layout = self.layout
		layout.operator('mesh.primitive_cube_add' , text = 'Add new cube')

def register():
	bpy.utils.register_class(SimpleToolPanel)
	
def unregister():
	bpy.utils.unregister_class(SimpleToolPanel)

if __name__=='__main__':
	register()
