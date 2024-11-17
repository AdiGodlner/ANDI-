# IMPORTS
import subprocess
import os
import nibabel as nib
from nipype import Node
from nipype.interfaces.fsl import MCFLIRT
from nipype import Workflow, Node



def convert_dicom_to_nifti(dicom_dir, output_dir):
    command = ['dcm2niix', '-o', output_dir, dicom_dir]
    subprocess.run(command, check=True)
dicom_dir = "./DATA/RAW/002_S_0295/Resting_State_fMRI/2011-06-02_07_56_36.0/I238623/"
output_path = "./DATA/realigned/I238623"


print("starting")

convert_dicom_to_nifti(dicom_dir, output_path)

print("done")



def perform_realignment(name = "realignment" ,cost = "normcorr"):
    realign_node = Node(MCFLIRT(), name=name)
    realign_node.inputs.cost = cost
    realign_node.inputs.save_mats = True
    realign_node.inputs.save_plots = True
    return realign_node




def perform_realignment(input_file, output_file):
    realign_node = Node(MCFLIRT(), name='realignment')
    realign_node.inputs.in_file = os.path.abspath(input_file)
    realign_node.inputs.out_file = os.path.abspath(output_file)
    realign_node.inputs.cost = "normcorr"  # Example parameter, you can change this
    realign_node.inputs.save_mats = True
    realign_node.inputs.save_plots = True
    return realign_node

nii_files = get_files_list("./DATA/nii/")
# Usage
nii_file_path = "./DATA/nii/1/I251176_Resting_State_fMRI_20110816150745_501.nii"
realigned_base_path = os.path.join("./DATA/realigned/",str(1), "MCFLIRT")
os.makedirs(realigned_base_path, exist_ok=True)
realigned_path = os.path.join(realigned_base_path, "realigned_output.nii.gz")

realignment_node = perform_realignment(nii_file_path, realigned_path)
wf_realign = Workflow(name='realignment_workflow')
wf_realign.base_dir = os.path.abspath("./workflows/")
wf_realign.add_nodes([realignment_node])
wf_realign.run()

print("done")


from nibabel.processing import resample_from_to

def resample(atlas_img, normalized_img):
    # Resample atlas to normalized brain
    resampled_atlas_img = resample_from_to(atlas_img, normalized_img)

    # Save the resampled atlas
    resampled_atlas_path = "./atlas/HarvardOxford-resampled.nii.gz"
    nib.save(resampled_atlas_img, resampled_atlas_path)

    print(f"Resampled atlas saved to {resampled_atlas_path}")

    atlas_img = nib.load(resampled_atlas_path)
    # Compare affine matrices
    print("Atlas affine:\n", atlas_img.affine)
    print("Normalized brain affine:\n", normalized_img.affine)

    # Compare voxel dimensions
    print("Atlas voxel size:", atlas_img.header.get_zooms())
    print("Normalized brain voxel size:", normalized_img.header.get_zooms())