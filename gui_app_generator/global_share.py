#Common shared variables

#Root window
main_window = None

#Canvas
input_area = None
message_area = None
control_area = None
output_area = None

#Consoles
msg_console = None
ai_console_left = None
ai_console_middle = None
ai_console_right = None

#User input
current_entry = 0
speed_entry = 0
flow_rate_entry = 0


#Progress bar
bar = None


#Event Handler
confirm_flag = False
reset_flag = False
exit_flag = False


#Hardware Monitor
cpu_info = None
cpu_model = None


#AI
AI_current = 0
AI_speed = 0
AI_flow = 0
AI_input_vector = None
AI_total = 0
AI_score = []