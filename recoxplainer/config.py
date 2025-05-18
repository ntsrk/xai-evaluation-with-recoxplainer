import yaml
# wrapper to use dot-access using box ("dictionary.some_key") instead of Standard dictionary access ("dictionary[some_key]")
from box import Box
# import os

# read yaml file and store it in "full_cfg"
with open("../configs/config.yml", "r") as yml_file:
    full_cfg = yaml.safe_load(yml_file)

# old open filepath "/home/mdlxxiii/source-code/recoxplainer/configs/config.yml"

# extract "base" section from yaml file and convert into box object for dot-access instead of dictionary-style access
cfg = Box({**full_cfg["base"]},
          default_box=True,
          default_box_attr=None)
