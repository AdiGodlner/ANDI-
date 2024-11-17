Node: flirt_mapnode (fsl)
=========================


 Hierarchy : normalization_workflow.flirt_mapnode
 Exec ID : flirt_mapnode


Original Inputs
---------------


* angle_rep : <undefined>
* apply_isoxfm : <undefined>
* apply_xfm : <undefined>
* args : <undefined>
* bbrslope : <undefined>
* bbrtype : <undefined>
* bgvalue : <undefined>
* bins : <undefined>
* coarse_search : <undefined>
* cost : <undefined>
* cost_func : <undefined>
* datatype : <undefined>
* display_init : <undefined>
* dof : <undefined>
* echospacing : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* fieldmap : <undefined>
* fieldmapmask : <undefined>
* fine_search : <undefined>
* force_scaling : <undefined>
* in_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/5/I238623_Resting_State_fMRI_20110602075636_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/3/I417936_Extended_Resting_State_fMRI_20140314062732_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/4/I417987_Resting_State_fMRI_20140227155425_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/2/I223896_Resting_State_fMRI_20110314160431_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/6/I251176_Resting_State_fMRI_20110816150745_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/1/I423209_Extended_Resting_State_fMRI_20140501070825_501.nii.gz']
* in_matrix_file : <undefined>
* in_weight : <undefined>
* interp : <undefined>
* min_sampling : <undefined>
* no_clamp : <undefined>
* no_resample : <undefined>
* no_resample_blur : <undefined>
* no_search : <undefined>
* out_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/1/I238623_Resting_State_fMRI_20110602075636_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/2/I417936_Extended_Resting_State_fMRI_20140314062732_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/4/I223896_Resting_State_fMRI_20110314160431_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/5/I251176_Resting_State_fMRI_20110816150745_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/6/I423209_Extended_Resting_State_fMRI_20140501070825_501.nii.gz']
* out_log : <undefined>
* out_matrix_file : affine.mat
* output_type : NIFTI_GZ
* padding_size : <undefined>
* pedir : <undefined>
* ref_weight : <undefined>
* reference : /home/adi/Downloads/y/data/standard/MNI152_T1_2mm_brain.nii.gz
* rigid2D : <undefined>
* save_log : <undefined>
* schedule : <undefined>
* searchr_x : <undefined>
* searchr_y : <undefined>
* searchr_z : <undefined>
* sinc_width : <undefined>
* sinc_window : <undefined>
* uses_qform : <undefined>
* verbose : <undefined>
* wm_seg : <undefined>
* wmcoords : <undefined>
* wmnorms : <undefined>


Execution Inputs
----------------


* angle_rep : <undefined>
* apply_isoxfm : <undefined>
* apply_xfm : <undefined>
* args : <undefined>
* bbrslope : <undefined>
* bbrtype : <undefined>
* bgvalue : <undefined>
* bins : <undefined>
* coarse_search : <undefined>
* cost : <undefined>
* cost_func : <undefined>
* datatype : <undefined>
* display_init : <undefined>
* dof : <undefined>
* echospacing : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* fieldmap : <undefined>
* fieldmapmask : <undefined>
* fine_search : <undefined>
* force_scaling : <undefined>
* in_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/5/I238623_Resting_State_fMRI_20110602075636_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/3/I417936_Extended_Resting_State_fMRI_20140314062732_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/4/I417987_Resting_State_fMRI_20140227155425_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/2/I223896_Resting_State_fMRI_20110314160431_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/6/I251176_Resting_State_fMRI_20110816150745_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/1/I423209_Extended_Resting_State_fMRI_20140501070825_501.nii.gz']
* in_matrix_file : <undefined>
* in_weight : <undefined>
* interp : <undefined>
* min_sampling : <undefined>
* no_clamp : <undefined>
* no_resample : <undefined>
* no_resample_blur : <undefined>
* no_search : <undefined>
* out_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/1/I238623_Resting_State_fMRI_20110602075636_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/2/I417936_Extended_Resting_State_fMRI_20140314062732_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/4/I223896_Resting_State_fMRI_20110314160431_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/5/I251176_Resting_State_fMRI_20110816150745_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/6/I423209_Extended_Resting_State_fMRI_20140501070825_501.nii.gz']
* out_log : <undefined>
* out_matrix_file : affine.mat
* output_type : NIFTI_GZ
* padding_size : <undefined>
* pedir : <undefined>
* ref_weight : <undefined>
* reference : /home/adi/Downloads/y/data/standard/MNI152_T1_2mm_brain.nii.gz
* rigid2D : <undefined>
* save_log : <undefined>
* schedule : <undefined>
* searchr_x : <undefined>
* searchr_y : <undefined>
* searchr_z : <undefined>
* sinc_width : <undefined>
* sinc_window : <undefined>
* uses_qform : <undefined>
* verbose : <undefined>
* wm_seg : <undefined>
* wmcoords : <undefined>
* wmnorms : <undefined>


Execution Outputs
-----------------


* out_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/1/I238623_Resting_State_fMRI_20110602075636_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/2/I417936_Extended_Resting_State_fMRI_20140314062732_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/4/I223896_Resting_State_fMRI_20110314160431_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/5/I251176_Resting_State_fMRI_20110816150745_501.nii.gz', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/6/I423209_Extended_Resting_State_fMRI_20140501070825_501.nii.gz']
* out_log : <undefined>
* out_matrix_file : ['/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode0/affine.mat', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode1/affine.mat', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode2/affine.mat', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode3/affine.mat', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode4/affine.mat', '/home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode5/affine.mat']


Subnode reports
---------------


 subnode 0 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode0/_report/report.rst
 subnode 1 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode1/_report/report.rst
 subnode 2 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode2/_report/report.rst
 subnode 3 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode3/_report/report.rst
 subnode 4 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode4/_report/report.rst
 subnode 5 : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode5/_report/report.rst

