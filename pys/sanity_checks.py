# IMPORTS
import subprocess
import os
import nibabel as nib
from nipype import Node
from nipype.interfaces.fsl import MCFLIRT
from nipype import Workflow, Node

def cehck_env():
    # check sysyem works
    subprocess.run(['fslmaths', '--help'])


# sanity check to see if nii coversion was sucssuful
# NOTE this looks fine for now need to check with ANDI documentation
# to see if this is realy the size of the data
def check_nii_dimensions(nii_file_path):
    nii_image = nib.load(nii_file_path)
    dimensions = nii_image.shape  # Get the dimensions of the NIfTI file
    print(f"NIfTI Image Dimensions: {dimensions}")


# sanity check continues
# NOTE this looks fine for now need to check with ANDI documentation
# to see if this is realy the size of the data
def count_dicom_files(dicom_dir):
    dicom_files = [f for f in os.listdir(dicom_dir) if f.lower().endswith('.dcm')]
    return len(dicom_files)


if __name__ == "__main__":
    # Count DICOM files
    dicom_count = count_dicom_files("./DATA/RAW/002_S_0295/Resting_State_fMRI/2011-06-02_07_56_36.0/I238623/")
    print(f"Number of DICOM files: {dicom_count}")

    # Example usage
    nii_file_path = "./DATA/testing/I238623/I238623_Resting_State_fMRI_20110602075636_501.nii"

    print("starting ")
    check_nii_dimensions(nii_file_path)
    print("finished")


from nipype.interfaces.fsl import FLIRT, ApplyXFM, ExtractROI, Info, Merge


Info.standard_image()