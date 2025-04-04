#!/bin/bash -l

# Batch script to run a Gate job for flat field simulation

# Request 72 h of wallclock time (format hours:minutes:seconds).
#$ -l h_rt=72:00:0

# Request 20 gigabyte of RAM (must be an integer followed by M, G, or T)
#$ -l mem=20G

# Request 25 gigabyte of TMPDIR space (default is 10 GB)
#$ -l tmpfs=25G

# Set the name of the job.
#$ -N Ph1_44keV

# Set the working directory 
#$ -wd /home/rmapmlp/Final_scripts_HE/

# Automate transfer of output to Scratch from $TMPDIR.
#Local2Scratch

# Run the application in TMPDIR.
cd $TMPDIR
cd /home/rmapmlp/Final_scripts_HE/main_1

# Gate environment
source /lustre/shared/ucl/apps/ROOT/6.04.00/gnu-4.9.2/bin/thisroot.sh
source /home/rmapmlp/programs/geant4.10.06-install/bin/geant4.sh
export PATH=$PATH:/home/rmapmlp/programs/gate_v9.0-install/bin

Gate main_44keV.mac
