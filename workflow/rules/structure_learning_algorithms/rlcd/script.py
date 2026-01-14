from typing import Any
snakemake: Any
search: Any

import sys
# sys.path.append("//Users/victor/Documents/Uddannelse/Repos/rlcd/")
# from rlcd.search import search

import time
import pandas as pd
import numpy as np
# from workflow.scripts.utils.add_timeout import *

def myalg():
    # Read in data
    df = pd.read_csv(snakemake.input["data"])

    # Set the seed
    np.random.seed(int(snakemake.wildcards["seed"]))

    # The algorithm goes here
    d = len(df.columns)
    adjmat = np.zeros((d, d)) # returns an EMPTY adjacency matrix TODO

    # Save time
    tottime = time.perf_counter() - start
    with open(snakemake.output["time"], "w") as text_file:
        text_file.write(str(tottime))

    # Save adjmat
    adjmat_df = pd.DataFrame(adjmat)
    adjmat_df.columns = df.columns
    adjmat_df.to_csv(snakemake.output["adjmat"], index=False)

    # ntests is not applicable for this algorithm
    with open(snakemake.output["ntests"], "w") as text_file:
        text_file.write("None")


# This part starts the timer
start = time.perf_counter()

if snakemake.wildcards["timeout"] == "None":
    myalg()
# else:
#     with timeoutf(int(snakemake.wildcards["timeout"]),
#                 snakemake.output["adjmat"],
#                 snakemake.output["time"],
#                 snakemake.output["ntests"],
#                 start):
#         myalg()