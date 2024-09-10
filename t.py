import magiccube



# Create the cube in solved state
cube = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube
#print(cube.get_all_pieces())
print(cube.find_piece("BRW"))
#print(cube)
cube.rotate("R U R' U R U2 R'")
print(cube.get_piece((0,0,0)))
#print(cube)
print(cube.find_piece("BRW"))


