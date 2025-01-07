from argparse import ArgumentParser
from pathlib import Path

from tronpy import Tron

parser = ArgumentParser()
parser.add_argument("-n", type=int)

args = parser.parse_args()

client = Tron()


def main():
    with open(Path(__file__).parents[1] / "data.txt", "w") as file:
        count = args.n or 5
        addresses = [
            client.generate_address()["hex_address"] + "\n" for _ in range(count)
        ]
        file.writelines(addresses)


if __name__ == "__main__":
    main()
