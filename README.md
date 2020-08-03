# Welding_Defects_Handler

AI based welding parameters generator
-------------------------------------------
This gui can help you to generate the remaining two welding parameters using deep neural network once one of the parameters is fixed. Only the fixed parameter is required to input, then you can press "confirm" and it will do the maths.

### A. Basic User Interface
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/basic_generator_layout.png)

### B. Demo
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/generator_demo.gif)

AI based welding parameters classifier
-------------------------------------------
This gui can help you to classify the welding defects by inputting three parameters. After inputting the parameters, you can press "confirm" and it will do the maths.

### A. Basic User Interface
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/basic_classifier_layout.png)

### B. Demo
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/classifier_demo.gif)

Training MLP
-------------------------------------------
If you want to configure your own MLP and even change the architecture of the network, you can edit *neural_network/welding_classification/main.py".*

Afterward, you can run **python3 main.py**.

### A. ANN_V1
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/ANN_V1/ANN_v1_Architecture.png)

### B. ANN_V2
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/ANN_V2/ANN_Architecture_85.png)


### C. ANN_V3
![image](https://github.com/vincent51689453/Welding_Defects_Handler/blob/master/git_image/ANN_V3/ANN_v3_Architecture.png)


Docker Hub 
-------------------------------------------
The enviroment and necessary packages are all packed in this docker image.

https://hub.docker.com/repository/docker/vincent51689453/cnerc_ai_welding
