import numpy as np
from env.models.robots.robot import Robot
from env.mjcf_utils import xml_path_completion, array_to_string


class HDT(Robot):
    """HDT is a single-arm robot designed by HDT Global."""

    def __init__(
        self,
        use_torque=False,
        xml_path="robots/hdt_angler/robot.xml",
    ):
        if use_torque:
            xml_path = "robots/hdt_angler/robot_torque.xml"
        super().__init__(xml_path_completion(xml_path))

        self.bottom_offset = np.array([0, 0, -0.913])

    def set_base_xpos(self, pos):
        """
        Places the robot on position @pos.
        """
        node = self.worldbody.find("./body[@name='base']")
        node.set("pos", array_to_string(pos - self.bottom_offset))

    def set_base_xquat(self, quat):
        """
        Places the robot on position @quat.
        """
        node = self.worldbody.find("./body[@name='base']")
        node.set("quat", array_to_string(quat))

    def set_joint_damping(self, damping=np.array((0.1, 0.1, 0.1, 0.1, 0.1, 0.01))):
        """Set joint damping """
        body = self._base_body
        for i in range(len(self._link_body)):
            body = body.find("./body[@name='{}']".format(self._link_body[i]))
            joint = body.find("./joint[@name='{}']".format(self._joints[i]))
            joint.set("damping", array_to_string(np.array([damping[i]])))

    def set_joint_frictionloss(self, friction=np.array((0.1, 0.1, 0.1, 0.1, 0.1, 0.01))):
        """Set joint friction loss (static friction)"""
        body = self._base_body
        for i in range(len(self._link_body)):
            body = body.find("./body[@name='{}']".format(self._link_body[i]))
            joint = body.find("./joint[@name='{}']".format(self._joints[i]))
            joint.set("frictionloss", array_to_string(np.array([friction[i]])))

    @property
    def dof(self):
        return 6

    @property
    def joints(self):
        return ["joint{}".format(x) for x in range(1, 7)]

    @property
    def init_qpos(self):
        return np.array([0., 0., 0., 0., 0., 0.])

    @property
    def contact_geoms(self):
        return ["jaco_link_geom_{}".format(x) for x in range(7)]


    @property
    def contact_geoms(self):
        return ["link{}_collision".format(x) for x in range(1, 7)]

    @property
    def _base_body(self):
        node = self.worldbody.find("./body[@name='base']")
        return node

    @property
    def _link_body(self):
        return ["link1", "link2", "link3", "link4", "link5", "link6"]

    @property
    def _joints(self):
        return ["joint1", "joint2", "joint3", "joint4", "joint5", "joint6"]