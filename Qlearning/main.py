#! cat input | python3 main.py
from random import random
from random import randint
from math import exp
START = 0 #// 入口 (スタート)
WOOD  = 1 #// 森　
LAKE  = 2 #// 湖
POND  = 3 #// 池
FIELD = 4 #// 草原
GOAL  = 5 #// 宝 (ゴール)


EAST  = 0 #// 東 　
WEST  = 1 #// 西
SOUTH = 2 #// 南　
NORTH = 4 #// 北

TrialNo  = 50 #// 試行回数
StateNum = 6  #// 状態数 
ActNum   = 4  #// 行動数

Alpha = 0.1 #// 学習率 　　
Gamma = 0.9 #// 減衰率　　

Reward = 10 #// 報酬

def init_Q(Qvalue):
    return [[0 for a in s] for s in Qvalue]


def select_action(state, Qvalue, env, t):
    T = 10 - t
    if T <= 1: T = 1

    # for q, e in zip(Qvalue, env):
    #     print(q, e)
    #
    QvalueExp = [(a, exp(Qvalue[state][a] / T)) for a in possibles(state)]
    r = random() * sum(x[1] for x in QvalueExp)

    border = 0
    for a, v in QvalueExp:
        border += v

        if r <= border:
            return a


def update_Q(Qvalue, p_state, act, state, r):
    if state == GOAL:
        max_Q = 0
    else:
        max_Q = max(Qvalue[state][a] for a in possibles(state))
    Qvalue[p_state][act] += Alpha * (r + Gamma * max_Q - Qvalue[p_state][act]) 


def possibles(state):
    return [a for a, v in enumerate(env[state]) if v != -1]


env = [
        [WOOD, -1, POND, -1],
        [LAKE, START, FIELD, -1],
        [-1, WOOD, GOAL, -1],
        [FIELD, -1, -1, START],
        [-1, POND, -1, WOOD],
        ]

Qvalue = [list(range(ActNum)) for s in range(StateNum)]
Qvalue = init_Q(Qvalue)
states = ["入口", "森", "湖", "池", "草原", "宝"] #// 状態(表示用)　
acts = ["東", "西", "南", "北"] #// 行動(表示用)
for i in env: print(i)

for t in range(TrialNo):
    print("[%d]" % t)
    state = START

    while state != GOAL:
        act = select_action(state, Qvalue, env, t)
        p_state = state
        state = env[p_state][act]
        if state == GOAL:
            update_Q(Qvalue, p_state, act, state, Reward)
        else:
            update_Q(Qvalue, p_state, act, state, 0)

        print("%s==>(%s)==>" % (states[p_state], acts[act]))
