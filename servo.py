import time
import numpy as np
import cv2
import RPi.GPIO as GPIO
import config

class Door(object):
    
	def __init__(self):
		# Initialize lock servo and button.
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(config.LOCK_SERVO_PIN, GPIO.OUT)
		self.servo = GPIO.PWM(config.LOCK_SERVO_PIN, 50) 
		 
		 
		# Set initial box state. 
		self.servo.start(2.5) 
		self.is_locked = None 
 
	def lock(self): 
		"""Lock the door.""" 
		self.servo.ChangeDutyCycle(2.5) 
		self.is_locked = True 
 
	def unlock(self): 
		"""Unlock the door.""" 
		self.servo.ChangeDutyCycle(6.5) 
		self.is_locked = False 
 
	def clean(self): 
		self.servo.stop()

