from app_main import *
import global_share as gs
import app_ai_core as AI


def confirm_event():
    a,b,c = 0,0,0
    #When confirm button is pressed
    confirm_flag = True
    update_console(gs.msg_console,"[INFO] parameters are locked ...\n")
    update_console(gs.msg_console,"[INFO] starting AI analysis ...\n")
    #start progress bar to be 0%
    progress_bar_update(gs.bar,0)
 
    #Read user input
    if(len(gs.current_entry.get()) == 0):
        a = 0
    else:
        a = gs.current_entry.get()
    if(len(gs.speed_entry.get()) == 0):
        b = 0
    else:
        b = gs.speed_entry.get()    
    if(len(gs.flow_rate_entry.get()) == 0):
        c = 0
    else:
        c = gs.flow_rate_entry.get()
    update_console(gs.msg_console,"[INFO] Captured initial parameters ...\n")
    update_console(gs.msg_console,"[INFO] current: "+str(a)+ " speed: "+str(b)\
        +" flow_rate: "+str(c) +"\n")


def reset_event():
    #When reset button is pressed
    reset_flag = True
    progress_bar_update(gs.bar,0)
    #Remove console output
    clear_console(gs.msg_console)
    clear_console(gs.ai_console)

def exit_event():
    #When exit button is pressed
    exit_flag = True
    gs.main_window.destroy()

