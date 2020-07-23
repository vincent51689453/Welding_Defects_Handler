import tkinter as tk
import tkinter.font as tkFont
import app_info


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


    #input parater 1 = input current
    #Set input parameter 1 framework
    fontStyle = tkFont.Font(family=app_info.app_input1_fontstyle, size=app_info.app_input1_size)
    input_current_frame = tk.Label(window, text=app_info.app_input1_header, font=fontStyle,\
        bg=app_info.app_input1_bg,fg=app_info.app_input1_text_color)
    input_current_frame.place(x=app_info.app_input1_x,y=app_info.app_input1_y)
    
    #Set input parameter 1 input box
    input_current_entry = tk.Entry(window,  width=app_info.app_input1_box_w)
    input_current_entry.place(x=app_info.app_input1_box_x,y=app_info.app_input1_box_y)


    return window


def main():
    main_window = main_window_init()
    main_window.mainloop()



if __name__ == "__main__":
    main()