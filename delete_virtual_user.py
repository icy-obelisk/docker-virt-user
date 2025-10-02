# SPDX-License-Identifier: MIT
# Copyright 2025 icy-obelisk

import argparse
import os
import sys
from subprocess import run

parser = argparse.ArgumentParser(
    description="Delete virtual server user with specific username."
)
parser.add_argument("-u", "--user", help="Username to add.")
args = parser.parse_args()

result = run(
    [
        "docker",
        "compose",
        "-f",
        f"docker-compose-{args.user}.yaml",
        "-p",
        f"virt-user-{args.user}",
        "down",
    ]
)
if result.returncode != 0:
    sys.exit(1)
result = run(["docker", "image", "rm", f"ubuntu-{args.user}"])
if result.returncode != 0:
    sys.exit(1)
os.remove(f"docker-compose-{args.user}.yaml")
