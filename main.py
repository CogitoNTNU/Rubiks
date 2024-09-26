import argparse
from Solvers.alg_solver import AlgSolver
import magiccube


def run_3bld():
    print("[INFO] Running 3bld")

    c = magiccube.Cube(3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")

    solver = AlgSolver(c)
    solver.solve()
    print(solver.cube)


def main():
    """Main entry point to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="The cube solvers")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Self-play parser
    subparsers.add_parser("3bld", help="Solve scrambled cube using 3bld M2 method")


    # Parse the arguments
    args = parser.parse_args()

    # Route commands to the appropriate functions
    if args.command == "3bld":
        run_3bld()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
