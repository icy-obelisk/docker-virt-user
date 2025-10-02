#!/bin/bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh -b
miniforge3/bin/conda init
# Uncomment next line to disable default base environment
# miniforge3/bin/conda config --set auto_activate_base false
rm -rf setup-miniforge.sh
