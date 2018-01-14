
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
        self.s0_coord = tuple(map(sum, zip((x, y), type_coord.get(type)[0])))
        self.s1_coord = tuple(map(sum, zip((x, y), type_coord.get(type)[1])))
        self.s2_coord = tuple(map(sum, zip((x, y), type_coord.get(type)[2])))
        self.s3_coord = tuple(map(sum, zip((x, y), type_coord.get(type)[3])))