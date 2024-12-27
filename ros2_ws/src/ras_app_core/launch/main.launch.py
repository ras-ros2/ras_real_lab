from ras_common.ras_common.config.loaders.ras_config import RasObject
from launch import LaunchDescription

def generate_launch_description():
    RasObject.init()
    if(RasObject.ras.real.mode == "real"):
        print("Real mode")
    else:
        print("Sim mode")

    return LaunchDescription()