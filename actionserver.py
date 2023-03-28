#!/usr/bin/env python

import rospy
import actionlib
from your_package.msg import YourAction, YourActionFeedback, YourActionResult

class YourActionServer(object):
    # create messages that are used to publish feedback/result
    _feedback = YourActionFeedback()
    _result = YourActionResult()

    def __init__(self):
        # create the action server
        self._as = actionlib.SimpleActionServer("your_action_name", YourAction, self.execute, False)
        self._as.start()

    def execute(self, goal):
        # execute the action
        rospy.loginfo("Executing action...")
        rospy.sleep(1.0)
        self._result.your_result_variable = "Result"
        self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('your_action_server')
    server = YourActionServer()
    rospy.spin()

