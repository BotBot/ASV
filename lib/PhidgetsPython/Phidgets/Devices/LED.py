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

class LED(Phidget):
    """This class represents a Phidget LED. All methods to control a Phidget LED are implemented in this class.
    
    The Phidget LED is a board that is meant for driving LEDs. Currently, the only available version drives 64 LEDs, but other versions may become available so this number is not absolute.
    
    LEDs can be controlled individually, at brightness levels from 0-100.
    
    Extends:
        Phidget
    """
    def __init__(self):
        """The Constructor Method for the LED Class
        """
        Phidget.__init__(self)
        
        PhidgetLibrary.getDll().CPhidgetLED_create(byref(self.handle))

    def getDiscreteLED(self, index):
        """Returns the brightness value of an LED.
        
        This value ranges from 0-100.
        
        Parameters:
            index<int>: index of the Discrete LED.
        
        Returns:
            Brightness of the LED <int>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index is out of range.
        """
        ledVal = c_int()
        result = PhidgetLibrary.getDll().CPhidgetLED_getDiscreteLED(self.handle, c_int(index), byref(ledVal))
        if result > 0:
            raise PhidgetException(result)
        else:
            return ledVal.value

    def setDiscreteLED(self, index, value):
        """Sets the brightness of an LED.
        
        Valid values are 0-100, with 0 being off and 100 being the brightest.
        This 0-100 value is converted internally to a 6-bit value (0-63) so only 64 levels of brightness are actually possible.
        
        Parameters:
            index<int>: index of the Discrete LED.
            value<int>: brightness value of the Discrete LED.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached, or if the index or brightness value are out of range.
        """
        result = PhidgetLibrary.getDll().CPhidgetLED_setDiscreteLED(self.handle,  c_int(index), c_int(value))
        if result > 0:
            raise PhidgetException(result)

    def getLEDCount(self):
        """Returns the number of LEDs that this board can drive.
        
        This may not correspond to the actual number of LEDs attached.
        
        Returns:
            The number of available LEDs <int>.
        
        Exceptions:
            PhidgetException: If this Phidget is not opened and attached.
        """
        LEDCount = c_int()
        result = PhidgetLibrary.getDll().CPhidgetLED_getLEDCount(self.handle, byref(LEDCount))
        if result > 0:
            raise PhidgetException(result)
        else:
            return LEDCount.value
