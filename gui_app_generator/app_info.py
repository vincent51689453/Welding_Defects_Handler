#app parameter details

#main interface
#--------------------------------------------------------------------
app_main_title = 'CNERC AI Welding Parameters Generator'
app_main_geometry = '800x600'
app_main_background = '#292929'
#--------------------------------------------------------------------


#header
#--------------------------------------------------------------------
header_style_1 = "Lucida Grande"
header_style_2 = "Helvetica"
header_style_3 = "DejaVu Serif"

app_main_header = 'CNERC AI Welding Parameters Generator'
app_header_fontstyle = header_style_3
app_header_size = 15
app_header_x = 20
app_header_y = 20
app_header_bg = '#292929'
app_header_text_color = 'white'
#--------------------------------------------------------------------


#input boundary box canvas
#--------------------------------------------------------------------
input_canvas_w = 310
input_canvas_h = 195
input_canvas_color = '#292929'
input_canvas_thick = 0
input_canvas_highlight = 0
input_canvas_x = 20
input_canvas_y = 60

input_zone_label = "Weld Parameter Input"
input_label_x = 20
input_label_y = 10
input_label_text_color = 'yellow'

#Left
line1_xmin, line1_xmax, line1_ymin, line1_ymax = 0,0,0,input_canvas_h-1
#Right
line2_xmin, line2_xmax, line2_ymin, line2_ymax = input_canvas_w-1,input_canvas_w-1,0,input_canvas_h-1
#Top
line3_xmin, line3_xmax, line3_ymin, line3_ymax = 0,input_canvas_w-1,0,0
#Bottom
line4_xmin, line4_xmax, line4_ymin, line4_ymax = 0,input_canvas_w-1,input_canvas_h-1,input_canvas_h-1
#--------------------------------------------------------------------


#input current (input1)
#--------------------------------------------------------------------
input_current_style_1 = "Lucida Grande"
input_current_style_2 = "DejaVu Serif"

app_input1_header = 'Input Current (A):'
app_input1_fontstyle = input_current_style_2
app_input1_size = 12
#x,y based on canvas
app_input1_x = 20
app_input1_y = 50
app_input1_bg = '#292929'
app_input1_text_color = 'white'
app_input1_box_w = 8
app_input1_box_x = app_input1_x+180
app_input1_box_y = app_input1_y
app_input1_box_bg = app_input1_bg
app_input1_box_fg = 'white'
#--------------------------------------------------------------------

#current speed (input2)
#--------------------------------------------------------------------
current_speed_style_1 = "Lucida Grande"
current_speed_style_2 = "DejaVu Serif"


app_input2_header = 'Speed (In/min):'
app_input2_fontstyle = current_speed_style_2
app_input2_size = 12
#x,y based on canvas
app_input2_x = 20
#app_input2_y = app_input1_y + 40
app_input2_y = 90
app_input2_bg = '#292929'
app_input2_text_color = 'white'
app_input2_box_w = 8
app_input2_box_x = app_input2_x+180
app_input2_box_y = app_input2_y
app_input2_box_bg = app_input2_bg
app_input2_box_fg = 'white'
#--------------------------------------------------------------------


#flow rate (input3)
#--------------------------------------------------------------------
flow_rate_style_1 = "Lucida Grande"
flow_rate_style_2 = "DejaVu Serif"

app_input3_header = 'Flow Rate (l/min):'
app_input3_fontstyle = current_speed_style_2
app_input3_size = 12
#x,y based on canvas
app_input3_x = 20
#app_input3_y = app_input2_y + 40
app_input3_y = 130
app_input3_bg = '#292929'
app_input3_text_color = 'white'
app_input3_box_w = 8
app_input3_box_x = app_input3_x+180
app_input3_box_y = app_input3_y
app_input3_box_bg = app_input3_bg
app_input3_box_fg = 'white'
#--------------------------------------------------------------------

#message boundary box canvas
#--------------------------------------------------------------------
msg_canvas_w = 440
msg_canvas_h = 260
msg_canvas_color = '#292929'
msg_canvas_thick = 0
msg_canvas_highlight = 0
msg_canvas_x = 340
msg_canvas_y = 260

msg_zone_label = "AI System Console"
#based on message canvas
msg_label_x = 20
msg_label_y = 10
msg_label_text_color = 'yellow'

#Left
line1_msg_xmin, line1_msg_xmax, line1_msg_ymin, line1_msg_ymax = 0,0,0,msg_canvas_h-1
#Right
line2_msg_xmin, line2_msg_xmax, line2_msg_ymin, line2_msg_ymax = msg_canvas_w-1,msg_canvas_w-1,0,msg_canvas_h-1
#Top
line3_msg_xmin, line3_msg_xmax, line3_msg_ymin, line3_msg_ymax = 0,msg_canvas_w-1,0,0
#Bottom
line4_msg_xmin, line4_msg_xmax, line4_msg_ymin, line4_msg_ymax = 0,msg_canvas_w-1,msg_canvas_h-1,msg_canvas_h-1
#--------------------------------------------------------------------


#control boundary box canvas
#--------------------------------------------------------------------
crtl_canvas_w = 310
crtl_canvas_h = 260
crtl_canvas_color = '#292929'
crtl_canvas_thick = 0
crtl_canvas_highlight = 0
crtl_canvas_x = 20
crtl_canvas_y = 260

crtl_zone_label = "Control Pannel"
#based on message canvas
crtl_label_x = 20
crtl_label_y = 10
crtl_label_text_color = 'yellow'

crtl_hardware_label = "Detected hardware"
crtl_hardware_label_size = 9
crtl_hardware_label_x = 20
crtl_hardware_label_y = 190
crtl_hardware_label_color = "PaleTurquoise1"


#CPU monitor
crtl_cpu_label_1 = "CPU:"
crtl_cpu_label_x = 20
crtl_cpu_label_y = 210
crtl_cpu_label_color = "LightSkyBlue1"
crtl_cpu_label_size = 8

crtl_cpu_model_x = 50
crtl_cpu_model_y = crtl_cpu_label_y
crtl_cpu_model_color = "green2"

#GPU monitor check
crtl_gpu_label_1 = "GPU:"
crtl_gpu_label_x = 20
crtl_gpu_label_y = 230
crtl_gpu_label_color = "LightSkyBlue1"
crtl_gpu_label_size = 8
crtl_gpu_model_x = 50
crtl_gpu_model_y = crtl_gpu_label_y
crtl_gpu_label_2 = "NVIDIA GPU | CUDA | cuDNN Supported"
crtl_cpu_model_color = "green2"


#confirm button
crtl_but_text_size = 10
crtl_but_conf_text = 'Confirm'
crtl_but_conf_x = 20
crtl_but_conf_y = 45
crtl_but_conf_bg = 'cyan4'
crlt_but_conf_color = 'white'
crtl_but_conf_width = 8

#reset button
crtl_but_text_size = 10
crtl_but_reset_text = 'Reset'
crtl_but_reset_x = 160
crtl_but_reset_y = 45
crtl_but_reset_bg = 'cyan4'
crlt_but_reset_color = 'white'
crtl_but_reset_width = 8


#exit button
crtl_but_text_size = 10
crtl_but_exit_text = 'Exit'
crtl_but_exit_x = 20
crtl_but_exit_y = 95
crtl_but_exit_bg = 'cyan4'
crlt_but_exit_color = 'white'
crtl_but_exit_width = 8

#help button
crtl_but_text_size = 10
crtl_but_help_text = 'Help'
crtl_but_help_x = 160
crtl_but_help_y = 95
crtl_but_help_bg = 'cyan4'
crlt_but_help_color = 'white'
crtl_but_help_width = 8



#Left
line1_crtl_xmin, line1_crtl_xmax, line1_crtl_ymin, line1_crtl_ymax = 0,0,0,crtl_canvas_h-1
#Right
line2_crtl_xmin, line2_crtl_xmax, line2_crtl_ymin, line2_crtl_ymax = crtl_canvas_w-1,crtl_canvas_w-1,0,crtl_canvas_h-1
#Top
line3_crtl_xmin, line3_crtl_xmax, line3_crtl_ymin, line3_crtl_ymax = 0,crtl_canvas_w-1,0,0
#Bottom
line4_crtl_xmin, line4_crtl_xmax, line4_crtl_ymin, line4_crtl_ymax = 0,crtl_canvas_w-1,crtl_canvas_h-1,crtl_canvas_h-1
#--------------------------------------------------------------------


#output boundary box canvas
#--------------------------------------------------------------------
out_canvas_w = 760
out_canvas_h = 50
out_canvas_color = '#292929'
out_canvas_thick = 0
out_canvas_highlight = 0
out_canvas_x = 20
out_canvas_y = 530

out_zone_label = "AI Output"
#based on message canvas
out_label_x = 20
out_label_y = 12
out_label_text_color = 'yellow'

#Left
line1_out_xmin, line1_out_xmax, line1_out_ymin, line1_out_ymax = 0,0,0,out_canvas_h-1
#Right
line2_out_xmin, line2_out_xmax, line2_out_ymin, line2_out_ymax = out_canvas_w-1,out_canvas_w-1,0,out_canvas_h-1
#Top
line3_out_xmin, line3_out_xmax, line3_out_ymin, line3_out_ymax = 0,out_canvas_w-1,0,0
#Bottom
line4_out_xmin, line4_out_xmax, line4_out_ymin, line4_out_ymax = 0,out_canvas_w-1,out_canvas_h-1,out_canvas_h-1
#--------------------------------------------------------------------

#console terminal
#--------------------------------------------------------------------
app_console_fontstyle = "DejaVu Serif"
app_console_fontsize = 10
app_console_background = 'black'
app_console_foreground = 'white'
text_box_w = 48
text_box_h = 12
text_box_x = 20
text_box_y = 40
#--------------------------------------------------------------------


#progress bar
#--------------------------------------------------------------------
bar_text_fontstyle = "DejaVu Serif"
bar_text = "Progress"
bar_text_font_size = crtl_hardware_label_size
bar_text_color = crtl_hardware_label_color
bar_text_x = 20
bar_text_y = 140
bar_x = 20
bar_y = 165
bar_length = 250
#--------------------------------------------------------------------


#ai output console terminal
#--------------------------------------------------------------------
#Console_left
app_ai_console_l_fontstyle = "DejaVu Serif"
app_ai_console_l_fontsize = 12
app_ai_console_l_background = 'black'
app_ai_console_l_foreground = 'white'
text_ai_box_w_l = 18
text_ai_box_h_l = 1
text_ai_box_x_l = 130
text_ai_box_y_l = 10

#Console_middle
app_ai_console_m_fontstyle = "DejaVu Serif"
app_ai_console_m_fontsize = 12
app_ai_console_m_background = 'black'
app_ai_console_m_foreground = 'white'
text_ai_box_w_m = 18
text_ai_box_h_m = 1
text_ai_box_x_m = 340
text_ai_box_y_m = 10

#Console_right
app_ai_console_r_fontstyle = "DejaVu Serif"
app_ai_console_r_fontsize = 12
app_ai_console_r_background = 'black'
app_ai_console_r_foreground = 'white'
text_ai_box_w_r = 18
text_ai_box_h_r = 1
text_ai_box_x_r = 550
text_ai_box_y_r = 10

#--------------------------------------------------------------------

#configuration boundary box canvas
#--------------------------------------------------------------------
config_canvas_w = 440
config_canvas_h = 195
config_canvas_color = '#292929'
config_canvas_thick = 0
config_canvas_highlight = 0
config_canvas_x = 340
config_canvas_y = 60

config_zone_label = "Configuration"
#based on configuration canvas
config_label_x = 20
config_label_y = 10
config_label_text_color = 'yellow'

#Left
line1_config_xmin, line1_config_xmax, line1_config_ymin, line1_config_ymax = 0,0,0,config_canvas_h-1
#Right
line2_config_xmin, line2_config_xmax, line2_config_ymin, line2_config_ymax = config_canvas_w-1,config_canvas_w-1,0,config_canvas_h-1
#Top
line3_config_xmin, line3_config_xmax, line3_config_ymin, line3_config_ymax = 0,config_canvas_w-1,0,0
#Bottom
line4_config_xmin, line4_config_xmax, line4_config_ymin, line4_config_ymax = 0,config_canvas_w-1,config_canvas_h-1,config_canvas_h-1
#--------------------------------------------------------------------

#Configuration input: base metal
#--------------------------------------------------------------------
base_material_style_1 = "Lucida Grande"
base_material_style_2 = "DejaVu Serif"

base_material_label = "Base Metal:"
#based on configuration canvas
base_material_label_x = 20
base_material_label_y = 35
base_material_text_color = 'lawn green'

base_material_header = '-> Material:'
base_material_thickness_header = '-> Thickness:'
base_material_joint_header = '-> Joint Type:'

base_material_fontstyle = base_material_style_2
base_material_size = 11

base_material_material_content = "Steel"
base_material_thickness_content = "6mm"
base_material_joint_content = "Square Groove Butt Joint"

#Metal information(x,y based on canvas)
base_material_x = 25
base_material_y = 60
base_material_bg = '#292929'
base_material_material_text_color = 'white'
base_material_box_w = 6
base_material_box_x = base_material_x+120
base_material_box_y = base_material_y
base_material_box_bg = base_material_bg
base_material_box_fg = 'white'

#Thickness information(x,y based on canvas)
base_thickness_x = 210
base_thickness_y = 60
base_thickness_bg = '#292929'
base_thickness_text_color = 'white'
base_thickness_box_w = 6
base_thickness_box_x = base_thickness_x+110
base_thickness_box_y = base_thickness_y
base_thickness_box_bg = base_material_bg
base_thickness_box_fg = 'white'

#Joint_Type information(x,y based on canvas)
joint_type_x = 25
joint_type_y = 90
joint_type_bg = '#292929'
joint_type_text_color = 'white'
joint_type_box_w = 28
joint_type_box_x = joint_type_x+120
joint_type_box_y = joint_type_y
joint_type_box_bg = base_material_bg
joint_type_box_fg = 'white'
#--------------------------------------------------------------------

#Configuration input: fillerwire
#--------------------------------------------------------------------
fillerwire_style_1 = "Lucida Grande"
fillerwire_style_2 = "DejaVu Serif"

fillerwire_label = "Fillerwire:"
#based on configuration canvas
fillerwire_label_x = 20
fillerwire_label_y = 115
fillerwire_text_color = 'lawn green'

fillerwire_header = '-> Material:'
fillerwire_diameter_header = '-> Diameter:'
fillerwire_gas_header = 'Protective Gas:'

fillerwire_fontstyle = base_material_style_2
fillerwire_size = 11

fillerwire_material_content = "Steel"
fillerwire_diameter_content = "1.2mm"
fillerwire_gas_content = "MIGSHIELD"

#Metal information(x,y based on canvas)
fillerwire_material_x = 25
fillerwire_material_y = 135
fillerwire_bg = '#292929'
fillerwire_material_text_color = 'white'
fillerwire_material_box_w = 6
fillerwire_material_box_x = fillerwire_material_x+120
fillerwire_material_box_y = fillerwire_material_y
fillerwire_material_box_bg = base_material_bg
fillerwire_material_box_fg = 'white'

#Diameter information(x,y based on canvas)
fillerwire_diameter_x = 210
fillerwire_diameter_y = 135
fillerwire_diameter_bg = '#292929'
fillerwire_diameter_text_color = 'white'
fillerwire_diameter_box_w = 6
fillerwire_diameter_box_x = fillerwire_diameter_x+110
fillerwire_diameter_box_y = fillerwire_diameter_y
fillerwire_diameter_box_bg = base_material_bg
fillerwire_diameter_box_fg = 'white'

#Protective gas information(x,y based on canvas)
fillerwire_gas_x = 20
fillerwire_gas_y = 165
fillerwire_gas_bg = '#292929'
fillerwire_gas_text_color = 'white'
fillerwire_gas_box_w = 23
fillerwire_gas_box_x = fillerwire_gas_x+125
fillerwire_gas_box_y = fillerwire_gas_y
fillerwire_gas_box_bg = base_material_bg
fillerwire_gas_box_fg = 'white'
#--------------------------------------------------------------------

"""
TKinter design reference
1. http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

"""