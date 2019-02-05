#benstoffer
#mitchell cumming


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
	
	success = True
	
	#see through cozmos camera
	robot.camera.image_stream_enabled = True
	
	#connect to the cubes
	robot.world.connect_to_cubes()
	
	#identify the cubes
	cube1 = robot.world.get_light_cube(LightCube1Id) #paperclip
	cube2 = robot.world.get_light_cube(LightCube2Id) #heart
	cube3 = robot.world.get_light_cube(LightCube3Id) # looks like ab / t
	
	if cube1 is not None:
		cube1.set_lights(cozmo.lights.green_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube1. Check the battery.")
		
	if cube2 is not None:
		cube2.set_lights(cozmo.lights.blue_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube2. Check the battery.")
		
	if cube3 is not None:
		cube3.set_lights(cozmo.lights.red_light)
		
	else:
		cozmo.logger.warning("Cozmo is not connected to Cube3. Check the battery.")
		
	
	#tapping the green cube	
	try:
		robot.say_text("Tap the green cube and I will move forward.").wait_for_completed()
		cube1.wait_for_tap(timeout=20)
		
	except asyncio.TimeoutError:
		
		robot.say_text("The green cube was not tapped.").wait_for_completed()
		success = False
		
	finally:
		
		cube1.set_lights_off()
		robot.say_text("I will now move forward.").wait_for_completed()
		robot.drive_straight(cozmo.util.distance_mm(400), cozmo.util.speed_mmps(150)).wait_for_completed()
		
		
	#tapping the blue cube
	try:
		robot.say_text("Tap the blue cube and I will take a picture.").wait_for_completed()
		cube2.wait_for_tap(timeout=20)
		
	except asyncio.TimeoutError:
		
		robot.say_text("The blue cube was not tapped.").wait_for_completed()
		success = False
		
	finally:
		new_im = robot.world.wait_for(cozmo.worl.EvtNewCameraImage)
		new_im.image.raw_image.show()
		
		#bmp file save
		img_latest = robot.world.latest_image.raw_image
		img_convert = img_latest.convert('L')
		img_convert.save("aPhoto.bmp")
		
		
			
		
		
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
		