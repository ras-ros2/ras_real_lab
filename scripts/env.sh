source /opt/ros/humble/setup.bash
export RAS_APP_NAME=ras_robot_app
export RAS_APP_PATH=$(realpath $(dirname "${BASH_SOURCE[0]}")/..)
export RAS_WORKSPACE_PATH=$RAS_APP_PATH/ros2_ws
export IGN_GAZEBO_RESOURCE_PATH=$RAS_APP_PATH/assets/objects/old_models:$RAS_APP_PATH/third_party/gazebo_models:${IGN_GAZEBO_RESOURCE_PATH}
export RAS_ROBOT_MODE=sim
export RAS_MODE_SCRIPT=$RAS_APP_PATH/scripts/real_mode.bashrc
source $RAS_WORKSPACE_PATH/install/setup.bash
export IGN_PARTITION=$RAS_APP_NAME
export ROS_DOMAIN_ID=1

source_mode_script(){
    if [ -e $RAS_MODE_SCRIPT ]; then
        source $RAS_MODE_SCRIPT
    fi
}
source_mode_script

ras_app() { if [ -e /tmp/.RAS_RUN ]
    then
        echo App is Already Running
    else
        if [ -z "$1" ]; then
            echo "Using preset mode: $RAS_ROBOT_MODE"
        elif [ "$1" == "sim" ] || [ "$1" == "real" ]; then
            echo "export RAS_ROBOT_MODE=$1" > $RAS_MODE_SCRIPT
        else
            echo "Error: Invalid mode. Use 'sim' or 'real'."
            exit 1
        fi
        source_mode_script
        echo Starting App in $RAS_ROBOT_MODE mode
        touch /tmp/.RAS_RUN
        $RAS_APP_PATH/scripts/run.sh
        rm /tmp/.RAS_RUN
    fi
}

ras_kill() { tmux kill-session -t main_session ; }
