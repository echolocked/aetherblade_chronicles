# actions/base_action.py

class BaseAction:
    def __init__(self, unit):
        self.unit = unit  # The unit performing the action

    def execute(self):
        """
        Execute the action. This method should be overridden by subclasses
        to provide specific action behavior.
        """
        raise NotImplementedError("Subclasses must implement this method")

    # You can include more common methods or attributes relevant to all actions here
