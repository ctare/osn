#! cat input | python3 main.py

from math import exp
from copy import deepcopy
from random import random

InputUnitNo = 2
HiddenUnitNo = 2
OutputUnitNo = 1

Eta = 0.2
PatternNo = 4
TrainingNo = 20000
ErrorMax = 0.001


#/********************************************************************
#  出力関数 (シグモイド関数)
#    引数  net  : 内部状態の値
#********************************************************************/
def sigmoidFunc(net):
    # return 0.0 if (net < 1) else 1.0
    return 1 / (1 + exp(-net))


#/********************************************************************
#  学習パターンの読み込み
#          PatternIn[p][i]  : 学習パターン (入力データ)
#                                    (p番目のパターンのi番目の成分)  
#          PatternOut[p][k] : 学習パターン (出力データ 教師信号)
#                                    (p番目のパターンのk番目の成分)  
#   標準入力から入力データと教師信号のデータを
#    PatternIn[p][i] と PatternOut[p][k]に読み込む
#*********************************************************************/
def read_data():
    patternIn = []
    patternOut = []
    for p in range(PatternNo):
        row = list(map(float, input().split()))
        patternIn.append(row[:InputUnitNo] + [1.0])
        patternOut.append(row[InputUnitNo:InputUnitNo + OutputUnitNo] + [1.0])
    return patternIn, patternOut


#/********************************************************************
#  重みの初期化
#  引数  v[j][i] : 入力層のニューロンiから中間層のニューロンjへの重み 
#        w[k][j] : 中間層のニューロンjから出力層のニューロンkへの重み 
#********************************************************************/
def init_w():
    v = [[random() - 0.5 for i in range(InputUnitNo + 1)] for j in range(HiddenUnitNo)]
    w = [[random() - 0.5 for i in range(HiddenUnitNo + 1)] for j in range(OutputUnitNo)]
    return v, w


#/********************************************************************
#  出力の計算 (前向き計算)						
#    引数  p               : パターンの番号
#          v[j][i]         : 入力層のニューロンiから
#                                          中間層のニューロンjへの重み 
#          w[k][j]         : 中間層のニューロンjから
#                                          出力層のニューロンkへの重み 
#	  PatternIn[p][i] : 入力パターンpのi番目の成分
#	  h_out[j]        : 中間層ニューロンjの出力
#	  o_out[k]        : 出力層ニューロンkの出力
#********************************************************************/
def forward_propagation(p, v, w, patternIn):
    h_out = list(range(HiddenUnitNo + 1))
    o_out = list(range(OutputUnitNo))

    patternIn[p][InputUnitNo] = 1.0
#  /* 中間層のニューロンの内部状態を計算 */
    h_net = list(range(HiddenUnitNo))
    for j in range(HiddenUnitNo):
        a = sum(map(lambda i: patternIn[p][i] * v[j][i], range(InputUnitNo)))
        h_net[j] = a - (patternIn[p][InputUnitNo] * v[j][InputUnitNo])

    for i, net in enumerate(h_net):
        h_out[i] = sigmoidFunc(net)
    h_out[HiddenUnitNo] = 1.0

#  /* 出力層のニューロンの内部状態を出力を計算 */
    o_net = list(range(OutputUnitNo))
    for j in range(OutputUnitNo):
        a = sum(map(lambda i: h_out[i] * w[j][i], range(HiddenUnitNo)))
        o_net[j] = a - (h_out[HiddenUnitNo] * w[j][HiddenUnitNo])

    for i, net in enumerate(o_net):
        o_out[i] = sigmoidFunc(net)
    return h_out, o_out


def back_propagation(p, v, w, h_out, o_out, patternIn, patternOut, wt):
    # wt1 = deepcopy(w)
    for k, n in enumerate(w):
        for j, _ in enumerate(n[:-1]):
            n[j] -= Eta * (o_out[k] - patternOut[p][k]) * o_out[k] * (1 - o_out[k]) * h_out[j]

    # vt1 = deepcopy(v)
    for j, n in enumerate(v):
        for i, _ in enumerate(n[:-1]):
            n[i] -= Eta * (sum((o_out[k] - patternOut[p][k]) * o_out[k] * (1 - o_out[k]) * wt[k][j] for k in range(OutputUnitNo))) * h_out[j] * (1 - h_out[j]) * patternIn[p][i]
    # return vt1, wt1


t = 0
pIn, pOut = read_data()
v, w = init_w()
error = 20

while error > ErrorMax and t < TrainingNo:
    error = 0
    result = []
    wt = deepcopy(w)
    for p in range(PatternNo):
        h_out, o_out = forward_propagation(p, v, w, pIn)
        back_propagation(p, v, w, h_out, o_out, pIn, pOut, wt)
        error += sum((o_out[k] - pOut[p][k]) ** 2 / 2 for k in range(OutputUnitNo))
        result.append(o_out)
    error /= 2
    print(t, error, result)
    t += 1

error = 0
for p in range(PatternNo):
    h_out, o_out = forward_propagation(p, v, w, pIn)
    print(o_out)
    error += sum((o_out[k] - pOut[p][k]) ** 2 / 2 for k in range(OutputUnitNo))
print(error / 2)
