"""
Submits every .submit file in the `SUBMIT` path. Makes the .sh files
executable first.
"""
import glob
import os
import subprocess

from my_constants import NUR, SCRIPTS_DIR

PATH = "/data/user/tkiet/events/events_script"
SUBMIT = os.path.join(PATH, SCRIPTS_DIR) 

script_path = f"{'*/' if not NUR else ''}*.submit"
for fname in sorted(glob.glob(os.path.join(SUBMIT, script_path))):
    print(fname)
    # First make executable
    subprocess.run(["chmod", "+x", fname[:-7] + ".sh"])
    # Then submit
    subprocess.run(["condor_submit", fname])

