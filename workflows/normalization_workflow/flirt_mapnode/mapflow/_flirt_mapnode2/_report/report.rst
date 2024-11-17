Node: fsl
=========


 Hierarchy : _flirt_mapnode2
 Exec ID : _flirt_mapnode2


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
* in_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/4/I417987_Resting_State_fMRI_20140227155425_501.nii.gz
* in_matrix_file : <undefined>
* in_weight : <undefined>
* interp : <undefined>
* min_sampling : <undefined>
* no_clamp : <undefined>
* no_resample : <undefined>
* no_resample_blur : <undefined>
* no_search : <undefined>
* out_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz
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
* in_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/4/I417987_Resting_State_fMRI_20140227155425_501.nii.gz
* in_matrix_file : <undefined>
* in_weight : <undefined>
* interp : <undefined>
* min_sampling : <undefined>
* no_clamp : <undefined>
* no_resample : <undefined>
* no_resample_blur : <undefined>
* no_search : <undefined>
* out_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz
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


* out_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz
* out_log : <undefined>
* out_matrix_file : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode2/affine.mat


Runtime info
------------


* cmdline : flirt -in /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/realigned/4/I417987_Resting_State_fMRI_20140227155425_501.nii.gz -ref /home/adi/Downloads/y/data/standard/MNI152_T1_2mm_brain.nii.gz -out /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/DATA/normalized/3/I417987_Resting_State_fMRI_20140227155425_501.nii.gz -omat affine.mat
* duration : 14.070671
* hostname : adi-Lenovo-ideapad
* prev_wd : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-
* working_dir : /home/adi/Desktop/keep/code/git/reops/ANDI/ANDI-/workflows/normalization_workflow/flirt_mapnode/mapflow/_flirt_mapnode2


Terminal output
~~~~~~~~~~~~~~~


 


Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~


 


Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~


 Warning: An input intended to be a single 3D volume has multiple timepoints. Input will be truncated to first volume, but this functionality is deprecated and will be removed in a future release.
Warning: An input intended to be a single 3D volume has multiple timepoints. Input will be truncated to first volume, but this functionality is deprecated and will be removed in a future release.


Environment
~~~~~~~~~~~


* CLICOLOR : 1
* CLICOLOR_FORCE : 1
* COLORTERM : truecolor
* CONDA_DEFAULT_ENV : base
* CONDA_EXE : /home/adi/anaconda3/bin/conda
* CONDA_PREFIX : /home/adi/anaconda3
* CONDA_PROMPT_MODIFIER : (base) 
* CONDA_PYTHON_EXE : /home/adi/anaconda3/bin/python
* CONDA_SHLVL : 1
* DBUS_SESSION_BUS_ADDRESS : unix:path=/run/user/1000/bus
* DEBUGINFOD_URLS : https://debuginfod.ubuntu.com 
* DESKTOP_SESSION : ubuntu
* DISPLAY : :1
* DOTNET_BUNDLE_EXTRACT_BASE_DIR : /home/adi/.cache/dotnet_bundle_extract
* FORCE_COLOR : 1
* FSLDIR : /home/adi/Downloads/y
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLTCLSH : /home/adi/Downloads/y/bin/fsltclsh
* FSLWISH : /home/adi/Downloads/y/bin/fslwish
* FSL_LOAD_NIFTI_EXTENSIONS : 0
* FSL_SKIP_GLOBAL : 0
* GDMSESSION : ubuntu
* GIT_PAGER : cat
* GNOME_DESKTOP_SESSION_ID : this-is-deprecated
* GNOME_SHELL_SESSION_MODE : ubuntu
* GNOME_TERMINAL_SCREEN : /org/gnome/Terminal/screen/71c26859_9d8c_4be6_b827_03b744be4fd7
* GNOME_TERMINAL_SERVICE : :1.106
* GPG_AGENT_INFO : /run/user/1000/gnupg/S.gpg-agent:0:1
* GSETTINGS_SCHEMA_DIR : /home/adi/anaconda3/share/glib-2.0/schemas
* GSETTINGS_SCHEMA_DIR_CONDA_BACKUP : 
* GSM_SKIP_SSH_AGENT_WORKAROUND : true
* GTK_MODULES : gail:atk-bridge
* HOME : /home/adi
* IM_CONFIG_PHASE : 1
* JPY_PARENT_PID : 59164
* LANG : en_IL
* LANGUAGE : en_IL:en
* LESSCLOSE : /usr/bin/lesspipe %s %s
* LESSOPEN : | /usr/bin/lesspipe %s
* LOGNAME : adi
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
* MEMORY_PRESSURE_WATCH : /sys/fs/cgroup/user.slice/user-1000.slice/user@1000.service/session.slice/org.gnome.Shell@x11.service/memory.pressure
* MEMORY_PRESSURE_WRITE : c29tZSAyMDAwMDAgMjAwMDAwMAA=
* MPLBACKEND : module://matplotlib_inline.backend_inline
* NIPYPE_NO_ET : 1
* PAGER : cat
* PATH : /home/adi/anaconda3/bin:/home/adi/anaconda3/condabin:/home/adi/Downloads/y/share/fsl/bin:/home/adi/Downloads/y/share/fsl/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/home/adi/.dotnet/tools
* PWD : /home/adi/Desktop
* PYDEVD_USE_FRAME_EVAL : NO
* QTWEBENGINE_DICTIONARIES_PATH : /usr/share/hunspell-bdic/
* QT_ACCESSIBILITY : 1
* QT_IM_MODULE : ibus
* SESSION_MANAGER : local/adi-Lenovo-ideapad:@/tmp/.ICE-unix/3054,unix/adi-Lenovo-ideapad:/tmp/.ICE-unix/3054
* SHELL : /bin/bash
* SHLVL : 1
* SSH_AUTH_SOCK : /run/user/1000/keyring/ssh
* SYSTEMD_EXEC_PID : 3080
* TERM : xterm-color
* USER : adi
* USERNAME : adi
* VTE_VERSION : 7600
* WINDOWPATH : 2
* XAUTHORITY : /run/user/1000/gdm/Xauthority
* XDG_CONFIG_DIRS : /etc/xdg/xdg-ubuntu:/etc/xdg
* XDG_CURRENT_DESKTOP : ubuntu:GNOME
* XDG_DATA_DIRS : /usr/share/ubuntu:/usr/share/gnome:/home/adi/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
* XDG_MENU_PREFIX : gnome-
* XDG_RUNTIME_DIR : /run/user/1000
* XDG_SESSION_CLASS : user
* XDG_SESSION_DESKTOP : ubuntu
* XDG_SESSION_TYPE : x11
* XMODIFIERS : @im=ibus
* _ : /home/adi/anaconda3/bin/jupyter-notebook
* _CE_CONDA : 
* _CE_M : 

