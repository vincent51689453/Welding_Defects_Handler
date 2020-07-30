from app_main import *
import global_share as gs
import app_ai_core as AI


def confirm_event():
    #Clear all consoles
    clear_console(gs.ai_console_left)
    clear_console(gs.ai_console_middle)
    clear_console(gs.ai_console_right)
    clear_console(gs.msg_console)
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
    
    #Starts AI core
    gs.AI_current = a
    gs.AI_speed = b
    gs.AI_flow = c

    AI_anaylze = False

    print(gs.AI_flow)
    
    #AI analyze
    AI_anaylze = AI.classification()
 

def reset_event():
    #When reset button is pressed
    reset_flag = True
    progress_bar_update(gs.bar,0)
    #Remove console output
    clear_console(gs.msg_console)
    clear_console(gs.ai_console_left)
    clear_console(gs.ai_console_middle)
    clear_console(gs.ai_console_right)
    clear_console(gs.ai_console_extra)

def exit_event():
    #When exit button is pressed
    exit_flag = True
    gs.main_window.destroy()


def help_event():
    #When help button is pressed
    update_console(gs.msg_console,"<<<  Help Center  >>>\n")
    update_console(gs.msg_console,"1. Input one of the parameters that you want to fix\n")
    update_console(gs.msg_console,"2. Press confirm to start the AI generator\n")
    update_console(gs.msg_console,"3. The progress bar will be filled once the analyze is done\n")
    update_console(gs.msg_console,"4. The resutls will be displayed in <AI Output> console\n")
    update_console(gs.msg_console,"  \n")
    update_console(gs.msg_console,"** <Reset button> helps to clean all the consoles up\n")
    update_console(gs.msg_console,"** <Exit button> helps to close the program\n")
    update_console(gs.msg_console,"** <Help button> helps to open the help center\n")
    update_console(gs.msg_console,"** <Help button> helps to open the help center\n")
    update_console(gs.msg_console,"  \n")
    update_console(gs.msg_console,"** Progress bar is set to 80 percent as demonstration\n")
    progress_bar_update(gs.bar,80)




    

