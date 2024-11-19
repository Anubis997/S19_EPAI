class SmartDevice:
    # Class attribute to track the total number of devices created
    device_count = 0

    def __init__(self, device_name, model_number, is_online=False):
        """
        Initializes a SmartDevice instance.

        Args:
            device_name (str): The name of the device.
            model_number (str): The model number of the device.
            is_online (bool): Whether the device is online. Defaults to False.
        """
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}

        # Increment the device count
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        """
        Updates or adds a status attribute for the device.

        Args:
            attribute (str): The attribute name.
            value: The attribute value.
        """
        self.status[attribute] = value

    def get_status(self, attribute):
        """
        Gets the value of a specific status attribute.

        Args:
            attribute (str): The attribute name.

        Returns:
            The value of the attribute, or 'Attribute not found' if it does not exist.
        """
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self):
        """
        Toggles the online status of the device.
        """
        self.is_online = not self.is_online

    def reset(self):
        """
        Resets all status attributes to their default values.
        """
        self.status = {}

    def __call__(self):
        """
        Makes the SmartDevice instance callable, returning its name and model number.
        """
        return f"{self.device_name} (Model: {self.model_number})"

    # Add the callable function attribute device_info dynamically
    device_info = lambda self: {"name": self.device_name, "model": self.model_number}
