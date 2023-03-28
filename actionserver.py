# Define the action and service messages:
*Creating `.msg` files in the msg folder of our package to define the structure of the action goal, result, and feedback messages, as well as the service request and response messages. *
 *created a `PlantStatus.msg` file to define the message structure for plant status information.*

## Implementing  service: 
*Write the service code to handle requests for plant status information. This might involve reading sensor data or other information from the hardware and returning it as a response. Here's an example of a simple service implementation:*

import rospy
from my_package.srv import PlantStatus

def handle_plant_status(req):
    # Read sensor data or other information from the hardware
    temperature = 25.0
    humidity = 50.0
    light_intensity = 1000

    # Create the service response
    status = PlantStatusResponse()
    status.temperature = temperature
    status.humidity = humidity
    status.light_intensity = light_intensity

    return status

def plant_status_server():
    rospy.init_node('plant_status_server')
    s = rospy.Service('plant_status', PlantStatus, handle_plant_status)
    rospy.spin()

if __name__ == '__main__':
    plant_status_server()
