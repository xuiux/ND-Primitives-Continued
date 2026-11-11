import bpy
from bpy.props import IntProperty, BoolProperty, FloatProperty, FloatVectorProperty, StringProperty, EnumProperty
from .import __package__ as base_package
from .utils import draw_keymap, show_hide_gizmos_update_all, invert_rotation_gizmo_direction_update_all
from .add_menu import update_add_menu

BLENDER_VERSION = bpy.app.version
CONST_ITEMS = [("Grid", "MESH_PLANE"),
                ("Cube", "MESH_CUBE"),
                ("Circle", "MESH_CIRCLE"),
                ("UV Sphere", "MESH_UVSPHERE"),
                ("Ico Sphere", "MESH_ICOSPHERE"),
                ("Cylinder", "MESH_CYLINDER"),
                ("Cone", "MESH_CONE"),
                ("Torus", "MESH_TORUS"),
                ("Quad Sphere", "SPHERE"),
                ("Capsule", "MESH_CAPSULE"),
                ("Quad Capsule", "META_CAPSULE"),
                ("Mod Cylinder", "MOD_SCREW"),
                ("Spiral", "MOD_SCREW"),
                ("Tube", "SURFACE_NCYLINDER"),
                ("Other", "ADD"),
                # (".blend", "BLENDER"),
                ("CUSTOM_OP", "FILE_SCRIPT")]

CONST_ITEM_NAMES_CN = {
    "Grid": "栅格",
    "Cube": "立方体",
    "Circle": "圆形",
    "UV Sphere": "UV 球体",
    "Ico Sphere": "Ico 球体",
    "Cylinder": "圆柱体",
    "Cone": "圆锥体",
    "Torus": "圆环",
    "Quad Sphere": "四边面球体",
    "Capsule": "胶囊体",
    "Quad Capsule": "四边面胶囊体",
    "Mod Cylinder": "修改圆柱体",
    "Spiral": "螺旋",
    "Tube": "管状体",
    "Other": "其他",
    "CUSTOM_OP": "自定义操作符",
}

add_pie_menu_items = [
    (item[0], CONST_ITEM_NAMES_CN.get(item[0], item[0]), "", item[1], index)
    for index, item in enumerate(CONST_ITEMS)]

class ND_Primitives_Preferences(bpy.types.AddonPreferences):
    bl_idname = base_package 

    show_in_menu: EnumProperty(name="ND Primitives 显示位置", items=[("ADD_MESH", "网格菜单", "", "OUTLINER_OB_MESH", 1),
                                                           ("OWN_CATEGORY_IN_ADD_MENU", "网格菜单中的独立分类", "", "FILE_3D", 0),
                                                           ("OWN_MENU_CATEGORY", "添加菜单", "", "OBJECT_DATA", 2),
                                                           ("NONE", "无", "")], default="ADD_MESH", update=update_add_menu)# type: ignore
    # use_relative_scale: BoolProperty(name="Auto Scale", default=True, description="Default to Relative Scale Value") # type: ignore
    # default_scale: FloatProperty(name="Default Size", default=1.0, min=0.1, max=10.0, unit='LENGTH', description="Default Regular Scale Size Value") # type: ignore
    min_scale: FloatProperty(name="最小自动缩放", default=0.01, min=0.0001, max=10.0, unit='LENGTH', description="自动缩放使用的最小尺寸") # type: ignore
    apply_modifier_on_enter_edit_mode: BoolProperty(name="进入编辑模式时自动应用修改器", default=True, description="进入编辑模式时自动把修改器结果应用到网格，无需手动应用") # type: ignore
    delete_modifier: BoolProperty(name="删除修改器", default=False, description="进入编辑模式时删除修改器") # type: ignore
    show_gizmo: BoolProperty(name="显示操控器", default=True, description="显示操控器", update=show_hide_gizmos_update_all) # type: ignore
    auto_swith_to_modifier_tab: BoolProperty(name="自动切换到修改器标签页", default=True, description="添加几何体后自动切换到修改器标签页") # type: ignore
    invert_rotation_gizmo_direction: BoolProperty(name="反转旋转操控器方向", default=False, description="反转旋转操控器的方向" ,update=invert_rotation_gizmo_direction_update_all) # type: ignore
    origin_at_bottom: BoolProperty(name="原点在底部", default=False, description="默认将原点放在几何体底部，重启 Blender 后生效") # type: ignore

    pie_add_left: EnumProperty(name="左", items=add_pie_menu_items, default="UV Sphere") # type: ignore
    pie_add_right: EnumProperty(name="右", items=add_pie_menu_items, default="Cube") # type: ignore
    pie_add_bottom: EnumProperty(name="下", items=add_pie_menu_items, default="Cylinder") # type: ignore
    pie_add_top: EnumProperty(name="上", items=add_pie_menu_items, default="Grid") # type: ignore
    pie_add_top_left: EnumProperty(name="左上", items=add_pie_menu_items, default="Mod Cylinder") # type: ignore
    pie_add_top_right: EnumProperty(name="右上", items=add_pie_menu_items, default="Other") # type: ignore
    pie_add_bottom_left: EnumProperty(name="左下", items=add_pie_menu_items, default="Quad Sphere") # type: ignore
    pie_add_bottom_right: EnumProperty(name="右下", items=add_pie_menu_items, default="Circle") # type: ignore
    
    pie_add_custom_op_left: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_left: StringProperty(default="") # type: ignore

    pie_add_custom_op_right: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_right: StringProperty(default="") # type: ignore

    pie_add_custom_op_top: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_top: StringProperty(default="") # type: ignore

    pie_add_custom_op_bottom: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_bottom: StringProperty(default="") # type: ignore

    pie_add_custom_op_top_left: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_top_left: StringProperty(default="") # type: ignore

    pie_add_custom_op_top_right: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_top_right: StringProperty(default="") # type: ignore

    pie_add_custom_op_bottom_left: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_bottom_left: StringProperty(default="") # type: ignore

    pie_add_custom_op_bottom_right: StringProperty(default="") # type: ignore
    pie_add_custom_op_name_bottom_right: StringProperty(default="") # type: ignore
    
    def draw(self, context):
        layout = self.layout

        # General settings
        layout.label(text="常规设置：")
        box = layout.box()
        row = box.row()
        row.prop(self, "apply_modifier_on_enter_edit_mode")
        sub_row = row.row()
        sub_row.enabled = self.apply_modifier_on_enter_edit_mode
        sub_row.prop(self, "delete_modifier")
        row = box.row()
        row.prop(self, "auto_swith_to_modifier_tab")

        if BLENDER_VERSION >= (4, 3, 0):
            row = box.row()
            row.prop(self, "show_gizmo")
            sub_row = row.row()
            sub_row.enabled = self.show_gizmo
            sub_row.prop(self, "invert_rotation_gizmo_direction")
        else:
            row = box.row()
            row.label(text="操控器仅在 Blender 4.3 及以上版本可用", icon="ERROR")

        row = box.row()
        row.label(text="默认值：")
        row = box.row()
        row.prop(self, "origin_at_bottom")
        row = box.row()
        row.label(text="最小自动缩放：")
        row.scale_x = 0.55
        row.alignment = 'LEFT'
        row.prop(self, "min_scale")


        # menu
        row = layout.row()
        row.alignment = 'LEFT'
        row.scale_x = 1.25
        row.label(text="菜单设置：")
        row.prop(self, "show_in_menu", text="显示位置")

        box = layout.box()
        row.alignment = 'LEFT'
        row.scale_x = 1.2
        row = box.row()

        # pie menu customization
        draw_keymap(self, context, box)
        # Pie menu customization layout to resemble a pie menu structure

        spacer1_X = 0.55
        spacer2_X = 0.75
        all_X = 1.0
        all_Y = 1.2

        positions = [
            ("Top", "pie_add_top"),
            ("Top-Left", "pie_add_top_left", "pie_add_top_right"),
            ("Left", "pie_add_left", "pie_add_right"),
            ("Bottom-Left", "pie_add_bottom_left", "pie_add_bottom_right"),
            ("Bottom", "pie_add_bottom")
        ]

        def is_pie_menu_active():
            wm = bpy.context.window_manager
            for keyconfig in (wm.keyconfigs.user, wm.keyconfigs.addon):
                if keyconfig is None:
                    continue
                km = keyconfig.keymaps.get('Object Mode')
                if km is None:
                    continue
                kmi = km.keymap_items.get('wm.call_menu_pie')
                if kmi is not None:
                    return kmi.active
            return False 

        for index, pos in enumerate(positions):
            if index != 0:
                box.separator()
            row = box.row()
            row.alignment = 'CENTER'
            row.scale_x = all_X
            row.scale_y = all_Y
            keymap_active = is_pie_menu_active()
            row.enabled = keymap_active
            if len(pos) == 2:
                row.prop(self, pos[1], text="")
            else:
                row.prop(self, pos[1], text="")
                spacer = row.row()
                spacer.scale_x = spacer1_X if "Top" in pos[0] or "Bottom" in pos[0] else spacer2_X
                spacer.label(text=" ")
                row.prop(self, pos[2], text="")


        # Custom Operators for all positions
        custom_positions = [
            ("pie_add_left", "pie_add_custom_op_left", "pie_add_custom_op_name_left"),
            ("pie_add_right", "pie_add_custom_op_right", "pie_add_custom_op_name_right"),
            ("pie_add_bottom", "pie_add_custom_op_bottom", "pie_add_custom_op_name_bottom"),
            ("pie_add_top", "pie_add_custom_op_top", "pie_add_custom_op_name_top"),
            ("pie_add_top_left", "pie_add_custom_op_top_left", "pie_add_custom_op_name_top_left"),
            ("pie_add_top_right", "pie_add_custom_op_top_right", "pie_add_custom_op_name_top_right"),
            ("pie_add_bottom_left", "pie_add_custom_op_bottom_left", "pie_add_custom_op_name_bottom_left"),
            ("pie_add_bottom_right", "pie_add_custom_op_bottom_right", "pie_add_custom_op_name_bottom_right")
        ]

        position_names = {
            "pie_add_left": "左",
            "pie_add_right": "右",
            "pie_add_bottom": "下",
            "pie_add_top": "上",
            "pie_add_top_left": "左上",
            "pie_add_top_right": "右上",
            "pie_add_bottom_left": "左下",
            "pie_add_bottom_right": "右下",
        }
        for position, custom_op, custom_op_name in custom_positions:
            if getattr(self, position) == "CUSTOM_OP":
                sub_row = box.row()
                sub_row.alignment = 'LEFT'
                sub_row.prop(self, custom_op, text="自定义操作符（%s）" % position_names.get(position, position))
                sub_row.prop(self, custom_op_name, text="名称")

