from backend.moves.sequence import (
    do_sequence,
    get_mapped_sequence,
    get_move,
    get_sequence,
    reverse_sequence,
    simplify_sequence,
)


def test_simplify_sequence():
    assert simplify_sequence("R") == "R"
    assert simplify_sequence("R R'") == ""
    assert simplify_sequence("R R' R") == "R"
    assert simplify_sequence("R R' R R") == "R2"
    assert simplify_sequence("R L2 R'") == "L2"
    assert simplify_sequence("R F R") == "R F R"
    assert simplify_sequence("R F R' R2") == "R F R"


def test_reverse_sequence():
    assert reverse_sequence("R") == "R'"
    assert reverse_sequence("R'") == "R"
    assert reverse_sequence("R2") == "R2'"
    assert reverse_sequence("R F R' R2") == "R2' R F' R'"


def test_get_move():
    assert get_move("R") == "R"
    assert get_move("R2") == "R2"
    assert get_move("R3") == "R'"
    assert get_move("R'") == "R'"
    assert get_move("R2'") == "R2"
    assert get_move("R3'") == "R"
    assert get_move("R1231412417812634716241874617") == "R"


def test_get_sequence():
    assert get_sequence("LO") == "R U2 D' B D'"
    assert get_sequence("LO'") == "D B' D U2' R'"
    assert get_sequence("LO2") == "R U2 D' B D' R U2 D' B D'"


def test_do_sequence():
    assert do_sequence("R R'") == ""
    assert do_sequence("R R' R") == "R"
    assert do_sequence("R R' R R") == "R2"
    assert do_sequence("LO") == "R U2 D' B D'"
    assert do_sequence("key") == "R U R' U' R' F R F'"


def test_get_mapped_sequence():
    assert get_mapped_sequence("R") == [8]
    assert get_mapped_sequence("R R'") == []
    assert get_mapped_sequence("R R' R") == [8]
    assert get_mapped_sequence("R R' R R") == [7]
    assert get_mapped_sequence("LO") == [8, 16, 11, 20, 11]
    assert get_mapped_sequence("key") == [8, 17, 6, 15, 6, 24, 8, 26]
