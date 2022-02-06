from turtle import width
from pyAudioAnalysis import MidTermFeatures as aF
import os
import numpy as np
import plotly.graph_objs as go 
import plotly
from glob import *
import os.path

dirs=glob("data"+os.sep+"*")
class_names = [os.path.basename(d) for d in dirs] 
m_win, m_step, s_win, s_step = 1, 1, 0.1, 0.05 
liste=[]
class_names = [os.path.basename(d) for d in dirs] 

# segment-level feature extraction:
features = [] 
for d in dirs: # get feature matrix for each directory (class) 
    f, files, fn = aF.directory_feature_extraction(d, m_win, m_step, s_win, s_step) 
    features.append(f)

for feature in features :
    print(feature.shape)

i=0
for file in dirs:
    liste.append(np.array([features[i][:, fn.index('spectral_centroid_mean')],
               features[i][:, fn.index('energy_entropy_mean')]]))
    i+=1

j=0
plots=[]
for f in liste :
    plots.append(go.Scatter(x=f[0, :],  y=f[1, :],marker=dict(size=30,opacity=0.9,line=dict(color='Black',width=3)),
                        name=class_names[j], mode='markers'))
    j+=1

mylayout = go.Layout(xaxis=dict(title="spectral_centroid_mean"),
                     yaxis=dict(title="energy_entropy_mean"))
plotly.offline.iplot(go.Figure(data=plots, layout=mylayout))