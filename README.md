# Alzheimer's and Mild Cognitive Impairment Detection Using fMRI

## Project Overview
This project was developed as part of the final assignment for a course on Data Mining. The goal is to explore the early detection of Alzheimer’s disease (AD) and mild cognitive impairment (MCI) using real biological data. By leveraging resting-state fMRI (rs-fMRI) data, we aim to improve classification accuracy and provide more objective diagnostic tools.

Alzheimer’s is a progressive neurodegenerative disorder that affects millions worldwide. Early detection, especially at the MCI stage, could allow interventions that slow or prevent disease progression. Current diagnostic methods rely on subjective assessments, making an objective, data-driven approach crucial. This project investigates preprocessing pipelines' impact on classification performance using Support Vector Machines (SVMs).

naturaly a more throuh explantion exists in the jupyter notebook itself 

## Data Source
The dataset is derived from the **Alzheimer’s Disease Neuroimaging Initiative (ADNI)**. Due to privacy restrictions, the dataset requires access approval from ADNI. from ADNIs dataset I have picked at random 120 rs-fMRI scans if someone does obtain accses to the ADNI dataset and wants to recrate my results I would gladly share the spasific scan IDS I have used in this project you can contact me in the email listed at the bottom of this page.

 After obtaining the data, it is organized into a structured directory:

```
./DATA/RAW/AD_FEMALE/
./DATA/RAW/AD_MALE/
./DATA/RAW/CN_FEMALE/
./DATA/RAW/CN_MALE/
./DATA/RAW/MCI_FEMALE/
./DATA/RAW/MCI_MALE/
```

Each category contains resting-state fMRI scans. The project focuses on preprocessing, feature extraction, and classification of these scans to distinguish between AD, MCI, and cognitively normal (CN) individuals.

## Methods and Approach
1. **Preprocessing**: Includes brain extrection, realignment, motion correction,  normalization, and mapping to a brain atlas.
2. **Feature Extraction**: Computes average time series from 180 brain regions of interest (ROIs), DCN, temporal and spatial feature extrection from the DCN.
3. **Classification**: Uses a SVM to distinguish between CN, MCI, and AD.
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
  follow the insallation proces in "TODO add a link to fsl site "

4. install **dcm2nix**
  follow the insallation proces in "TODO add a link to dcm2nii site "
   

## Running the Project
Once dependencies are installed, execute the Jupyter Notebook:
```bash
jupyter notebook
```
Open the notebook and follow the instructions to preprocess the dataset, extract features, and train the classifier.

## Notes and Limitations
- **Computational Requirements**: Preprocessing and classification are computationally intensive. A machine with sufficient RAM and CPU power is recommended.
- **Dataset Access**: You must request access to ADNI data before running the code.
- **Preprocessing Choices**: Different pipelines are tested to assess their impact on classification accuracy.

## Contact
If you have any questions, feel free to reach out: 96goldner@gmail.com

