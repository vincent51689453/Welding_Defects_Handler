import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
import app_info
from PIL import Image,ImageTk

#Debug test control
debug_test = True

def update_console(consle,text):
    consle.configure(state='normal')
    consle.insert(tk.INSERT,text)    

def ai_console_output(gui_window):
    fontStyle = tkFont.Font(family=app_info.app_ai_console_fontstyle, size=app_info.app_ai_console_fontsize)

    console_ai_text = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_ai_box_w,height=app_info.text_ai_box_h,font=fontStyle)

    console_ai_text.grid(column=0,pady=10,padx=10)
    console_ai_text.configure(state='disabled',background=app_info.app_ai_console_background,foreground=app_info.app_ai_console_foreground)
    console_ai_text.place(x=app_info.text_ai_box_x,y=app_info.text_ai_box_y)

    return console_ai_text


def progress_bar_update(indicator,work_done):
    indicator["value"]=work_done


def progress_bar_init(gui_window):
    progress_bar = ttk.Progressbar(gui_window,orient="horizontal",length=app_info.bar_length,mode="determinate")
    progress_bar.place(x=app_info.bar_x,y=app_info.bar_y)
    #Set Initial value and maximum value
    progress_bar["value"] = 0
    progress_bar["maximum"] = 100
    return progress_bar



def console_init(gui_window):
    fontStyle = tkFont.Font(family=app_info.app_console_fontstyle, size=app_info.app_console_fontsize)

    console_text = scrolledtext.ScrolledText(gui_window, wrap=tk.WORD,\
        width=app_info.text_box_w,height=app_info.text_box_h,font=fontStyle)

    console_text.grid(column=0,pady=10,padx=10)
    console_text.configure(state='disabled',background=app_info.app_console_background,foreground=app_info.app_console_foreground)
    console_text.place(x=app_info.text_box_x,y=app_info.text_box_y)

    return console_text


def draw_control_elements(gui_window):
    #confirm button
    fontStyle = tkFont.Font(family=app_info.app_header_fontstyle, size=app_info.crtl_but_text_size)
    confirm_button = tk.Button(gui_window, text=app_info.crtl_but_conf_text, \
        bg=app_info.crtl_but_conf_bg,fg=app_info.crlt_but_conf_color,font=fontStyle,\
            highlightbackground=app_info.input_canvas_color,width=app_info.crtl_but_conf_width)
    confirm_button.place(x=app_info.crtl_but_conf_x,y=app_info.crtl_but_conf_y)

    #reset button
    fontStyle = tkFont.Font(family=app_info.app_header_fontstyle, size=app_info.crtl_but_text_size)
    reset_button = tk.Button(gui_window, text=app_info.crtl_but_reset_text, \
        bg=app_info.crtl_but_reset_bg,fg=app_info.crlt_but_reset_color,font=fontStyle,\
            highlightbackground=app_info.input_canvas_color,width=app_info.crtl_but_reset_width)
    reset_button.place(x=app_info.crtl_but_reset_x,y=app_info.crtl_but_reset_y)

def draw_input_bondary(gui_window):
    gui_window.create_line(app_info.line1_xmin,app_info.line1_ymin,\
        app_info.line1_xmax,app_info.line1_ymax,fill='white')       
    gui_window.create_line(app_info.line2_xmin,app_info.line2_ymin,\
        app_info.line2_xmax,app_info.line2_ymax,fill='white')
    gui_window.create_line(app_info.line3_xmin,app_info.line3_ymin,\
        app_info.line3_xmax,app_info.line3_ymax,fill='white')
    gui_window.create_line(app_info.line4_xmin,app_info.line4_ymin,\
        app_info.line4_xmax,app_info.line4_ymax,fill='white')

    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    zone_label = tk.Label(gui_window, text=app_info.input_zone_label, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.input_label_text_color)
    zone_label.place(x=app_info.input_label_x,y=app_info.input_label_y)

def draw_message_boundary(gui_window):
    gui_window.create_line(app_info.line1_msg_xmin,app_info.line1_msg_ymin,\
        app_info.line1_msg_xmax,app_info.line1_msg_ymax,fill='white')       
    gui_window.create_line(app_info.line2_msg_xmin,app_info.line2_msg_ymin,\
        app_info.line2_msg_xmax,app_info.line2_msg_ymax,fill='white')
    gui_window.create_line(app_info.line3_msg_xmin,app_info.line3_msg_ymin,\
        app_info.line3_msg_xmax,app_info.line3_msg_ymax,fill='white')
    gui_window.create_line(app_info.line4_msg_xmin,app_info.line4_msg_ymin,\
        app_info.line4_msg_xmax,app_info.line4_msg_ymax,fill='white')

    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    zone_label = tk.Label(gui_window, text=app_info.msg_zone_label, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.msg_label_text_color)
    zone_label.place(x=app_info.msg_label_x,y=app_info.msg_label_y)

def draw_control_boundary(gui_window): 
    gui_window.create_line(app_info.line1_crtl_xmin,app_info.line1_crtl_ymin,\
        app_info.line1_crtl_xmax,app_info.line1_crtl_ymax,fill='white')       
    gui_window.create_line(app_info.line2_crtl_xmin,app_info.line2_crtl_ymin,\
        app_info.line2_crtl_xmax,app_info.line2_crtl_ymax,fill='white')
    gui_window.create_line(app_info.line3_crtl_xmin,app_info.line3_crtl_ymin,\
        app_info.line3_crtl_xmax,app_info.line3_crtl_ymax,fill='white')
    gui_window.create_line(app_info.line4_crtl_xmin,app_info.line4_crtl_ymin,\
        app_info.line4_crtl_xmax,app_info.line4_crtl_ymax,fill='white')

    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    zone_label = tk.Label(gui_window, text=app_info.crtl_zone_label, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.crtl_label_text_color)
    zone_label.place(x=app_info.crtl_label_x,y=app_info.crtl_label_y)  

def draw_output_boundary(gui_window):
    gui_window.create_line(app_info.line1_out_xmin,app_info.line1_out_ymin,\
        app_info.line1_out_xmax,app_info.line1_out_ymax,fill='white')       
    gui_window.create_line(app_info.line2_out_xmin,app_info.line2_out_ymin,\
        app_info.line2_out_xmax,app_info.line2_out_ymax,fill='white')
    gui_window.create_line(app_info.line3_out_xmin,app_info.line3_out_ymin,\
        app_info.line3_out_xmax,app_info.line3_out_ymax,fill='white')
    gui_window.create_line(app_info.line4_out_xmin,app_info.line4_out_ymin,\
        app_info.line4_out_xmax,app_info.line4_out_ymax,fill='white')

    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    zone_label = tk.Label(gui_window, text=app_info.out_zone_label, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.out_label_text_color)
    zone_label.place(x=app_info.out_label_x,y=app_info.out_label_y)       


def input_current_init(gui_window):
    #input parameter 1 = input current
    #Set input parameter 1 label
    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    input_current_label = tk.Label(gui_window, text=app_info.app_input1_header, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.app_input1_text_color)
    input_current_label.place(x=app_info.app_input1_x,y=app_info.app_input1_y)
    
    #Set input parameter 1 input box
    input_current_entry = tk.Entry(gui_window, width=app_info.app_input1_box_w,\
        bg=app_info.app_input1_box_bg,fg=app_info.app_input1_box_fg)
    input_current_entry.place(x=app_info.app_input1_box_x,y=app_info.app_input1_box_y)

    return input_current_label, input_current_entry

def speed_init(gui_window):
    #input parameter 2 = current speed
    fontStyle = tkFont.Font(family=app_info.app_input2_fontstyle, size=app_info.app_input2_size)
    speed_label = tk.Label(gui_window, text=app_info.app_input2_header, font=fontStyle,\
        bg=app_info.app_input2_bg,fg=app_info.app_input2_text_color)
    speed_label.place(x=app_info.app_input2_x,y=app_info.app_input2_y)

    #Set input parameter 2 input box
    speed_entry = tk.Entry(gui_window, width=app_info.app_input2_box_w,\
        bg=app_info.app_input2_box_bg,fg=app_info.app_input2_box_fg)
    speed_entry.place(x=app_info.app_input2_box_x,y=app_info.app_input2_box_y)   

    return speed_label,speed_entry 

def flow_rate_init(gui_window):
    #input parameter 3 = flow rate
    fontStyle = tkFont.Font(family=app_info.app_input3_fontstyle, size=app_info.app_input3_size)
    flow_rate_label = tk.Label(gui_window, text=app_info.app_input3_header, font=fontStyle,\
        bg=app_info.app_input3_bg,fg=app_info.app_input3_text_color)
    flow_rate_label.place(x=app_info.app_input3_x,y=app_info.app_input3_y)

    #Set input parameter 3 input box
    flow_rate_entry = tk.Entry(gui_window, width=app_info.app_input3_box_w,\
        bg=app_info.app_input3_box_bg,fg=app_info.app_input3_box_fg)
    flow_rate_entry.place(x=app_info.app_input3_box_x,y=app_info.app_input3_box_y)   

    return flow_rate_label,flow_rate_entry 


def main_window_init():
    window = tk.Tk()

    #Set basic window title, size and background color
    window.title(app_info.app_main_title)
    window.geometry(app_info.app_main_geometry)
    window.configure(background=app_info.app_main_background)

    #Set header
    fontStyle = tkFont.Font(family=app_info.app_header_fontstyle, size=app_info.app_header_size, weight="bold")
    header_label = tk.Label(window, text=app_info.app_main_header, font=fontStyle, \
        bg=app_info.app_header_bg,fg=app_info.app_header_text_color)
    header_label.place(x=app_info.app_header_x,y=app_info.app_header_y)

    return window


def main():
    #Setup root window
    main_window = main_window_init()

   
    #Setup canvas for input zone
    input_area = tk.Canvas(main_window, width=app_info.input_canvas_w, height=app_info.input_canvas_h,\
        bg = app_info.input_canvas_color, bd = app_info.input_canvas_thick, highlightthickness=app_info.input_canvas_highlight)
    input_area.place(x=app_info.input_canvas_x,y=app_info.input_canvas_y)

    #Setup different input interfaces on input canvas
    current_label, current_entry = input_current_init(input_area)
    speed_label, speed_entry = speed_init(input_area)
    flow_rate_lable, flow_rate_entry = flow_rate_init(input_area)

    #Draw input boundary boxes
    draw_input_bondary(input_area)

    #Setup canvas for message zone
    message_area = tk.Canvas(main_window,width=app_info.msg_canvas_w, height=app_info.msg_canvas_h,\
        bg = app_info.msg_canvas_color, bd = app_info.msg_canvas_thick, highlightthickness=app_info.msg_canvas_highlight)
    message_area.place(x=app_info.msg_canvas_x,y=app_info.msg_canvas_y)

    #Draw message boundary boxes
    draw_message_boundary(message_area)

    #Setup canvas for control
    control_area = tk.Canvas(main_window,width=app_info.crtl_canvas_w, height=app_info.crtl_canvas_h,\
        bg = app_info.crtl_canvas_color, bd = app_info.crtl_canvas_thick, highlightthickness=app_info.crtl_canvas_highlight)
    control_area.place(x=app_info.crtl_canvas_x,y=app_info.crtl_canvas_y)

    #Draw control boundary boxes
    draw_control_boundary(control_area)

    #Draw control elements
    draw_control_elements(control_area)

    #Setup canvas for output zone
    output_area = tk.Canvas(main_window,width=app_info.out_canvas_w, height=app_info.out_canvas_h,\
        bg = app_info.out_canvas_color, bd = app_info.out_canvas_thick, highlightthickness=app_info.out_canvas_highlight)
    output_area.place(x=app_info.out_canvas_x,y=app_info.out_canvas_y)    

    #Draw output boundary boxes
    draw_output_boundary(output_area)

    #Import terminal 
    msg_console =console_init(message_area)

    #Import progress bar
    bar = progress_bar_init(control_area)
 

    #Import AI output console
    ai_console = ai_console_output(output_area)

    if(debug_test):
        #update progress bar
        progress_bar_update(bar,30)
        #Display text on different consoles
        update_console(msg_console,"msg_console")
        update_console(ai_console,"ai_console")

    
    main_window.mainloop()



if __name__ == "__main__":
    main()