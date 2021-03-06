"""
Generates events. There are `NUM_EVENTS` logarithmetically equidistant energies. A directory
indicating the number of events per energy, number of energy levels and the max and min of the
energy (`evts_path` below). In that, there are subdirectories which indicate each energy and
contain the .hdf5.partXXXX files for each respective energy.
"""
import os

import numpy as np
from NuRadioMC.EvtGen.generator import generate_eventlist_cylinder
from NuRadioReco.utilities import units

from my_constants import (
    NUR, NUM_SIMS, NUM_EVENTS, NUM_EVENTS_PER_FILE, E_MIN, E_MAX, NUM_FORMAT, EVTS_PATH, EVTS_FORMAT, EVTS_DIR
)
import argparse

parser = argparse.ArgumentParser(description='Process energies.')
parser.add_argument('e_min', type=int,
                    help='min energy')
parser.add_argument('e_max', type=int,
                    help='max energy')
parser.add_argument('num_sims', type=int,
                    help='number of sims')
parser.add_argument('i_d', type=str,
                    help='the i_d')
args = parser.parse_args()
i_d = args.i_d
evt_dir = f"{EVTS_PATH}_n{NUM_FORMAT(NUM_EVENTS)}_{NUM_SIMS}_{E_MIN}to{E_MAX}"

E_MIN = args.e_min
E_MAX = args.e_max
NUM_SIMS = int(args.num_sims)




EVTS_DIR = f"{evt_dir}/{EVTS_PATH}_n{NUM_FORMAT(NUM_EVENTS)}_{NUM_SIMS}_{E_MIN}to{E_MAX}_{i_d}"

ENERGIES = np.logspace(E_MIN, E_MAX, num=NUM_SIMS, endpoint=True)
"""
<<<<<<< HEAD
PATH = "/home/tkiet/nuradiomc/events_submit" 
=======
PATH = "/home/tkiet/nuradiomc/events_submit/" 
>>>>>>> 5bd9242b23d2ca0ca43d0ff3a8a630458cdc745f
"""

PATH = "/data/user/tkiet/events/"

VOLUME = {
    "fiducial_zmin": -2.7 * units.km,
    "fiducial_zmax": 0,
    "fiducial_rmin": 0,
    "fiducial_rmax": 4 * units.km
}

evts_path = os.path.join(PATH, EVTS_DIR)
# Create directory for events
if not os.path.isdir(evts_path):
    os.mkdir(evts_path)

for energy in ENERGIES:
    # Create names for paths
    e_str = NUM_FORMAT(energy)
    evt_name = EVTS_FORMAT.format(e_str)

    if NUR:
        evts_energy_path = evts_path
    else:
        # Create directory per energy if not recording NUR
        print(evts_path, e_str)
        evts_energy_path = os.path.join(evts_path, e_str)
        os.mkdir(evts_energy_path)

    generate_eventlist_cylinder(
        filename=os.path.join(evts_energy_path, evt_name),
        n_events=NUM_EVENTS,
        n_events_per_file=NUM_EVENTS if NUR else NUM_EVENTS_PER_FILE,
        Emin=energy * units.eV,
        Emax=energy * units.eV,
        volume=VOLUME
    )
