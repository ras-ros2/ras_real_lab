#!/usr/bin/env python3

"""
Copyright (C) 2024 Sachin Kumar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

For inquiries or further information, you may contact:
Sachin Kumar
Email: info@opensciencestack.org
"""

import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
from xarm.wrapper import XArmAPI

GRIPPER_IP = "192.168.1.111"

class IntermediateGripperServer(Node):
    def __init__(self):
        super().__init__("intermediate_gripper_node")
        self.get_logger().info("Intermediate Gripper Server")
        self.use_real_gripper = self.declare_parameter("use_real_gripper", False)

        if self.use_real_gripper.value:
            self.gripper = XArmAPI(GRIPPER_IP)
            if self.gripper.connected():
                self.get_logger().info("Gripper Connected")
            else:
                self.get_logger().error("Gripper Connection Failed")
                exit(1)

        self.create_service(SetBool, "/open_gripper", self.gripper_callback)

    def gripper_callback(self, req: SetBool.Request, resp: SetBool.Response):
        if req.data:
            if self.use_real_gripper.value:
                res = self.gripper.open_lite6_gripper(False) # Open gripper immediately
                if res == 0:
                    self.get_logger().info("Gripper Opened")
                    resp.success = True
                else :
                    self.get_logger().error(f"Gripper Open Failed with error code: {res}")
                    resp.success = False
            else:
                self.get_logger().info("Fake Gripper Opened")
        else:
            if self.use_real_gripper.value:
                res = self.gripper.close_lite6_gripper(False) # Close gripper immediately
                if res == 0:
                    self.get_logger().info("Gripper Closed")
                    resp.success = True
                else :
                    self.get_logger().error(f"Gripper Close Failed with error code: {res}")
                    resp.success = False
            else:
                self.get_logger().info("Fake Gripper Closed")

        resp.success = True
        return resp

def main(args=None):
    rclpy.init(args=args)
    node = IntermediateGripperServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt (SIGINT)")
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
