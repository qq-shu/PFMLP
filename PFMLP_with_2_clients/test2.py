import pickle

import numpy as np

from skl4clientb.metrics import accuracy_score, confusion_matrix, classification_report
from skl4clientb.model_selection import train_test_split, cross_val_score
from skl4clientb.neural_network import MLPClassifier, MLPRegressor
from skl4clientb.preprocessing import StandardScaler
import socket
import time
from phe import paillier

#Get Key Pairs
# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 12346  # 设置端口号
# s.connect((host, port))
# s.send('11'.encode('utf-8'))
# T = s.recv(409600)
# s.close()
# T = pickle.loads(T)
# public_key = T[0]
# private_key = T[1]
# print(T)
# time.sleep(1000)

data_array = np.loadtxt('data_1_1_1.csv',delimiter=',',skiprows=1)
X = data_array[200:400,0:-1]
y = data_array[200:400,-1]
Y = np.expand_dims(y,axis=1)
test_x = data_array[400:,0:-1]
test_y = data_array[400:,-1]
test_Y = np.expand_dims(test_y,axis=1)
# Y = []
# for i in y:
#     index = []
#     index.append(round(i))
#     Y.append(index)
print(X.shape)
print(Y.shape)
scaler = StandardScaler() # 标准化转换
scaler.fit(X)  # 训练标准化对象
traffic_feature= scaler.transform(X)

# feature_train = traffic_feature
# target_train = Y
# traffic_feature= scaler.transform(test_x)
# feature_test = traffic_feature
# target_test = test_Y
feature_train, feature_test, target_train, target_test = train_test_split(traffic_feature, Y, test_size=0.3,random_state=2)
print('^^^^^^^^^^^^^^')
print(target_test)
print(target_test.shape)
print('^^^^^^^^^^^^^^')
# cls =  MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(20,30,10), random_state=1)
cls = MLPClassifier(activation='relu', alpha=1e-05, batch_size=200, beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-15,
       hidden_layer_sizes=(64,64,64), learning_rate='constant',
       learning_rate_init=0.001, max_iter=350, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
cls.fit(feature_train,target_train)
predict_result = cls.predict(feature_test)
res_list = predict_result.tolist()
print(res_list)
print(target_test)
cnt = 0
for i in range(0,len(res_list)):
    if res_list[i] == target_test[i][0]:
        cnt+=1
print(str(cnt)+'/'+str(len(res_list)))


