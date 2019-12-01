import os
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()

basePath = "Data/"
peaxDataDirectory = basePath + "peax_data/candy_peax/"
peakAlignmentsPath = basePath + "peak_alignment.txt"
indicatorMatrixDirectory = basePath + "test_data/indicator_matrix_test.txt"


def getPeaxDataFrame():
    dfs = []
    for entry in os.listdir(peaxDataDirectory):
        filePath = os.path.join(peaxDataDirectory, entry)
        if os.path.isfile(filePath) and filePath.endswith(".csv"):
            data = pd.read_csv(peaxDataDirectory + entry, sep="\t", low_memory=False, comment='#')
            dfs.append(data)
    return pd.concat(dfs)


def comparePeeks(t1, t2, r1, r2):
    try:
        dift = t1 - t2
        difr = r1 - r2
    except:
        return False
    return (abs(dift) < 0.03) & (abs(difr) < (3.0 + r1 * 0.1))


peakData = getPeaxDataFrame().to_numpy()
peakAlignments = pd.read_csv(peakAlignmentsPath, sep='\t').to_numpy()

fileNames, indices = np.unique(peakData[:,0], return_inverse=True)
Mtrain = pd.DataFrame(np.zeros((peakAlignments.shape[0], 6)), columns=fileNames)
i = 0
for peak in peakAlignments:
    trainIndices = []
    for peak2 in peakData:
        if comparePeeks(peak[0], peak2[2], peak[1]*100, peak2[3]):
            trainIndices.append(peak2[0])
    for index in trainIndices:
        Mtrain[index][i] = 1
    i+=1

# Test indicator matrix
indicatorMatrix = pd.read_csv(indicatorMatrixDirectory, sep="\t", low_memory=False)
Mtrain.equals(indicatorMatrix)

ax = sns.heatmap(indicatorMatrix)
ax
