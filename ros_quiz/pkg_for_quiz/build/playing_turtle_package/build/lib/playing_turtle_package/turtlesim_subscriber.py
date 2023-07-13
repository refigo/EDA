import rclpy as rp
from rclpy.node import Node

from turtlesim.msg import Pose


class TurtlesimSubscriber(Node):

    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription_a = self.create_subscription(
            Pose,
            '/A/pose',
            self.callbackA,
            10)
        self.subscription_a # prevent unused variable warning

        self.subscription_b = self.create_subscription(
            Pose,
            '/B/pose',
            self.callbackB,
            10)
        self.subscription_b

        self.subscription_c = self.create_subscription(
            Pose,
            '/C/pose',
            self.callbackC,
            10)
        self.subscription_c

        self.subscription_d = self.create_subscription(
            Pose,
            '/D/pose',
            self.callbackD,
            10)
        self.subscription_d

    def printPose(self, msg):
        print("X : ", msg.x, ", Y : ", msg.y)

    def callbackA(self, msg):
        print("turtle_name: A", end=' ')
        self.printPose(msg)

    def callbackB(self, msg):
        print("turtle_name: B", end=' ')
        self.printPose(msg)

    def callbackC(self, msg):
        print("turtle_name: C", end=' ')
        self.printPose(msg)

    def callbackD(self, msg):
        print("turtle_name: D", end=' ')
        self.printPose(msg)

def main(args=None):
    rp.init(args=args)

    turtlesim_subscriber = TurtlesimSubscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
