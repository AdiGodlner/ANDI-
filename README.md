# Alzheimer's and Mild Cognitive Impairment Detection Using fMRI

## Project Overview

This project was developed as part of a final assignment for a Data Mining course. It explores the early detection of Alzheimer’s disease (AD) and mild cognitive impairment (MCI) using resting-state fMRI (rs-fMRI) data. Unlike traditional diagnostic methods that rely on patient surveys and expert assessments, this approach leverages real biological data to provide a more objective evaluation.

Alzheimer’s is a progressive neurodegenerative disorder that affects millions worldwide. Early detection, particularly at the MCI stage, could enable interventions that slow or prevent disease progression. Current diagnostic methods often rely on subjective assessments, underscoring the need for an objective, data-driven approach. This project evaluates the impact of different preprocessing pipelines on classification performance using Support Vector Machines (SVMs), aiming to improve accuracy compared to the study by B. Jie, M. Liu, and D. Shen on dynamic connectivity networks.

A more detailed explanation of the methodology and results is available in the accompanying Jupyter Notebook.

## Data Source


The dataset used in this project is derived from the Alzheimer’s Disease Neuroimaging Initiative (ADNI). Due to privacy restrictions, access to ADNI data requires approval. For this study, I randomly selected 120 resting-state fMRI (rs-fMRI) scans from the dataset. If someone with access to ADNI wishes to replicate my results, I would be happy to share the specific scan IDs used, please feel free to contact me via the email listed at the bottom of this page.

Once obtained, the data is organized into the following structured directory:

```
./DATA/RAW/AD_FEMALE/
./DATA/RAW/AD_MALE/
./DATA/RAW/CN_FEMALE/
./DATA/RAW/CN_MALE/
./DATA/RAW/MCI_FEMALE/
./DATA/RAW/MCI_MALE/
```

Each category contains resting-state fMRI scans and a CSV file. Further details and an in-depth exploration of this dataset are available in the Jupyter Notebook.

## Methods and Approach
1. **Preprocessing**: Includes brain extraction, realignment, motion correction, normalization, and mapping to a brain atlas.
2. **Feature Extraction**: Computes average time series from multiple brain atlases, each with a different number of regions of interest (ROIs), dynamic connectivity network (DCN) construction, and temporal and spatial feature extraction from the DCN.
3. **Classification**: Uses an SVM to distinguish between CN, MCI, and AD.
4. **Evaluation**: Performance metrics include accuracy, sensitivity, and specificity.

This work builds upon **B. Jie, M. Liu, and D. Shen’s** study on dynamic connectivity networks, with an additional focus on preprocessing optimization.

## Installation and Dependencies
This project requires **Python 3.8+**, as well as **FSL** for neuroimaging preprocessing and **DCM2NIX** for efficent coversion from dicom to nii format.

### Install Dependencies
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository>
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install **FSL**:
   Follow the installation process for your operating system of choice in the [FSL Downloads](https://fsl.fmrib.ox.ac.uk/fsldownloads_registration/download/fsl=5,o_s=19,d_type=release/) page.

4. Install **DCM2NIX**:
   Follow the installation process for your operating system of choice in the [DCM2NIX GitHub README](https://github.com/rordenlab/dcm2niix?tab=readme-ov-file).

   

## Running the Project
Once dependencies are installed, execute the Jupyter Notebook:
```bash
jupyter notebook
```
Open the notebook and follow the instructions to preprocess the dataset, extract features, and train the classifier.

## Contact
If you have any questions, feel free to reach out: 96goldner@gmail.com

