# from ras_common.config.loaders.ras_config import RasObject
from ras_common.globals import RAS_ROBOT_MODE

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import logging
from launch_ros.actions import Node

def generate_launch_description():
    launch = None
    gripper_node = Node(
            package='ras_app_main',
            executable='intermediate_gripper_server.py',
            name='intermediate_gripper_server',
            output='screen',
            parameters=[{'use_real_gripper': True if RAS_ROBOT_MODE == "real" else False}]
        )
    logger = logging.getLogger('launch')

    if(RAS_ROBOT_MODE == "real"):
        logger.info('Real mode')
        launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([FindPackageShare('ras_app_main'), '/launch', '/real.launch.py'])
        )

    elif(RAS_ROBOT_MODE == "sim"):
        logger.info("Sim mode")
        launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([FindPackageShare('ras_app_main'), '/launch', '/sim.launch.py'])
        )

    else:
        logger.error("Invalid mode",RAS_ROBOT_MODE)

    return LaunchDescription([launch])