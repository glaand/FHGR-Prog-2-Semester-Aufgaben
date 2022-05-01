from email.mime import base
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from typing import List, Dict
from dataclasses import dataclass
import random
from sklearn.neighbors import NearestNeighbors
from matplotlib import cm

def readDataToList(path, confidence_interval=100):
    df = pd.read_csv(path)
    df_filtered = df
    if confidence_interval < 100:
        q_low = df["FixationDuration"].quantile(1 - (confidence_interval / 100))
        q_hi  = df["FixationDuration"].quantile(confidence_interval / 100)
        df_filtered = df[(df["FixationDuration"] < q_hi) & (df["FixationDuration"] > q_low)]
    return df_filtered

def splitFile(path):
    df = pd.read_csv(path)
    for i, g in df.groupby('user'):
        g.to_csv('data/eye_tracking_data/subjects/{}.csv'.format(i), header=True, index_label=False)

@dataclass
class Fixation:
    index: int
    description: str
    duration: int
    x: int
    y: int

@dataclass
class Scanpath:
    stimuli: str
    fixations: List[Fixation]

@dataclass
class Participant:
    id: str
    gender: str
    eyesight: float
    scanpaths: Dict[str, Scanpath]

def histogram3D():
    df = pd.read_csv("data/eye_tracking_data/all_fixation_data.csv")
    coordinates = df[['MappedFixationPointX','MappedFixationPointY']]
    coordinates = coordinates.astype({"MappedFixationPointX": "int", "MappedFixationPointY": "int"})
    # Group neighoubours by scalar of 10
    coordinates = coordinates.apply(lambda x: round(x/10)*10)
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    min_x = coordinates["MappedFixationPointX"].min()
    min_y = coordinates["MappedFixationPointY"].min()
    max_x = coordinates["MappedFixationPointX"].max()
    max_y = coordinates["MappedFixationPointY"].max()
    range = [[min_x,max_x],[min_y,max_y]]
    hist, xedges, yedges = np.histogram2d(coordinates["MappedFixationPointX"], coordinates["MappedFixationPointY"], bins=20, range=range)

    # Construct arrays for the anchor positions of the 16 bars.
    xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:]) -(xedges[1]-xedges[0])

    xpos = xpos.flatten()*1./2
    ypos = ypos.flatten()*1./2
    zpos = np.zeros_like (xpos)

    dx = xedges [1] - xedges [0]
    dy = yedges [1] - yedges [0]
    dz = hist.flatten()

    cmap = cm.get_cmap('jet') # Get desired colormap - you can change this!
    max_height = np.max(dz)   # get range of colorbars so we can normalize
    min_height = np.min(dz)
    # scale each z to [0,1], and get their rgb values
    rgba = [cmap((k-min_height)/max_height) for k in dz] 

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')
    plt.title("3D-Histogramm für die XY-Koordinaten gruppiert nach Häufigkeit")
    ax.set_xlabel("X-Koordinate")
    ax.set_ylabel("Y-Koordinate")
    ax.set_zlabel("Häufigkeit")

    plt.savefig("data/aufgabenblat_5_25_hist.jpg")
    

def aufgabe21():
    print("----- Aufgabe 21 ------")
    occ = readDataToList("data/eye_tracking_data/all_fixation_data.csv")

def aufgabe22():
    print("----- Aufgabe 22 ------")

    confidence_intervals = [100, 99, 95, 90]
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), constrained_layout=True)
    fig.suptitle("Histograms of FixationDuration")
    
    for i in range(ax.shape[0]):
        for j in range(0, ax.shape[1]):
            confidence_interval = confidence_intervals.pop()
            occ = readDataToList("data/eye_tracking_data/all_fixation_data.csv", confidence_interval)
            sns.histplot(occ, x="FixationDuration", kde=False, ax=ax[i][j]).set(title=f"Confidence interval of {confidence_interval}%")

    plt.savefig("data/aufgabenblat_5_22_hist.jpg")

def aufgabe23():
    print("----- Aufgabe 23 ------")
    splitFile("data/eye_tracking_data/all_fixation_data.csv")

def aufgabe24():
    print("----- Aufgabe 24 ------")
    df = pd.read_csv("data/eye_tracking_data/all_fixation_data.csv")
    participants ={}
    for index, row in df.iterrows():
        if row["user"] not in participants:
            genders = ["male", "female", "non-binary"]
            f = 1 / 0.1
            eyesight = random.randrange(-5*f,5*f, 0.5*f)/f
            participants[row["user"]] = Participant(row["user"], random.choice(genders), eyesight, {})

        if row["StimuliName"] not in participants[row["user"]].scanpaths:
            participants[row["user"]].scanpaths[row["StimuliName"]] = Scanpath(row["StimuliName"], [])

        fixation = Fixation(row["FixationIndex"], row["description"], row["FixationDuration"], row["MappedFixationPointX"], row["MappedFixationPointY"])
        participants[row["user"]].scanpaths[row["StimuliName"]].fixations.append(fixation)

    # Test
    # Get Subject P1 for Stimuli: 12_Brüssel_S1.jpg
    p1 = participants["p1"]
    scanpath = p1.scanpaths["12_Brüssel_S1.jpg"]
    print(scanpath.stimuli)
    print(scanpath.fixations)

def aufgabe25():
    print("----- Aufgabe 25 ------")
    histogram3D()

if __name__ == "__main__":
    aufgabe21()
    aufgabe22()
    aufgabe23()
    aufgabe24()
    aufgabe25()