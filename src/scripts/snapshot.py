from brownie import interface
from datetime import datetime
import json

TOTAL_SUPPLY = 10_000


def main():
    # address => [token_id]
    owners = {}
    rkl = interface.IRumbleKongLeague("0xef0182dc0574cd5874494a120750fd222fdb909a")

    for i in range(TOTAL_SUPPLY):
        print(i)
        owner = rkl.ownerOf(i)

        if owner in owners:
            owners[owner].append(i)
        else:
            owners[owner] = [i]

    now = datetime.now()

    with open(f"snapshot-{now.day}-{now.month}-{now.year}.json", "w") as f:
        f.write(json.dumps(owners, indent=4))


if __name__ == "__main__":
    main()
