#!/usr/bin/bash

tmux new-session -d -s main_session
tmux split-window -v -t main_session:0
tmux split-window -v -t main_session:0

tmux send-keys -t main_session:0.0 "ros2 run ras_aws_transport iot_receiver.py" C-m
tmux send-keys -t main_session:0.1 "ros2 run ras_moveit moveit_real_server" C-m
tmux send-keys -t main_session:0.2 "ros2 run ras_bt_framework TrajectoryRecordsService.py" C-m

tmux new-window -t main_session:1 -n 'robot'
tmux send-keys -t main_session:1.0 "ros2 launch ras_app_core main.launch.py" C-m

tmux new-window -t main_session:2 -n 'logging'
tmux split-window -v -t main_session:2
tmux split-window -v -t main_session:2
tmux send-keys -t main_session:2.0 "ros2 run ras_aws_transport log_sender.py" C-m
tmux send-keys -t main_session:2.1 "ros2 run ras_bt_framework executor" C-m
tmux send-keys -t main_session:2.2 "ros2 run ras_aws_transport gripper.py" C-m

tmux attach-session -t main_session