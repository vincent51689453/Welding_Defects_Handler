from app_main import *
import global_share as gs


def confirm_lock():
    confirm_flag = True
    print("[INFO] Confirmed by user -> System locked up")
    update_console(gs.msg_console,"test\n")
