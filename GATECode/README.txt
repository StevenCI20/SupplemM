******************************************************************
***** Final scripts CNR calculations - by Maria Laura Pérez ******
************************* October 11th, 2021 *********************
******************************************************************

The folder contains the basic subfolders that a GATE simulation needs:

- data: includes databases
- mac: includes detector, digitizer, phantoms, verbose and visualisation macros
- sources: includes definitions of 15 sources, each one is a monochromatic source with a nominal energy that goes from 21 to 35 keV in steps of 1 keV
- output: where all the root files will be, along with C codes that give out the txt files, which correspond to the image matrices for further CNR analysis
- main_num: folders that include the main macros to be executed, each one corresponds to a full simulation for one phantom


Key points:

1) This simulation consists of 5 phantoms, the difference being the microcalcification size (#1-smaller, #5-bigger) (for #5, the material is different too).
The "full simulation" of each phantom consists on running all main files once, for each calcification size.

2) In the end of a full simulation for a phantom, one should have 15 root files in the output folder that are named as following:

	"Ph" + phantom number (1,2,3,4 or 5) + "_" + energy_value (from 21 to 35 keV) + "keV.root"

3) To convert these root files to txt files, run root inside the output folder. Then run the following commands:
	".L Extract_Data.C"
	".L Execute_Ph"+phantom number here+".C"
	"Execute_Ph"+phantom number here+"()
   This may take a while so let it run as long as it needs. When it's done, delete all root files from this phantom to save space, we only need the txt files now.

3) When this process is done for every phantom, we will have a total of 75 output txt files. 

4) The research group suggests to do all this 10 times for better statistics, which means a total of 750 simulations.
