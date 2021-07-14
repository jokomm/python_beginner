"""Pibot Robot I."""

from PiBot import PiBot
robot = PiBot()

left_line_sensor = robot.get_second_line_sensor_from_left()
right_line_sensor = robot.get_second_line_sensor_from_right()

robot.set_wheels_speed(50)
while left_line_sensor > 150 and right_line_sensor > 150:
    left_line_sensor = robot.get_second_line_sensor_from_left()
    right_line_sensor = robot.get_second_line_sensor_from_right()
    robot.sleep(0.001)

robot.sleep(0.5)
robot.set_wheels_speed(0)
robot.done()
