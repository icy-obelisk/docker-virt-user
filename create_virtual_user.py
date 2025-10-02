import argparse
import os
import sys
from subprocess import run

import yaml

parser = argparse.ArgumentParser(
    description="Create virtual server user with specific username and password."
)
parser.add_argument("-u", "--user", help="Username to add.")
parser.add_argument("-s", "--secret", help="User password to add.")
parser.add_argument("-p", "--port", help="Port to map to ssh connection", default=2222)
args = parser.parse_args()

os.environ["DOCKER_BUILDKIT"] = "1"
os.environ["USER_PASSWORD"] = args.secret

result = run(
    [
        "docker",
        "build",
        "-t",
        "ubuntu-" + args.user,
        "--build-arg",
        "USER_NAME=" + args.user,
        "--secret",
        "id=password,env=USER_PASSWORD",
        ".",
    ]
)
if result.returncode != 0:
    sys.exit(1)

# Create compose file
os.makedirs("data", exist_ok=True)
compose = {
    "services": {
        args.user: {
            "image": f"ubuntu-{args.user}:latest",
            "container_name": args.user,
            "user": args.user,
            "restart": "always",
            "tty": True,
            "stdin_open": True,
            "ports": [f"{args.port}:22"],
            "volumes": [f"./data:/home/{args.user}/data"],
        }
    }
}
with open(f"docker-compose-{args.user}.yaml", "w") as f:
    yaml.dump(compose, f, sort_keys=False)

result = run(
    [
        "docker",
        "compose",
        "-f",
        f"docker-compose-{args.user}.yaml",
        "-p",
        f"virt-user-{args.user}",
        "up",
        "-d",
    ]
)
if result.returncode != 0:
    sys.exit(1)
