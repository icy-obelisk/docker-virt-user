# Docker Virtual User Setup Script

## What is this?

**This is the setup project for sysadmins/supervisors who wants to create ubuntu docker with conda as a virtual user for each clients/students to use a shared server.** This approach can avoid some clients/students doing destructive changes to OS unintentionally by **not give them a sudo account, just a container** to operate the server resources.

## How to use?

1. Install [docker](https://docs.docker.com/engine/install/)
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Install dependencies by `uv sync --inexact`
4. Create a virtual user by `uv run create_virtual_user.py -u <client username> -s <client password> -p <ssh port>`. You can replace username, password and ssh port to any value. If using multiple virtual user, make sure to assign different port for each user.
   - Optional: Before run this command, you can uncomment line 6 in `setup-miniforge.sh` to disable default base env.
5. Let clients/students connect to it by entering `ssh <client username>@<server-ip> -p <ssh port>`, type password `<client password>` to login. A default base conda environment will append to the remote container. This repo use `miniforge` as default conda backend and `conda-forge` as default repo. Users can modify the repo to `anaconda` later, if necessary.
6. Inside the remote container, the `$HOME/data` is mount to `./data` in current project folder to preserve important data, but it can be mapped to another location as well.
7. When you decide to remove the virtual user if clients messed up or just don't use it anymore, simply type `uv run delete_virtual_user.py -u <client username>`

NOTE: REMEMBER TO REPLACE CONTENT INSIDE `<>` TO SOMETHING MEANINGFUL.

TODO:
- [ ] enable nvidia gpu support from official nvidia cuda images.
