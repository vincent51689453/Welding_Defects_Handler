from app_main import *
import global_share as gs


def confirm_event():
    #When confirm button is pressed
    confirm_flag = True
    update_console(gs.msg_console,"[INFO] Manual inputs are confirmed\n")
    update_console(gs.msg_console,"[INFO] Parameters are locked\n")
    update_console(gs.msg_console,"[INFO] Starting AI analysis...\n")
    #start progress bar to be 1%
    progress_bar_update(gs.bar,1)

def reset_event():
    #When reset button is pressed
    reset_flag = True
    update_console(gs.msg_console,"[INFO] Restarting system\n")
    update_console(gs.msg_console,"[INFO] Done!\n")
    progress_bar_update(gs.bar,0)

def exit_event():
    #When exit button is pressed
    exit_flag = True
    gs.main_window.destroy()

