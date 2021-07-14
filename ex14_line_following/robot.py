"""Pibot Robot II."""

from PiBot import PiBot
robot = PiBot()

left_sensor = robot.get_second_line_sensor_from_left()
right_sensor = robot.get_second_line_sensor_from_right()
sensors = robot.get_line_sensors()
print(sensors)

robot.set_wheels_speed(60)
while left_sensor != 1024 or right_sensor != 1024:
    left_sensor = robot.get_second_line_sensor_from_left()
    right_sensor = robot.get_second_line_sensor_from_right()
    if left_sensor < 101 and right_sensor < 101:
        robot.set_wheels_speed(60)
    elif left_sensor < 101:
        robot.set_left_wheel_speed(20)
        robot.set_right_wheel_speed(60)
        sensors = robot.get_line_sensors()
    elif right_sensor > 101:
        robot.set_left_wheel_speed(60)
        robot.set_right_wheel_speed(20)
        sensors = robot.get_line_sensors()
    robot.sleep(0.001)
print(sensors)
robot.set_wheels_speed(0)
robot.done()
