from ras_common.config.loaders.ras_config import RasObject

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import logging

def generate_launch_description():
    RasObject.init()
    launch = None
    logger = logging.getLogger('launch')

    if(RasObject.ras.real.mode == "real"):
        logger.info('Real mode')
        launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([FindPackageShare('ras_app_core'), '/launch', '/real.launch.py'])
        )

    elif(RasObject.ras.real.mode == "sim"):
        logger.info("Sim mode")
        launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([FindPackageShare('ras_app_core'), '/launch', '/sim.launch.py'])
        )

    else:
        logger.error("Invalid mode")

    return LaunchDescription([launch])