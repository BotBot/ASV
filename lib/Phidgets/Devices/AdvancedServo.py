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

class AdvancedServo(Phidget):
    """This class represents a Phidget AdvancedServo Controller.
    
    All methods to control a AdvancedServo Controller are implemented in this class.
    
    See the product manual for more specific API details, supported functionality, units, etc.
    
    Extends:
        Phidget
    """
    def __init__(self):
        """The Constructor Method for the AdvancedServo Class
        """
        Phidget.__init__(self)
        
        self.__currentChange = None
        self.__positionChange = None
        self.__velocityChange = None
        
        self.__onCurrentChange = None
        self.__onPositionChange = None
        self.__onVelocityChange = None
        
        PhidgetLibrary.getDll().CPhidgetAdvancedServo_create(byref(self.handle))
        
        if sys.platform == 'win32':
            self.__CURRENTCHANGEHANDLER = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
            self.__POSITIONCHANGEHANDLER = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
            self.__VELOCITYCHANGEHANDLER = WINFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
        elif sys.platform == 'darwin' or sys.platform == 'linux2':
            self.__CURRENTCHANGEHANDLER = CFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
            self.__POSITIONCHANGEHANDLER = CFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
            self.__VELOCITYCHANGEHANDLER = CFUNCTYPE(c_int, c_void_p, c_void_p, c_int, c_double)
    
    def getMotorCount(self):
        """Returns the number of motors this Phidget can support.
        
        Note that there is no way of programatically determining how many motors are actually attached to the board.
        
        Returns:
            The number of motors <int>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        motorCount = c_int()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getMotorCount(self.handle, byref(motorCount))
        if result > 0:
            raise PhidgetException(result)
        else:
            return motorCount.value
    
    def getAcceleration(self, index):
        """Returns a motor's acceleration.
        
        The valid range is between getAccelerationMin and getAccelerationMax,
        and refers to how fast the AdvancedServo Controller will change the speed of a motor.
        
        Parameters:
            index<int>: index of motor.
        
        Returns:
            The acceleration of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        accel = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getAcceleration(self.handle, c_int(index), byref(accel))
        if result > 0:
            raise PhidgetException(result)
        else:
            return accel.value
    
    def setAcceleration(self, index, value):
        """Sets a motor's acceleration.
        
        The valid range is between getAccelerationMin and getAccelerationMax.
        This controls how fast the motor changes speed.
        
        Parameters:
            index<int>: index of the motor.
            value<double>: requested acceleration for that motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or acceleration value are invalid.
        """
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setAcceleration(self.handle, c_int(index), c_double(value))
        if result > 0:
            raise PhidgetException(result)
    
    def getAccelerationMax(self, index):
        """Returns the maximum acceleration that a motor will accept, or return.
        
        Parameters:
            index<int>: Index of the motor.
        
        Returns:
            Maximum acceleration of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        accelMax = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getAccelerationMax(self.handle, c_int(index), byref(accelMax))
        if result > 0:
            raise PhidgetException(result)
        else:
            return accelMax.value

    def getAccelerationMin(self, index):
        """Returns the minimum acceleration that a motor will accept, or return.
        
        Parameters:
            index<int>: Index of the motor.
        
        Returns:
            Minimum acceleration of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        accelMin = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getAccelerationMin(self.handle, c_int(index), byref(accelMin))
        if result > 0:
            raise PhidgetException(result)
        else:
            return accelMin.value
    
    def getVelocityLimit(self, index):
        """Gets the last set velocity limit for a motor.
        
        The valid range is between getVelocityMin and getVelocityMax
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current velocity limit of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        veloctiyLimit = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getVelocityLimit(self.handle, c_int(index), byref(veloctiyLimit))
        if result > 0:
            raise PhidgetException(result)
        else:
            return veloctiyLimit.value

    def setVelocityLimit(self, index, value):
        """Sets the velocity limit for a motor.
        
        The valid range is between getVelocityMin and getVelocityMax
        
        Parameters:
            index<int>: index of the motor.
            value<double>: requested velocity limit for the motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or velocity value are invalid.
        """
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setVelocityLimit(self.handle, c_int(index), c_double(value))
        if result > 0:
            raise PhidgetException(result)
    
    def getVelocity(self, index):
        """Gets the current velocity of a motor.
        
        The range for this value should be between getVelocityMin and getVelocityLimit
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current velocity of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        veloctiy = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getVelocity(self.handle, c_int(index), byref(veloctiy))
        if result > 0:
            raise PhidgetException(result)
        else:
            return veloctiy.value
    
    def getVelocityMax(self, index):
        """Gets the maximum velocity that can be set for a motor.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The maximum velocity for the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        veloctiyMax = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getVelocityMax(self.handle, c_int(index), byref(veloctiyMax))
        if result > 0:
            raise PhidgetException(result)
        else:
            return veloctiyMax.value
    
    def getVelocityMin(self, index):
        """Gets the minimum velocity that can be set for a motor.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The minimum velocity for the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        veloctiyMin = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getVelocityMin(self.handle, c_int(index), byref(veloctiyMin))
        if result > 0:
            raise PhidgetException(result)
        else:
            return veloctiyMin.value
    
    def __nativeVelocityChangeEvent(self, handle, usrptr, index, value):
        if self.__velocityChange != None:
            self.__velocityChange(VelocityChangeEventArgs(index, value))
        return 0

    def setOnVelocityChangeHandler(self, velocityChangeHandler):
        """Sets the VelocityChange Event Handler.
        
        The velocity change handler is a method that will be called when the velocity of a motor changes.
        These velocity changes are reported back from the AdvancedServo Controller and so correspond to actual motor velocity over time.
        
        Parameters:
            velocityChangeHandler: hook to the velocityChangeHandler callback function.
        
        Exceptions:
            PhidgetException
        """
        self.__velocityChange = velocityChangeHandler
        self.__onVelocityChange = self.__VELOCITYCHANGEHANDLER(self.__nativeVelocityChangeEvent)
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_set_OnVelocityChange_Handler(self.handle, self.__onVelocityChange, None)
        if result > 0:
            raise PhidgetException(result)
    
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
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getPosition(self.handle, c_int(index), byref(position))
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
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setPosition(self.handle, c_int(index), c_double(value))
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
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getPositionMax(self.handle, c_int(index), byref(positionMax))
        if result > 0:
            raise PhidgetException(result)
        else:
            return positionMax.value
    
    def setPositionMax(self, index, value):
        """Sets the maximum position of a servo motor.
        
        Parameters:
            index<int>: index of the motor.
            position<double>: desired maximum position limit for the motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or position is out of range,
            or if the desired maximum position limit is out of range, or if the motor is not engaged.
        """
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setPositionMax(self.handle, c_int(index), c_double(value))
        if result > 0:
            raise PhidgetException(result)

    def getPositionMin(self, index):
        """Returns the minimum position that a servo will accept, or return.
        
        Returns:
            The minimum position in degrees <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        positionMin = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getPositionMin(self.handle, c_int(index), byref(positionMin))
        if result > 0:
            raise PhidgetException(result)
        else:
            return positionMin.value
    
    def setPositionMin(self, index, value):
        """Sets the minimum position of a servo motor.
        
        Parameters:
            index<int>: index of the motor.
            position<double>: desired minimum position limit for the motor.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or position is out of range,
            or if the desired minimum position limit is out of range, or if the motor is not engaged.
        """
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setPositionMin(self.handle, c_int(index), c_double(value))
        if result > 0:
            raise PhidgetException(result)

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
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_set_OnPositionChange_Handler(self.handle, self.__onPositionChange, None)
        if result > 0:
            raise PhidgetException(result)
    
    def getCurrent(self, index):
        """Returns a motor's current usage.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current usage of the motor <double>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        current = c_double()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getCurrent(self.handle, c_int(index), byref(current))
        if result > 0:
            raise PhidgetException(result)
        else:
            return current.value

    def __nativeCurrentChangeEvent(self, handle, usrptr, index, value):
        if self.__currentChange != None:
            self.__currentChange(CurrentChangeEventArgs(index, value))
        return 0

    def setOnCurrentChangeHandler(self, currentChangeHandler):
        """Sets the CurrentCHange Event Handler.
        
        The current change handler is a method that will be called when the current consumed by a motor changes.
        
        Parameters:
            currentChangeHandler: hook to the currentChangeHandler callback function.
        
        Exceptions:
            PhidgetException
        """
        self.__currentChange = currentChangeHandler
        self.__onCurrentChange = self.__CURRENTCHANGEHANDLER(self.__nativeCurrentChangeEvent)
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_set_OnCurrentChange_Handler(self.handle, self.__onCurrentChange, None)
        if result > 0:
            raise PhidgetException(result)
    
    def getSpeedRampingOn(self, index):
        """Gets the speed ramping state for a motor.
        
        This is whether or not velocity and acceleration are used.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current state of the speedRamping flag for this motor<boolean>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        rampingState = c_int()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getSpeedRampingOn(self.handle, c_int(index), byref(rampingState))
        if result > 0:
            raise PhidgetException(result)
        else:
            if rampingState.value == 1:
                return True
            else:
                return False
    
    def setSpeedRampingOn(self, index, state):
        """Sets the speed ramping state for a motor.
        
        This is whether or not velocity and acceleration are used.
        
        Parameters:
            index<int>: Index of the motor.
            state<boolean>: State to set the speedRamping flag for this motor to.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range.
        """
        if state == True:
            value = 1
        else:
            value = 0
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setSpeedRampingOn(self.handle, c_int(index), c_int(value))
        if result > 0:
            raise PhidgetException(result)
    
    def getEngaged(self, index):
        """Gets the engaged state of a motor.
        
        This is whether the motor is powered or not.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current state of the engaged flag for this motor<boolean>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        engagedState = c_int()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getEngaged(self.handle, c_int(index), byref(engagedState))
        if result > 0:
            raise PhidgetException(result)
        else:
            if engagedState.value == 1:
                return True
            else:
                return False
    
    def setEngaged(self, index, state):
        """Sets the engaged state of a motor.
        
        This is whether the motor is powered or not.
        
        Parameters:
            index<int>: Index of the motor.
            state<boolean>: State to set the engaged flag for this motor to.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range.
        """
        if state == True:
            value = 1
        else:
            value = 0
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_setEngaged(self.handle, c_int(index), c_int(value))
        if result > 0:
            raise PhidgetException(result)
    
    def getStopped(self, index):
        """Gets the stopped state of a motor.
        
        This is true when the motor is not moving and there are no outstanding commands.
        
        Parameters:
            index<int>: index of the motor.
        
        Returns:
            The current state of the stopped flag for this motor<boolean>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is invalid.
        """
        stoppedState = c_int()
        result = PhidgetLibrary.getDll().CPhidgetAdvancedServo_getStopped(self.handle, c_int(index), byref(stoppedState))
        if result > 0:
            raise PhidgetException(result)
        else:
            if stoppedState.value == 1:
                return True
            else:
                return False