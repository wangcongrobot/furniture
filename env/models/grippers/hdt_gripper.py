"""
Gripper for HDT Global's HDT Angler (has two fingers).
"""
import numpy as np
from env.mjcf_utils import xml_path_completion
from env.models.grippers.gripper import Gripper


class HDTGripperBase(Gripper):
    """
    Gripper for HDT Global's HDT Angler (has two fingers).
    """

    def __init__(self):
        super().__init__(xml_path_completion("grippers/hdt_gripper.xml"))

    def format_action(self, action):
        return action

    @property
    def init_qpos(self):
        return np.array([0.020833, 0.020833])

    @property
    def joints(self):
        return ["hdt_pincer_joint1", "hdt_pincer_joint2"]

    @property
    def dof(self):
        return 2

    @property
    def visualization_sites(self):
        return ["grip_site", "grip_site_cylinder"]

    @property
    def contact_geoms(self):
        return [
            "pincer_link1_collision",
            "pincer_link2_collision",
        ]

    @property
    def left_finger_geoms(self):
        return [
            "pincer_link1_collision",
        ]

    @property
    def right_finger_geoms(self):
        return [
            "pincer_link2_collision",
        ]


class HDTGripper(HDTGripperBase):
    """
    Modifies PandaGripperBase to only take one action.
    """

    def format_action(self, action):
        """
        1 => closed, -1 => open
        """
        assert len(action) == 1
        return np.array([1 * action[0], 1 * action[0]])

    @property
    def dof(self):
        return 1
