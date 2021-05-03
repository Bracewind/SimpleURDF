from urdf2.urdf2model import Link
from urdf2.urdf2Metamodel.Robot import Robot
from urdf2.urdf2Metamodel.World import World
from urdf2.urdf2Metamodel.Joint import Joint
from urdf2.urdf2Metamodel import JointType

from urdf2.urdfParser.URDFRepresentation import JOINT_PARENT, JOINT_CHILD, LINK

JOINT_TYPE_MAPPING = {"continuous": JointType.JOINT_CONTINUOUS}


class UrdfToUrdf2:
    def __init__(self):
        self.world = None

    # context contains element of direct neighbor and child, not children
    # of neighbor
    def _addToContext(self, context: dict, node):
        if node.URDF2type in context.keys():
            context[node.URDF2type].append(node)
        else:
            context[node.URDF2type] = [node]

    def _searchNodeByName(self, context: dict, nodeType: str, name: str):
        for node in context[nodeType]:
            if node.name == name:
                return node

    def createRobot(self, urdfRobot):
        links = []
        context = []
        for link in urdfRobot.link:
            linkURDF2 = self.createLink(link)
            links.append(linkURDF2)
            context.append({linkURDF2.name: linkURDF2})

        joints = []
        print()
        for joint in urdfRobot.joint:
            joints.append(self.createJoint(context, joint))

        robot = Robot(urdfRobot.get("name"), links, joints)
        return robot

    def createLink(self, urdfLink):
        linkURDF2 = Link(urdfLink.get("name"))
        return linkURDF2

    def createJoint(self, context, urdfJoint):
        jointType = JOINT_TYPE_MAPPING[urdfJoint.get("type")]
        joint = Joint(
            urdfJoint.get("name"),
            jointType,
            context[urdfJoint.get("parent")],
            context[urdfJoint.get("child")],
        )
        return joint

    def jointParentAction(self, context, linkName: str):
        context[JOINT_PARENT] = self._searchNodeByName(context, LINK, linkName)

    def jointChildAction(self, context, linkName: str):
        context[JOINT_CHILD] = self._searchNodeByName(context, LINK, linkName)
