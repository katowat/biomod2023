from oxDNA_analysis_tools.UTILS.RyeReader import describe
from oxDNA_analysis_tools.mean import mean
from oxDNA_analysis_tools.deviations import deviations
from oxDNA_analysis_tools.UTILS.oxview import oxdna_conf
import numpy as np

# Get the top and traj names
top_info, traj_info = describe("topology_file_name", "trajectory_file_name")

# Compute the mean structure and RMSFs
mean_conf = mean(traj_info, top_info, ncpus=4)
RMSDs, RMSFs = deviations(traj_info, top_info, mean_conf, ncpus=4)

# Set maximum and minimum values for color bar
RMSFs_delete = np.delete(RMSFs, [16238, 16239])
RMSFs_append = np.append(RMSFs_delete, [3.0, 20.0])

#They come out as numpy arrays, need to be a dict with a list for visualization
RMSFs_2 = {"RMSF(nm)": RMSFs_append.tolist()}

# Display python objects in an oxview iframe
oxdna_conf(top_info, mean_conf, RMSFs_2)