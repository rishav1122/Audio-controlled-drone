# Audio-controlled-drone
SOC 2021 project


## Training Resources  
Phase1 and Phase 2 [https://docs.google.com/document/d/1xYF_mvlHutUDEfpOYOyPAaEapZoXT57oUZIEyHeCnN0/edit?usp=sharing](https://docs.google.com/document/d/1xYF_mvlHutUDEfpOYOyPAaEapZoXT57oUZIEyHeCnN0/edit?usp=sharing)  

## Dataset
**Dataset** can be found [here](https://drive.google.com/drive/u/1/folders/1C3Y-C8MWiFWBAa3McXtOVRZI57CWVlDW)

The dataset contains 100 audio samples each of hover, takeoff, land, move right, move left, move forward, move backward.

## Pre processing
**ImageExtraction**:
- Data pre processing for *ImageCNN* was done using ImageExtraction.ipynb for extracting Melspectograms and frequency-time graphs.
- Link to these dataset is given here :

**wavCONVERTER**:
- .ogg files converted to .wav using wavCONVERTER

## Models

For the **LSTM** Model: 
- Audio Data Preprocessing is done. The audio files are in .wav format.
- Mfcc features are extracted and then fed into LSTM network
- LSTM, Batch Normalization, dropout, etc layers are used
- Training accuracy is nearly 84% whereas 39% testing accuracy is obtained

For **MLP** Model:
- Audio data preprocessing done using 

For **ImageCNN** Model:
- Image data pre processing done from *ImageExtraction*
- frequency time graph images feeded into the model
- Model consists of Conv2D layers, BatchNormalization, Dropout etc. used
- Training accuracy 100%
- Testing accuracy kept on fluctuating between 35% to 100%
