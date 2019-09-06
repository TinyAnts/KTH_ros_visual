#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("nagarajan", String, queue_size=10)
    rospy.init_node("publisher", anonymous=True)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():

        k=1
        n=4
        for i in range(n):
            k = k + i
            hello_str = "%s" %k  #"k = {} for n = {}".format(k,i)
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
