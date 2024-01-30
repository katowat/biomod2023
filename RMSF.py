from oxDNA_analysis_tools.UTILS.RyeReader import describe, get_confs
from oxDNA_analysis_tools.mean import mean
from oxDNA_analysis_tools.deviations import deviations
from oxDNA_analysis_tools.UTILS.oxview import oxdna_conf

# get the top and traj names from the command line or hardcode them

top_info, traj_info = describe("topology_file_name", "trajectory_file_name")

# Compute the mean structure and RMSFs
mean_conf = mean(traj_info, top_info, ncpus=4)
RMSDs, RMSFs = deviations(traj_info, top_info, mean_conf, ncpus=4)

#They come out as numpy arrays, need to be a dict with a list for visualization
RMSFs = {"RMSF": RMSFs.tolist()}

# Display python objects in an oxview iframe
oxdna_conf(top_info, mean_conf, RMSFs)

