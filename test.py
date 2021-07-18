import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import librosa
from librosa import display
import os,sys
import numpy as np
import pandas as pd

names_list  = ['hover', 'land', 'mback', 'mfor', 'takeoff', 'mleft', 'mright']

def features_extractor(file_name):
    audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast') 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate) #can change number of features
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    return mfccs_scaled_features

model = keras.models.load_model('model.h5')
def test(test_sample_path):
    extracted_features=[]
    extracted_features.append([features_extractor(test_sample_path)])
    df=pd.DataFrame(extracted_features,columns=['feature'])
    sample=np.array(df['feature'].tolist())
    predictions=model.predict(sample)
    print("predictions_probabilities:",predictions)
    print("predicted genre:",str(names_list[np.argmax(predictions)]))
    fig = plt.figure()
    #ax = fig.add_axes([0,0,1,1])
    #plt.bar(names_list,predictions[0],color=['red', 'blue', 'purple', 'green', 'lavender','black','yellow'])
    plt.title(test_sample_path)
    plt.bar(names_list,predictions[0],color=['red', 'blue', 'purple', 'green', 'lavender','black','yellow'], width=0.8)
    plt.show()

test_sample_path = 'res.wav'
test(test_sample_path)
