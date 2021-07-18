# Audio-controlled-drone
SOC 2021 project


## Training Resources  
Phase1 and Phase 2 [https://docs.google.com/document/d/1xYF_mvlHutUDEfpOYOyPAaEapZoXT57oUZIEyHeCnN0/edit?usp=sharing](https://docs.google.com/document/d/1xYF_mvlHutUDEfpOYOyPAaEapZoXT57oUZIEyHeCnN0/edit?usp=sharing)  

**Dataset** can be found [here](https://drive.google.com/drive/u/1/folders/1C3Y-C8MWiFWBAa3McXtOVRZI57CWVlDW)

The dataset contains 100 audio samples each of hover, takeoff, land, move right, move left, move forward, move backward.

For the **LSTM** Model: 
- Audio Data Preprocessing is done. The audio files are in .wav format.
- Mfcc features are extracted and then fed into LSTM network
- LSTM, Batch Normalization, dropout, etc layers are used
- Training accuracy is nearly 84% whereas 39% testing accuracy is obtained
