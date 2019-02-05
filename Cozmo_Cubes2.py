#import the cozmo and image libraries
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from PIL import Image


#import libraries for movement and asynchronous behavior
import asyncio
from cozmo.util import degrees, distance_mm

#import these libraries when needed for threads
import _thread
import time


def on_object_tapped(self, event, *, obj, tap_count, tap_duration, **kw):
	robot.say_text("The cube was tapped").wait_for_completed()
	return

def cozmo_program(robot: cozmo.robot.Robot):
	
	#see through cozmos camera
	robot.camera.image_stream_enabled = true
	
	#connect to the cubes
	robot.world.connect_to_cubes()
	
	#identify the cubes
	cube1 = robot.world.get_light_cube(LightCube1Id) #paperclip
	cube2 = robot.world.get_light_cube(LightCube2Id) #heart
	cube3 = robot.world.get_light_cube(LightCube3Id) # looks like ab / t
	
	if cube1 is not none:
		cube1.set_lights(cozmo.lights.green_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube1. Check the battery.")
		
	if cube2 is not none:
		cube2.set_lights(cozmo.lights.blue_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube2. Check the battery.")
		
	if cube3 is not none:
		cube3.set_lights(cozmo.lights.red_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube3. Check the battery.")
		
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
		