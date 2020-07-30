from app_main import *
import global_share as gs
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import scale


def classification():
    update_console(gs.msg_console,"  \n")
    update_console(gs.msg_console,"[AI] Starting classifier... It may takes a while, depends on GPU\n")
    progress_ratio = 0

    nn_input = np.array([gs.AI_current,gs.AI_current,gs.AI_current, \
                         gs.AI_current,gs.AI_current,gs.AI_current, \
                         gs.AI_current,gs.AI_current,gs.AI_current,\
                         gs.AI_current,gs.AI_current,\
                         gs.AI_speed,gs.AI_flow])
    # standardizing the input feature
    nn_input = scale(nn_input)
    nn_input = np.array([nn_input])
    input_message= "[AI] Input vector: "+str(nn_input)+"\n"
    #update_console(gs.msg_console,input_message)
    print("input-vector:",nn_input)
    #Load network
    classifier = keras.models.load_model('./ANN_v2.h5')
    defects = classifier.predict(nn_input)   

    #Display
    input_message = "Input vector: " + str(nn_input) + "\n"
    update_console(gs.msg_console,input_message)

    print("Network Output: ",defects)
    raw_output_message = "[AI] Network Output:" + str(defects)+ "\n"
    update_console(gs.msg_console,raw_output_message)

    #Thresholding
    #0: Incomplete penetration
    #defects[:, 0] = (defects[:, 0] > 0.6)
    #1: Incomplete fusion
    #defects[:, 1] = (defects[:, 1] > 0.5)
    #2: Porosity
    #defects[:, 2] = (defects[:, 2] > 0.65)
    #3: Underfill
    #defects[:, 3] = (defects[:, 3] > 0.6)
    print("Thresholding: ",defects)
    thresh_output_message = "[AI] Defects:" + str(defects) + "\n"
    update_console(gs.msg_console,thresh_output_message)
    print("<<------------------------------------------------------------>>")   
 
    update_console(gs.msg_console,"---------------------------------------------------------\n")

    #update AI console
    output_1 = round(float(defects[:,0])*100,2)
    output_2 = round(float(defects[:,1])*100,2)
    output_3 = round(float(defects[:,2])*100,2)
    output_4 = round(float(defects[:,3])*100,2)

    ai_left_msg = "Incomplete penetration:  " + str(output_1) + "%"
    if(output_1 > 60):
        ai_left_msg += " > 60%  ==> FAILED"
    else:
        ai_left_msg += " < 60%  ==> PASS"
    update_console(gs.ai_console_left,ai_left_msg,False)

    ai_middle_msg = "Incomplete fusion:  " + str(output_2) + "%"
    if(output_2 > 50):
        ai_middle_msg += " > 50%  ==> FAILED"
    else:
        ai_middle_msg += " < 50%  ==> PASS"    
    update_console(gs.ai_console_middle,ai_middle_msg,False)

    ai_right_msg = "Porosity:  " + str(output_3) + "%"
    if(output_3 > 65):
        ai_right_msg += " > 65%  ==> FAILED"
    else:
        ai_right_msg += " < 65%  ==> PASSED"
    update_console(gs.ai_console_right,ai_right_msg,False)

    ai_extra_msg = "Underfill:  " + str(output_4) + "%"
    if(output_4 > 60):
        ai_extra_msg += " > 60%  ==> FAILED"
    else:
        ai_extra_msg += " < 60%  ==> PASS"   
    update_console(gs.ai_console_extra,ai_extra_msg,False)    

    progress_bar_update(gs.bar,progress_ratio)

    #update root window
    gs.main_window.update()


    progress_bar_update(gs.bar,100)
    update_console(gs.msg_console,"[AI] Finished... ")

    return True
    
