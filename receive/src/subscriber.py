#!/usr/bin/env python


import rospy
from std_msgs.msg import String

def callback(data):
    q = float(0.15)
    k = float(data.data) / q
    pub = rospy.Publisher("/kthfs/result", String, queue_size=10)
    rospy.loginfo("%s", k)
    pub.publish(str(k))
    rate = rospy.Rate(20)
    rate.sleep()

def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("nagarajan", String, callback)
    rate = rospy.Rate(20)
    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    listener()
