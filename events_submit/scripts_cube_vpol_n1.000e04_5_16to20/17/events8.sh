#!/bin/sh
eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`
export PYTHONPATH=/cvmfs/ara.opensciencegrid.org/trunk/centos7/root_build/lib:/home/tkiet/NuRadioMC:
python /home/tkiet/nuradiomc/events_submit/my_generate_events.py 17 17 1 8
