from app_main import *
import global_share as gs


def confirm_lock():
    confirm_flag = True
    update_console(gs.msg_console,"[INFO] Manual inputs are confirmed\n")
    update_console(gs.msg_console,"[INFO] Parameters are locked\n")
    update_console(gs.msg_console,"[INFO] Starting AI analysis...\n")
    #start progress bar to be 1%
    progress_bar_update(gs.bar,1)