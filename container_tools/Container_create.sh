xhost +
sudo docker run --gpus all -it --device=/dev/video0:/dev/video0 -v /home/vincent/docker:/workspace/ -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -e XAUTHORITY -e NVIDIA_DRIVER_CAPABILITIES=all --env QT_X11_NO_MITSHM=1 -p 2002:8888 nvcr.io/nvidia/tensorflow:19.07-py3
