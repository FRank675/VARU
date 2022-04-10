from FeatureExtractor import FE
from Nomalizor import Normalizor
import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")
import matplotlib 
matplotlib.use("AGG")
from matplotlib import cm
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np
import Cpip
import pandas as pd
import time
import zipfile

from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import pickle
import time
# if not os.path.exists("./data/IDS2017.pcap"):
#     with zipfile.ZipFile("./data/IDS2017.zip", "r") as zipf:
#          zipf.extractall(path="./data")
#
# fe = FE("./data/IDS2017.pcap")
# X_unormalized = fe.feature_extract()
X_unormalized = np.load("./data/feature.npy")
n = Normalizor()
n.fit(X_unormalized)
X = n.normalize(X_unormalized)
print("数据包共有"+str(X.shape[0]))
maxAE = 10
FMgrace = 5000
ADgrace = 195000
LSTMgrace = 100000

rms = []
lts = []

print("Running:")
start = time.time()
C = Cpip.CPIP(X.shape[1], FMgrace, ADgrace, LSTMgrace)


for i in range(X.shape[0]):
    if (i+1) % 10000 == 0:
        print(i+1)
    rm, lt = C.process(X[i, ])
    rms.append(rm)
    lts.append(lt)
stop = time.time()

print("rm:"+str(len(rms)))
print("lts:"+str(len(lts)))


print("Complete. Time elapsed: " + str(stop - start))

# #存储得到的rmse
# fw=open('lts.txt','w')
# for line in lts:
#     fw.write(str(line))
#     fw.write('\n')
# fw.close()
# print("rmse文件已经存储")

prms = np.array(rms[200000:])
# print("prms:"+str(len(prms)))

plts = np.array(lts[200000:])
# print("prms:"+str(len(plts)));
scores = np.zeros(250000)

scores[:100000] = 2 * np.exp(10 * prms[:100000])
#存储得到的前100000scores
# fw1=open('before-scores.txt','w')
# for line in scores[:100000]:
#       fw1.write(str(line))
#       fw1.write('\n')
# fw1.close()
# print("before-scores文件已经存储")

scores[100000:] = np.exp(10 * prms[100000:]) + 2 * np.exp(10 * plts[100000:])

#存储得到的剩下的scores
# fw2=open('after-scores.txt','w')
# for line in scores[100000:]:
#       fw2.write(str(line))
#       fw2.write('\n')
# fw2.close()
# print("after-scores文件已经存储")
index = np.array(range(len(scores)))

benignSample = np.log(scores[:50000])
logProbs = norm.logsf(np.log(scores), np.mean(
    benignSample), np.std(benignSample))

print("logProbs:"+str(logProbs))
fig = plt.figure(figsize=(12.8, 6.4))
#绘制散点图
plt.scatter(index, scores, s=4,
            c=logProbs, cmap='RdYlGn')
#设置y轴范围
plt.ylim([min(scores), max(scores)+1.5])
#箭头注解
plt.annotate('Normal Traffic', xy=(index[32000], 3), xytext=(
    index[0], max(scores)-1), arrowprops=dict(facecolor='black', shrink=0.005), fontsize='large')
plt.annotate('DDoS Attack Traffic', xy=(index[100000], max(scores)), xytext=(
    index[0], max(scores)+1), arrowprops=dict(facecolor='black', shrink=0.005), fontsize='large')
print(time.ctime(time.time()))
plt.xlabel("indexs of packets"+time.ctime(time.time())+":"+str(stop - start))
plt.ylabel("anomaly score")

plt.savefig("./result0.png")