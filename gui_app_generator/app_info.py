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
input_canvas_w = 300
input_canvas_h = 180
input_canvas_color = '#292929'
input_canvas_thick = 0
input_canvas_highlight = 0
input_canvas_x = 20
input_canvas_y = 60

input_zone_label = "Manual Input"
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
msg_canvas_h = 460
msg_canvas_color = '#292929'
msg_canvas_thick = 0
msg_canvas_highlight = 0
msg_canvas_x = 340
msg_canvas_y = 60

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
crtl_canvas_w = 300
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
text_box_w = 49
text_box_h = 24
text_box_x = 20
text_box_y = 40
#--------------------------------------------------------------------


#progress bar
#--------------------------------------------------------------------
bar_x = 20
bar_y = 230
bar_length = 250
#--------------------------------------------------------------------


#ai output console terminal
#--------------------------------------------------------------------

app_ai_console_fontstyle = "DejaVu Serif"
app_ai_console_fontsize = 12
app_ai_console_background = 'black'
app_ai_console_foreground = 'white'
text_ai_box_w = 60
text_ai_box_h = 1
text_ai_box_x = 130
text_ai_box_y = 10

#--------------------------------------------------------------------
"""
TKinter design reference
1. http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

"""