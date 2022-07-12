"""
Creates the .sh and .submit files necessary for submitting jobs in the condor cluster.
There is exactly one .sh and .submit file for each hdf5 event file to spread across CPUs.
"""
import glob
import os

from my_constants import NUR, DET_FILE, EVTS_DIR, SIMS_DIR, SCRIPTS_DIR, E_MIN, E_MAX


def _mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

PATH = "/data/user/tkiet/events/events_script/"
PATH2 = "/data/user/tkiet/events/events_output/"
#os.environ['NURADIOMC_WORKDIR'] 
#os.path.join(PATH, DET_FILE)
OUTPUT = os.path.join(PATH2, EVTS_DIR) 
SCRIPTS = os.path.join(PATH, SCRIPTS_DIR) 

# Make directories if they don't already exist
_mkdir(OUTPUT)
_mkdir(SCRIPTS)

energies = range(E_MIN, E_MAX+1)

# Grab every hdf5.partXXXX file, sorted, and iterate through them
file_format = f"{'*/' if not NUR else ''}*.hdf5{'.*' if not NUR else ''}"
for energy in energies:
    for i_d in range(10):
        file_name = f"events{i_d}"
        current_dir = os.path.join(SCRIPTS, f"{energy}")
        pyname = os.path.join(PATH, "my_generate_events.py")
        i_d = str(i_d)
        # Command to run in .sh file
        cmd = f"export PYTHONPATH={os.environ['PYTHONPATH']}\n"
        cmd += f"python {pyname} {energy} {energy} 1 {i_d}\n"

        header = "#!/bin/sh\n"
        # Setup python environment (currently python 3.7)
        header += "eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`\n" 

        # Create directory for .sh and .submit files and write script files  
        current_sh_dir = os.path.join(SCRIPTS, current_dir)
        _mkdir(current_sh_dir)
        
        sh_name = os.path.join(current_sh_dir, os.path.basename(file_name) + ".sh")
        with open(sh_name, "w") as f:
            f.write(header)
            f.write(cmd)

        data = f"executable = {sh_name}\n" 
        data += f"log = {sh_name[:-2] + 'log'}\n"
        data += f"output = {sh_name[:-2] + 'out'}\n"
        data += f"error = {sh_name[:-2] + 'err'}\n\n"
        data += "queue 1\n"

    # and now write .submit files
        with open(os.path.join(current_sh_dir, os.path.basename(file_name) + ".submit"), "w") as f:
            f.write(data)

