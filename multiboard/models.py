from enum import Enum


class TileType(Enum):
    CORE = "Core"
    SIDE = "Side"
    CORNER = "Corner"


class MultiboardTile:

    # Initialises the MultiboardTile object
    def __init__(self, length, width, tile_type):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.length = length  # Param length will be in mm
        self.width = width  # Param width will be in mm
        self.tile_type = TileType(tile_type)  # Validates tile_type
        self.area = self.calculate_area()

    def calculate_area(self):
        return self.length * self.width  # Used to calculate the area of tile in mm

    def get_multihole_count(self):
        return (self.length // 25) * (self.width // 25)  # Returning the number of multiholes on a tile

    def can_print(self, printer_length, printer_width):
        return self.length <= printer_length and self.width <= printer_width  # Check the tile can be printed

    def __str__(self):
        return f"Tile (length={self.length}, width={self.width})"  # Returns the output of the area back to the user

    @classmethod
    def create_6x6_tile(cls, tile_type):
        return cls(158, 158, tile_type)  # Creates a 6x6 tile of 158mm x 158mm

    @classmethod
    def create_8x8_tile(cls, tile_type):
        return cls(208, 208, tile_type)  # Creates a 8x8 tile of 208mm by 208mm

    @classmethod
    def create_9x9_tile(cls, tile_type):
        return cls(237, 237, tile_type)  # creates a 9x9 tile of 237mm x 237mm
