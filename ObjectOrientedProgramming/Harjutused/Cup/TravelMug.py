from Cup import Cup

class TravelMug(Cup):
    """A travel mug subclass."""
    def __init__(self, volume: int, color: str, is_full: bool = False, lid_on: bool = True):
        super().__init__(volume, color, is_full)
        self.lid_on = lid_on

    def toggle_lid(self):
        self.lid_on = not self.lid_on

    def __repr__(self):
        return f"TravelMug({self.volume}ml, {self.color}, {'full' if self.is_full else 'empty'}, {'lid on' if self.lid_on else 'lid off'})"
