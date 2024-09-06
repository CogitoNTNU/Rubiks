import magiccube



# Create the cube in solved state
cube = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube
print(cube)
cube.rotate("R U R' U R U2 R'")

print(cube)