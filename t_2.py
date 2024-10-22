# import magiccube
# from Solvers.alg_solver import *
# from Solvers.domino_solver import *


# # initialize cube
# swapped = magiccube.Cube(3, "WWWWWWWWWOOOOOGOOOGGGOGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")
# cube = magiccube.Cube(3, "WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY")


# # cube.rotate("R U R2 F' R U R U' R' F R U' R' ")
# # print(cube)
# cube.scramble()
# print(cube)
# algsolver = AlgSolver(cube)
# print(algsolver.get_color_by_coords((0, 0, 0)))
# print(algsolver.get_color_by_coords((2, 0, 0)))
# print(algsolver.get_color_by_coords((0, 2, 0)))
# print(algsolver.get_color_by_coords((0, 0, 2)))

# # letters = str(algsolver.get_color_by_coords((2, 2, 2)))

# # print(algsolver.getalgfromcolor(letters))
# # print(algsolver.getalgsbystr(algsolver.getalgfromcolor(letters)))
# # print("-" * 100)
# # for i in range(8):
# #     letters = str(algsolver.get_color_by_coords((2, 2, 2)))
# #     cube.rotate(algsolver.getalgsbystr(algsolver.getalgfromcolor(letters)))
# #     print(cube)

# # print()
# # for i in range(8):
# #     letters = list(algsolver.get_color_by_coords((2, 2, 2)))
# #     cube.rotate(algsolver.getalg(algsolver.getalgfromcolor(letters)))

# ## OG = 0, GR = 1, RB = 2, BO = 3
# # print(algsolver.get_unformated_string())
# # Default: kvite og gule på venstre face
# # God orientasjon: Bare kvite på toppen eller
# # Rød/grøn: Sjekk om den rød-grønne
# # Sjekke kor mange kvite edges

# # colors = self.get_colors_by_position()


# dom = Domino_solver(cube)
# print(f"Edges: {dom.color_edge_count_on_face("O", "L")}")
# print(f"Corners: {dom.color_corner_count_on_face("O", "L")}")

# # domswapped = Domino_solver(swapped)
# # print(domswapped.mid_4_good())
l = (1, 2, 3)
print(l[2])