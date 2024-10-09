import json
import re

import portalocker

with open(r"backend\moves\sequenses.json", "r", encoding="UTF-8") as f:
    portalocker.lock(f, portalocker.LOCK_SH)
    sequence_map: dict[str, str] = json.load(f)["ThreeByThree"]
    portalocker.unlock(f)


# Map of moves to their corresponding index in the move_map
move_map = {
    "R": 6,
    "R2": 7,
    "R'": 8,
    "L": 0,
    "L2": 1,
    "L'": 2,
    "U": 17,
    "U2": 16,
    "U'": 15,
    "D": 9,
    "D2": 10,
    "D'": 11,
    "F": 24,
    "F2": 25,
    "F'": 26,
    "B": 20,
    "B2": 19,
    "B'": 18,
    "M": 3,
    "M2": 4,
    "M'": 5,
    "E": 12,
    "E2": 13,
    "E'": 14,
    "S": 21,
    "S2": 22,
    "S'": 23,
}


def simplify_sequence(seq: str) -> str:
    """
    Simplifies a sequence of Rubik's Cube moves by removing redundant moves.

    Args:
        seq (str): The sequence of Rubik's Cube moves.

    Returns:
        str: The simplified sequence of Rubik's Cube moves.
    """

    previous_sequence = ""

    # Check direction of triple turn and returns single a diametrically opposed turn
    def triple_turn(match: re.Match) -> str:
        return (
            f" {match.group('char')} {match.group('separation')}"
            if match.group("suffix") == "'"
            else f" {match.group('char')}'{match.group('separation')}"
        )

    # fmt: off
    # pylint: disable=line-too-long
    while previous_sequence != (previous_sequence := seq):
        # Removes N' N pairs separated by an unknown amount of same plane turns
        seq = re.sub(r"(?:^| )(.)'(?P<separation>(?<=[LRM]')[LRM '2]*?|(?<=[UED]')[UED '2]*?|(?<=[FSB]')[FSB '2]*?)\1(?= |$)", r" \g<separation>", seq)
        # Removes N N' pairs separated by an unknown amount of same plane turns
        seq = re.sub(r"(?:^| )(.) (?P<separation>(?<=[LRM] )[LRM '2]*?|(?<=[UED] )[UED '2]*?|(?<=[FSB] )[FSB '2]*?)\1'(?= |$)", r" \g<separation>", seq)
        # Removes N2 N2 pairs separated by an unknown amount of same plane turns
        seq = re.sub(r"(?:^| )(.2)(?P<separation>(?<=[LRM]2)[LRM '2]*?|(?<=[UED]2)[UED '2]*?|(?<=[FSB]2)[FSB '2]*?)\1(?= |$)", r" \g<separation>", seq)
        # Replaces N N pairs separated by an unknown amount of same plane turns with N2
        seq = re.sub(r"(?:^| )(?P<char>.) (?P<separation>(?<=[LRM] )[LRM '2]*?|(?<=[UED] )[UED '2]*?|(?<=[FSB] )[FSB '2]*?)\1(?= |$)", r" \g<char>2 \g<separation>", seq)
        # Replaces N' N' pairs separated by an unknown amount of same plane turns with N2
        seq = re.sub(r"(?:^| )(?P<char>.)'(?P<separation>(?<=[LRM]')[LRM '2]*?|(?<=[UED]')[UED '2]*?|(?<=[FSB]')[FSB '2]*?)\1'(?= |$)", r" \g<char>2 \g<separation>", seq)
        # Replaces N N2 pairs separated by an unknown amount of same plane turns with N'
        seq = re.sub(r"(?:^| )(?P<char>.)(?P<suffix> |$)(?P<separation>(?<=[LRM] )[LRM '2]*?|(?<=[UED] )[UED '2]*?|(?<=[FSB] )[FSB '2]*?)\1(?:2)(?= |$)", triple_turn, seq)
        # Replaces N' N2 pairs separated by an unknown amount of same plane turns with N
        seq = re.sub(r"(?:^| )(?P<char>.)(?P<suffix>')(?P<separation>(?<=[LRM]')[LRM '2]*?|(?<=[UED]')[UED '2]*?|(?<=[FSB]')[FSB '2]*?)\1(?:2)(?= |$)", triple_turn, seq)
        # Replaces N2 N pairs separated by an unknown amount of same plane turns with N'
        seq = re.sub(r"(?:^| )(?P<char>.)2(?P<separation>(?<=[LRM]2)[LRM '2]*?|(?<=[UED]2)[UED '2]*?|(?<=[FSB]2)[FSB '2]*?)\1(?P<suffix> |$)(?= |$)", triple_turn, seq)
        # Replaces N2 N' pairs separated by an unknown amount of same plane turns with N
        seq = re.sub(r"(?:^| )(?P<char>.)2(?P<separation>(?<=[LRM]2)[LRM '2]*?|(?<=[UED]2)[UED '2]*?|(?<=[FSB]2)[FSB '2]*?)\1(?P<suffix>')(?= |$)", triple_turn, seq)
        # Cleans up extra whitespaces
        seq = re.sub(r"\s+", " ", seq)
    # pylint: enable=line-too-long
    # fmt: on
    return seq.strip()

def reverse_sequence(moves: str) -> str:
    """
    Reverses the sequence of moves in a Rubik's Cube algorithm.

    Args:
        moves (str): The sequence of moves to be reversed.

    Returns:
        str: The reversed sequence of moves.
    """

    return " ".join(
        [
            move[:-1] if move.endswith("'") else move + "'"
            for move in moves.split()[::-1]
        ]
    )

def get_move(move: str) -> str:
    # Extract repeat part
    repeat = int(match.group()) % 4 if (match := re.search(r"\d+", move)) else 1

    # Generalizes suffix
    if repeat == 0:
        return ""
    elif repeat == 1:
        return move[:1] + "'" if move.endswith("'") else move[:1]
    elif repeat == 2:
        return move[:1] + "2"
    elif repeat == 3:
        return move[:1] if move.endswith("'") else move[:1] + "'"


def get_sequence(sequence_name: str) -> str:
    """
    Retrieves a sequence and its repetition count based on the sequence name.

    Args:
        sequence_name (str): The name of the sequence to retrieve.

    Returns:
        tuple[str, int]: A tuple containing the sequence of moves as a string and
                            the repetition count.
    """

    # Extract repeat part
    repeat = (
        int(match.group()) if (match := re.search(r"\d+", sequence_name)) else 1
    )
    # Extract sequence part
    sequence = sequence_map[
        re.match(
            "|".join([r"^" + key + r"(?=[\d']|$)" for key in sequence_map]),
            sequence_name,
        ).group()
    ]
    # Adjust for prime move if applicable
    if sequence_name.endswith("'"):
        sequence = reverse_sequence(sequence)

    # Return sequence and repetitions
    return sequence*repeat


def do_sequence(moves: str) -> str:
    """
    Executes a sequence of Rubik's Cube moves.

    Args
        moves (str): The sequence of moves to perform.
    """
    move_list = ""

    for move in moves.split(" "):
        print(re.match(
            "|".join([r"^" + key + r"\d*[']?$" for key in sequence_map]), move
        ))

        # Basic moves
        if re.match(r"^[LMRUEDFSB]\d*[']?$", move):
            move_list += get_move(move)

        # Named sequences of basic moves
        elif re.match(
            "|".join([r"^" + key + r"\d*[']?$" for key in sequence_map]), move
        ):
            move_list += do_sequence(get_sequence(move))

        move_list += " "
    simplified_sequence=simplify_sequence(move_list)
    return simplified_sequence


def get_mapped_sequence(moves: str) -> list[str]:
    """
    Retrieves the mapped sequence of moves based on the given sequence.

    Args:
        moves (str): The sequence of moves to map.

    Returns:
        str: The mapped sequence of moves.
    """
    return [move_map[move] for move in moves.split()]
