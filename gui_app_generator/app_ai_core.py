from app_main import *
import global_share as gs
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import scale

def generate_input_vector(current,speed,flow_rate):
    anchor = 0
    output = []

    counter = 0

    current = int(current)
    speed = int(speed)
    flow_rate = int(flow_rate)
    
    #step = 40 (default)
    min_current,max_current= 180,300
    step_of_current = 40
    #step = 4 (default)
    min_speed,max_speed = 6,18
    step_of_speed = 4
    #step = 5 (default)
    min_flow,max_flow = 3,18
    step_of_flow = 5

    update_console(gs.msg_console,"  \n")
    update_console(gs.msg_console,"[AI] Starts creating input vectors..\n")

    #find fixed and variable parameters
    if((current > 0) and (speed == 0) and (flow_rate == 0)):
        update_console(gs.msg_console,"[AI] Anchor = current\n")
        anchor = 0

    if((current == 0) and (speed > 0) and (flow_rate == 0)):
        update_console(gs.msg_console,"[AI] Anchor = speed\n")
        anchor = 1

    if((current == 0) and (speed == 0) and (flow_rate > 0)):
        update_console(gs.msg_console,"[AI] Anchor = flow rate\n") 
        anchor = 2

    #Fix current, gerenate speed and flow rate
    if(anchor == 0):
        speed = min_speed
        flow_rate = min_flow
        #Generate speed
        while(speed<=max_speed):
            #Generate flow_rate
            while(flow_rate<=max_flow):
                input_vector = np.array([current,current,current,current,\
                                        current,current,current,current,\
                                        current,current,current,speed,flow_rate])
                output.append(input_vector)
                counter += 1
                #Step of flow rate
                flow_rate += step_of_flow
            #Step of speed
            speed += step_of_speed
            #Reset
            flow_rate = min_flow

        update_console(gs.msg_console,"[AI] Done!\n") 
        return output,counter

    #Fix speed, gerenate current and flow rate
    if(anchor == 1):
        current = min_current
        flow_rate = min_flow
        #Generate current
        while(current<=max_current):
            #Generate flow_rate
            while(flow_rate<=max_flow):
                input_vector = np.array([current,current,current,current,\
                                        current,current,current,current,\
                                        current,current,current,speed,flow_rate])
                output.append(input_vector)
                counter += 1
                #Step of flow rate
                flow_rate += step_of_flow
            #Step of current
            current += step_of_current
            #Reset
            flow_rate = min_flow

        update_console(gs.msg_console,"[AI] Done!\n") 
        return output,counter

     #Fix flow_rate, gerenate current and speed
    if(anchor == 2):
        current = min_current
        speed = min_speed
        #Generate current
        while(current<=max_current):
            #Generate flow_rate
            while(speed<=max_speed):
                input_vector = np.array([current,current,current,current,\
                                        current,current,current,current,\
                                        current,current,current,speed,flow_rate])
                output.append(input_vector)
                counter += 1
                #Step of flow rate
                speed += step_of_speed
            #Step of current
            current += step_of_current
            #Reset
            speed = min_speed

        update_console(gs.msg_console,"[AI] Done!\n") 
        return output,counter  

def classification(ai_input,iterations):
    i = 0
    raw = []
    update_console(gs.msg_console,"  \n")
    update_console(gs.msg_console,"[AI] Starting classifier... It may takes a while, depends on GPU\n")
    print(iterations)
    progress_ratio = 0
    #Try every vector
    while(i<iterations):
        nn_input = ai_input[i]
        print("<<------------------------- Iteration ------------------------->>")
        input_message= "[AI] Input vector: "+str(nn_input)+"\n"
        #update_console(gs.msg_console,input_message)
        print("input-vector:",nn_input)
        # standardizing the input feature
        nn_input = scale(nn_input)
        nn_input = np.array([nn_input])
        classifier = keras.models.load_model('./ANN_200.h5')
        defects = classifier.predict(nn_input)

        defects_raw = defects

        #Store to global share parameter (raw)
        raw.append(defects_raw)
        

        #Display
        input_message = "Input vector: " + str(nn_input) + "\n"
        update_console(gs.msg_console,input_message)


        update_console(gs.msg_console,"[AI] Iteration #"+str(i)+":\n")
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
        #print("Thresholding: ",defects)
        print("<<------------------------------------------------------------>>")
        
 
        update_console(gs.msg_console,"---------------------------------------------------------\n")

        progress_ratio = int(i/iterations*100)

        progress_bar_update(gs.bar,progress_ratio)

        #update root window
        gs.main_window.update()

        nn_input = None
        classifier = None
        defects = None
        sc = None
        defects = None

        i+=1

    progress_bar_update(gs.bar,100)
    update_console(gs.msg_console,"[AI] Finished... ")

    return True,i,raw
    

def optimization(score_list,iterations):
    i = 0
    min_score = 999.99
    min_index = 0
    nn_1,nn_2,nn_3,nn_4 = 0.0,0.0,0.0,0.0
    error_1,error_2,error_3,error_4 = False,False,False,False
    update_console(gs.msg_console,"[AI] Total numbers of parameters: "+str(iterations)+"\n")
    update_console(gs.msg_console,"[AI] Starts optimizing parameters.. \n")
    while(i<(iterations-1)):
        #i = each prediciton output
        #0 = extract 1d vector
        #0-4 : sum of scores
        score = float(score_list[i][0][0]) + float(score_list[i][0][1]) + \
                float(score_list[i][0][2]) + float(score_list[i][0][3])

        #update_console(gs.msg_console,"Score: "+str(score)+"\n")    
        print("score: ", score)

        if (score < min_score):
            min_score = score
            nn_1 = float(score_list[i][0][0])*100
            nn_1 = round(nn_1,2)
            if(nn_1>60): error_1 = True
            nn_2 = float(score_list[i][0][1])*100
            nn_2 = round(nn_2,2)
            if(nn_2>50): error_2 = True
            nn_3 = float(score_list[i][0][2])*100
            nn_3 = round(nn_3,2)
            if(nn_3>65): error_3 = True
            nn_4 = float(score_list[i][0][3])*100
            nn_4 = round(nn_4,2)
            if(nn_4>50): error_4 = True
            min_index = i

        i+=1

    #Output final results
    print("Optimized score index:",min_score)
    print("Minimum score index:",min_index)
    print("Parameters are: ",gs.AI_input_vector[min_index])
    print("Minimum score:",score)

    #Update to AI output console
    #Disable auto scroll
    update_console(gs.ai_console_left,"Current = " + str(gs.AI_input_vector[min_index][1])+"\n",False)
    update_console(gs.ai_console_middle,"Speed = " + str(gs.AI_input_vector[min_index][11])+"\n",False)
    update_console(gs.ai_console_right,"Flow = " + str(gs.AI_input_vector[min_index][12])+"\n",False)

    #Update to message console
    update_console(gs.msg_console,"******************************************************** \n") 
    update_console(gs.msg_console,"[AI] Here are the optimized parameters... \n") 
    update_console(gs.msg_console,"\n")
    update_console(gs.msg_console,"[AI] Risk evaluations: \n")

    message_penetration = "[AI] Incomplete penetration -> " + str(nn_1) + "%"
    if(error_1 == True):
        message_penetration += "  --- [FAILED]\n"
    else:
        message_penetration += "  --- [PASSED]\n" 

    message_fusion = "[AI] Incomplete fusion -> " + str(nn_2) + "%"
    if(error_2 == True):
        message_fusion += " --- [FAILED]\n"
    else:
        message_fusion += " --- [PASSED]\n"

    message_porosity = "[AI] Porosity -> " + str(nn_3) + "%"
    if(error_3 == True):
        message_porosity += " --- [FAILED]\n"
    else:
        message_porosity += " --- [PASSED]\n"   

    message_underfill = "[AI] Underfill -> " + str(nn_4) + "%"
    if(error_4 == True):
        message_underfill += " --- [FAILED]\n"
    else:
        message_underfill += " --- [PASSED]\n"  

    update_console(gs.msg_console,message_penetration)
    update_console(gs.msg_console,message_fusion)
    update_console(gs.msg_console,message_porosity)
    update_console(gs.msg_console,message_underfill)
    update_console(gs.msg_console,"******************************************************** \n") 

