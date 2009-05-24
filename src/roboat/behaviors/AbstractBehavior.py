'''
Created on May 24, 2009

@author: janusz
'''

class AbstractBehavior():
    """The Abstract Class defining the behavior interface."""
    
    priority = 0
    

    def shouldRun( self ):
        """This function returns a boolean value indicating if this behavior should take over the control of the robot now.
            Should run returns True if this behavior should take over the control of the robot and false otherwise
            shouldrun is run very often and in a very tight loop so keep it short."""
        raise NotImplementedError( "You tried to call an abstract function. Maybe you forgot to define the function in your class" )

    def run(self):
        """ If a behavior is picked for controlling the robot this method is called. 
            In this method short adjustments in the overall behavior of the robot can be made. 
            Again try to return the control very fast."""
        raise NotImplementedError("You tried to call an abstract function. Maybe you forgot to define the function in your class" )
    