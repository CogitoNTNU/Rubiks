import magiccube



# Create the cube in solved state
cube = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube
#print(cube.get_all_pieces())
print(cube.find_piece("BRW"))
#print(cube)
print(cube.get_piece((2,2,2)))
cube.rotate("Y2 R U R' U R U2 R'")

print(cube)
print(cube.find_piece("BRW"))



