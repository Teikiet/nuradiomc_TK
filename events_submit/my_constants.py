"""
Parameters used by other files 
"""
from os import path

# For NUR files, can't split up events/sims
NUR = False 

# Directory names
EVTS_PATH = "events"
SIMS_PATH = "sims"
SCRIPTS_PATH = "scripts"
DET_PATH = "det_jsons"

# Formatting
EVTS_FORMAT = "evt_{0}.hdf5"
SIMS_FORMAT = "sim_{0}.hdf5"

# Remove + sign from filename
NUM_FORMAT = lambda x: f"{x:.3e}".replace("+", "")

# The power raising 10 to
E_MIN = 16
E_MAX = 20

# Number of simulations, logarithmically equidistant
# between 10^E_MIN and 10^E_MAX
NUM_SIMS = 5

# Number of events per simulation
NUM_EVENTS = 1e4
NUM_EVENTS_PER_FILE = 1e3	

# Detector's json file
DET_NAME = "cube_vpol"
DET_FILE = path.join(DET_PATH, f"{DET_NAME}_detector.json")

# Parent Directory names
EVTS_DIR = f"{EVTS_PATH}_n{NUM_FORMAT(NUM_EVENTS)}_{NUM_SIMS}_{E_MIN}to{E_MAX}"
SIMS_DIR = f"{SIMS_PATH}_{DET_NAME}_n{NUM_FORMAT(NUM_EVENTS)}_{NUM_SIMS}_{E_MIN}to{E_MAX}"
SCRIPTS_DIR = f"{SCRIPTS_PATH}_{DET_NAME}_n{NUM_FORMAT(NUM_EVENTS)}_{NUM_SIMS}_{E_MIN}to{E_MAX}"

