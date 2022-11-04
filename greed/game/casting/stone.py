from game.casting.actor import Actor


class Stones(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of a Stone is to provide a message about itself.

    Attributes:
        _message (string): A short description about the Stone.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the Stone's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message