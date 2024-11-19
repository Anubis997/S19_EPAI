class SmartDevice:
    # Class attribute to track total number of devices created
    device_count = 0

    def __init__(self, device_name, model_number, is_online=False):
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        """Update or add a status attribute."""
        self.status[attribute] = value

    def get_status(self, attribute):
        """Retrieve the value of a status attribute."""
        return self.status.get(attribute, "Attribute not found")

    def toggle_online(self):
        """Toggle the online status."""
        self.is_online = not self.is_online

    def reset(self):
        """Reset all status attributes."""
        self.status.clear()

    def __call__(self):
        """Return the device name and model number when the instance is called."""
        return f"{self.device_name} (Model: {self.model_number})"

    # Default callable function attribute
    device_info = lambda self: {
        "name": self.device_name,
        "model": self.model_number
    }
