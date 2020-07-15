import numpy as np
from env.models.robots.robot import Robot
from env.mjcf_utils import xml_path_completion, array_to_string


class HDT(Robot):
    """HDT is a witty single-arm robot designed by HDT Global Robotics."""

    def __init__(self):
        super().__init__(xml_path_completion("robots/hdt_angler/robot.xml"))

        self.bottom_offset = np.array([0, 0, -0.913])

    def set_base_xpos(self, pos):
        """Places the robot on position @pos."""
        node = self.worldbody.find("./body[@name='base']")
        node.set("pos", array_to_string(pos - self.bottom_offset))

    def set_base_xquat(self, quat):
        """Places the robot on position @quat."""
        node = self.worldbody.find("./body[@name='base']")
        node.set("quat", array_to_string(quat))

    def is_robot_part(self, geom_name):
        """Checks if name is part of robot"""
        arm_parts = geom_name in ['right_l2_geom2', 'right_l3_geom2', 'right_l4_geom2', 'right_l5_geom2', 'right_l6_geom2']
        gripper_parts = geom_name in ['l_finger_g0', 'l_finger_g1', 'l_fingertip_g0', 'r_finger_g0', 'r_finger_g1', 'r_fingertip_g0']
        return arm_parts or gripper_parts

    @property
    def dof(self):
        return 6

    @property
    def joints(self):
        return ["joint{}".format(x) for x in range(1, 7)]

    @property
    def init_qpos(self):
        # return np.array([0, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161])
        # 0: base, 1: 1st elbow, 3: 2nd elbow 5: 3rd elbow
        return np.array([0., 0., 0., 0., 0., 0.])

