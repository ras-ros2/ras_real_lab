#!/usr/bin/bash

tmux new-session -d -s perception_session

tmux send-keys -t perception_session:0.0 "ros2 run ras_perception aruco_detection.py" C-m

tmux attach-session -t perception_session