# based on code from UV Toolkits Pie Menus https://extensions.blender.org/add-ons/uv-toolkit/
import bpy
from bpy.types import Menu
from .utils import get_addon_prefs
from .addon_preferences import CONST_ITEMS, CONST_ITEM_NAMES_CN

# need to profile!!
class AddModifierPie(Menu):
    bl_idname = "ND_PRIMITIVES_MT_add_objects_pie_menu"
    bl_label = "ND 基础几何体饼菜单" 

    @staticmethod
    def get_operator_name(context, custom_op):
        custom_op = custom_op.split(".")
        if 3 < len(custom_op):
            if hasattr(bpy.ops, custom_op[2]):
                op_category = getattr(bpy.ops, custom_op[2])
                op_id_end_line = custom_op[3].find("(")
                op_id = custom_op[3][:op_id_end_line]
                op = getattr(op_category, op_id)
                return op.get_rna_type().name
        return "未知操作符"

    def pie_item(self, context, pie_property, custom_op, custom_op_name):
        layout = self.layout
        pie = layout.menu_pie()
        if pie_property == "CUSTOM_OP":
            if custom_op_name:
                op_name = custom_op_name
            else:
                op_name = self.get_operator_name(context, custom_op)
            pie.operator("uv.toolkit_execute_custom_op", text=op_name).exec_op = custom_op

        elif pie_property == "Other":
            if context.mode == 'EDIT_MESH':
                pie.operator("wm.call_menu", text="其他", icon="ADD").name = "VIEW3D_MT_mesh_add"  # RIGHT TOP
            else:
                pie.operator("wm.call_menu", text="其他", icon="ADD").name = "VIEW3D_MT_add"  # RIGHT TOP
        else:
            type_name = pie_property.split("_")[-1]
            display_name = CONST_ITEM_NAMES_CN.get(type_name, type_name)
            icon = [item[1] for item in CONST_ITEMS if item[0] == type_name][0]
            pie.operator("mesh.add_nd_primitive", text=display_name, icon=icon).type = type_name


    def draw(self, context):
        # import time
        # exec_time = time.time() 
        addon_prefs = get_addon_prefs()
        self.pie_item(context,
                      addon_prefs.pie_add_left,
                      addon_prefs.pie_add_custom_op_left,
                      addon_prefs.pie_add_custom_op_name_left)  # 4
        self.pie_item(context,
                      addon_prefs.pie_add_right,
                      addon_prefs.pie_add_custom_op_right,
                      addon_prefs.pie_add_custom_op_name_right)  # 6
        self.pie_item(context,
                      addon_prefs.pie_add_bottom,
                      addon_prefs.pie_add_custom_op_bottom,
                      addon_prefs.pie_add_custom_op_name_bottom)  # 2
        self.pie_item(context,
                      addon_prefs.pie_add_top,
                      addon_prefs.pie_add_custom_op_top,
                      addon_prefs.pie_add_custom_op_name_top)  # 8
        self.pie_item(context,
                      addon_prefs.pie_add_top_left,
                      addon_prefs.pie_add_custom_op_top_left,
                      addon_prefs.pie_add_custom_op_name_top_left)  # 7
        self.pie_item(context,
                      addon_prefs.pie_add_top_right,
                      addon_prefs.pie_add_custom_op_top_right,
                      addon_prefs.pie_add_custom_op_name_top_right)  # 9
        self.pie_item(context,
                      addon_prefs.pie_add_bottom_left,
                      addon_prefs.pie_add_custom_op_bottom_left,
                      addon_prefs.pie_add_custom_op_name_bottom_left)  # 1
        self.pie_item(context,
                      addon_prefs.pie_add_bottom_right,
                      addon_prefs.pie_add_custom_op_bottom_right,
                      addon_prefs.pie_add_custom_op_name_bottom_right)  # 3
        # print(f"Total Time: {time.time() - exec_time:.12f} seconds")
