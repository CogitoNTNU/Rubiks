import magiccube



# Create the cube in solved state
cube = magiccube.Cube(
    3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

# Print the cube
print(cube)
list1 = []
for item in cube.get_all_pieces().items():
    list1.append(item)

cube.rotate("R U R' U'")

print(cube)
list2= []
for item in cube.get_all_pieces().items():
    list2.append(item)

for i in range(len(list1)):
    if list1[i] != list2[i]:
        print(list1[i], list2[i])
        print(cube.find_piece(list1[i][0]).get_piece_color())
        #print(cube.find_piece(list2[i][1]))

