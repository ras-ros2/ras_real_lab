#!/usr/bin/bash

tmux new-session -d -s perception_session
tmux split-window -v -t perception_session:0

tmux send-keys -t perception_session:0.0 "ros2 run ras_perception aruco_detection.py" C-m
tmux send-keys -t perception_session:0.1 "ros2 run ras_perception logging_server.py" C-m

tmux attach-session -t perception_session