
# Block class to define a block object
class Block:
    def __init__(self, type, x, y):
        # Dictionary that stores the block patterns for the 7 different types of blocks
        type_coord = {
            0: [(0, 2), (1, 2), (2, 2), (3, 2)],
            1: [(0, 1), (0, 2), (1, 2), (2, 2)],
            2: [(0, 2), (1, 2), (2, 2), (2, 1)],
            3: [(1, 1), (2, 1), (1, 2), (2, 2)],
            4: [(0, 2), (1, 2), (1, 1), (2, 1)],
            5: [(1, 1), (0, 2), (1, 2), (2, 2)],
            6: [(0, 1), (1, 1), (1, 2), (2, 2)]
        }

        # Variables that store the squares' coordinates initialized on object creation
        self.s0_coord = type_coord.get(type)[0]
        self.s1_coord = type_coord.get(type)[1]
        self.s2_coord = type_coord.get(type)[2]
        self.s3_coord = type_coord.get(type)[3]

        # Variable that stores the location coordinates
        self.location = (x, y)


    # Returns the coords of a square considering the location of the block
    def getSCoord(self, square):
        return tuple(map(sum, zip(self.location, square)))


    # Performs a transformation on the squares that rotates the block 90 degrees clockwise
    def rotate(self):
        # Dictionary that stores the coordinate transformations ( y_initial -> x )
        coord_swap = {
            0: 3,
            1: 2,
            2: 1,
            3: 0,
        }

        # Stores the y_initial values of the squares
        temp = (self.s0_coord[1], self.s1_coord[1], self.s2_coord[1], self.s3_coord[1])

        # Saves the transformed coordinates to the object data: ( y_initial -> dictionary transformation -> x ) and ( x_initial -> y )
        self.s0_coord = (coord_swap.get(temp[0]), self.s0_coord[0])
        self.s1_coord = (coord_swap.get(temp[1]), self.s1_coord[0])
        self.s2_coord = (coord_swap.get(temp[2]), self.s2_coord[0])
        self.s3_coord = (coord_swap.get(temp[3]), self.s3_coord[0])


