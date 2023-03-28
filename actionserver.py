Implement the action:
    First writing the action code to handle requests for plant watering. 
    This might involve activating a water pump or other hardware to water the plant.
    
 Here's an example of a simple action implementation:
import rospy
import actionlib
from my_package.msg import WaterPlantAction, WaterPlantGoal, WaterPlantResult, WaterPlantFeedback

def water_plant_server():
    rospy.init_node('water_plant_server')
    server = actionlib.SimpleActionServer('water_plant', WaterPlantAction, execute_cb=handle_water_plant, auto_start=False)
    server.start()
    rospy.spin()

def handle_water_plant(goal):
    # Activate water pump or other hardware to water the plant
    watering_time = 5.0 # seconds
    for i in range(int(watering_time)):
        # Publish feedback to show progress
        feedback = WaterPlantFeedback()
        feedback.percent_complete = float(i + 1) / watering_time * 100.0
        server.publish_feedback(feedback)
        rospy.sleep(1.0)

    # Create the action result
    result = WaterPlantResult()
    result.success = True

    # Set the action result and finish the action
    server.set_succeeded(result)

if __name__ == '__main__':
    water_plant_server()
