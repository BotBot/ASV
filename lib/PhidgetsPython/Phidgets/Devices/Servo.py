"""Copyright 2008 Phidgets Inc.
This work is licensed under the Creative Commons Attribution 2.5 Canada License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/2.5/ca/
"""

__author__ = 'Adam Stelmack'
__version__ = '2.1.6'
__date__ = 'April 9 2009'

from threading import *
from ctypes import *
from Phidgets.Phidget import *
from Phidgets.PhidgetException import *
import sys

class Servo(Phidget):
    """This class represents a Phidget servo Controller.
    
    All methods to control a Servo Controller are implemented in this class.
    The Phidget Sevo controller simply outputs varying widths of PWM, which is what most servo motors take as an input driving signal.
    
    Extends:
        Phidget
    """
    def __init__(self):
        """The Constructor Method for the Servo Class
        """
        Phidget.__init__(self)
        
        self.__positionChange = None
        
        self.__onPositionChange = None
        
        PhidgetLibrary.getDll().CPhidgetServo_create(byref(self.handle))
        
        if sys.platform == 'win32':
            self.__POSITIONCHANGEHANDLER = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
        elif sys.platform == 'darwin' or sys.platform == 'linux2':
            self.__POSITIONCHANGEHANDLER = CFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)

    def getMotorCount(self):
        """Returns the number of motors this Phidget can support.
        
        Note that there is no way of programatically determining how many motors are actually attached to the board.
        
        Returns:
            The number of motors <int>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        motorCount = c_int()
        result = PhidgetLibrary.getDll().CPhidgetServo_getMotorCount(self.handle, byref(motorCount))
        if result > 0:
            raise PhidgetException(result)
        else:
            return motorCount.value

    def getPosition(self, index):
        """Returns the position of a servo motor.
        
        Note that since servo motors do not offer any feedback in their interface, this value is simply whatever the servo was last set to.
        There is no way of determining the position of a servo that has been plugged in, until it's position has been set.
        Therefore, if an initial position is important, it should be set as part of initialization.
        
        If the servo is not engaged, the position is unknown and calling this function will throw an exception.
        
        The range here is between getPositionMin and getPositionMax, and corresponds aproximately to an angle in degrees. Note that most servos will not be able to operate accross this entire range.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current position of the selected motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range, or the motor is not engaged.
        """
        position = c_double()
        result = PhidgetLibrary.getDll().CPhidgetServo_getPosition(self.handle, c_int(index), byref(position))
        if result > 0:
            raise PhidgetException(result)
        else:
            return position.value

    def setPosition(self, index, value):
        """Sets the position of a servo motor.
        
        The range here is between getPositionMin and getPositionMax, and corresponds aproximately to an angle in degrees.
        Note that most servos will not be able to operate accross this entire range.
        Typically, the range might be 25 - 180 degrees, but this depends on the servo.
        
        Parameters:
            index<int>: index of the motor.
            position<double>: desired position for the motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or position is out of range,
            or if the desired position is out of range, or if the motor is not engaged.
        """
        result = PhidgetLibrary.getDll().CPhidgetServo_setPosition(self.handle, c_int(index), c_double(value))
        if result > 0:
            raise PhidgetException(result)

    def getPositionMax(self, index):
        """Returns the maximum position that a servo will accept, or return.
        
        Returns:
            The maximum position in degrees <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        positionMax = c_double()
        result = PhidgetLibrary.getDll().CPhidgetServo_getPositionMax(self.handle, c_int(index), byref(positionMax))
        if result > 0:
            raise PhidgetException(result)
        else:
            return positionMax.value

    def getPositionMin(self, index):
        """Returns the minimum position that a servo will accept, or return.
        
        Returns:
            The minimum position in degrees <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        positionMin = c_double()
        result = PhidgetLibrary.getDll().CPhidgetServo_getPositionMin(self.handle, c_int(index), byref(positionMin))
        if result > 0:
            raise PhidgetException(result)
        else:
            return positionMin.value

    def __nativePositionChangeEvent(self, handle, usrptr, index, value):
        if self.__positionChange != None:
            self.__positionChange(PositionChangeEventArgs(index, value))
        return 0

    def setOnPositionChangeHandler(self, positionChangeHandler):
        """Sets the Position Change Event Handler.
        
        The servo position change handler is a method that will be called when the servo position has changed.
        The event will get fired after every call to setPosition.
        
        Parameters:
            positionChangeHandler: hook to the positionChangeHandler callback function.
        
        Exceptions:
            PhidgetException
        """
        self.__positionChange = positionChangeHandler
        self.__onPositionChange = self.__POSITIONCHANGEHANDLER(self.__nativePositionChangeEvent)
        result = PhidgetLibrary.getDll().CPhidgetServo_set_OnPositionChange_Handler(self.handle, self.__onPositionChange, None)
        if result > 0:
            raise PhidgetException(result)

    def getEngaged(self, index):
        """Returns the engaged state of a servo
        
        Returns:
            Motor Engaged state <boolean>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range.
        """
        engagedStatus = c_int()
        result = PhidgetLibrary.getDll().CPhidgetServo_getEngaged(self.handle, c_int(index), byref(motorStatus))
        if result > 0:
            raise PhidgetException(result)
        else:
            if engagedStatus.value == 1:
                return True
            else:
                return False

    def setEngaged(self, index, state):
        """Engage or disengage a servo motor
        
        This engages or disengages the servo.
        The motor is engaged whenever you set a position, use this function to
        disengage, and reengage without setting a position.
        
        Parameters:
            index<int>: index of a servo motor.
            state<boolean>: desired engaged state of the servo motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range.
        """
        if state == True:
            value = 1
        else:
            value = 0
        result = PhidgetLibrary.getDll().CPhidgetServo_setEngaged(self.handle, c_int(index), c_int(value))
        if result > 0:
            raise PhidgetException(result)
