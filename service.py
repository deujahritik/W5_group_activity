#!/usr/bin/env python

import rospy
from your_package.srv import YourService, YourServiceResponse

def handle_your_service(req):
    # handle the service request
    rospy.loginfo("Handling service request...")
    your_response_variable = "Response"
    return YourServiceResponse(your_response_variable)

if __name__ == '__main__':
    rospy.init_node('your_service_server')
    # create the service
    service = rospy.Service('your_service_name', YourService, handle_your_service)
    rospy.loginfo("Service ready.")
    rospy.spin()

