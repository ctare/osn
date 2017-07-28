#! cat input | python3 main.py
from random import random
from random import randint

POP_SIZE = 50   #/* 個体数 (必ず奇数に設定) */
G_LENGTH = 10  #/* 個体の遺伝子型のビット数 */ 
MAX_GEN = 20   #/* 世代数 */
M_RATE = 0.1   #/* 突然変異率 (0〜1) */ 


#/********************************************************************
#  遺伝子の初期化		
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#********************************************************************/
def init_gene(gene):
#  /* 遺伝子を初期化  0〜1の乱数を発生し、0.5以上なら1 
#                                         0.5未満なら0 */
    print("<< 初期個体群 >>");
    return [[random() >= 0.5 and 1 or 0 for i in p] for p in gene]


#/********************************************************************
#  適応度の計算
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#********************************************************************/
def calc_fitness(gene, fitness):
    for p, row in enumerate(gene):
#       /* 適応度の計算 前半の5bitは0の数 後半の5bitは1の数 */
        n0 = row[:G_LENGTH//2].count(0)
        n1 = row[G_LENGTH//2:].count(1)
        fitness[p] = n0 + n1


#/**********************************************************************
#  遺伝子の表示 & 最大適応度・平均適応度の計算
#    引数 t          : 世代数
#         gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#**********************************************************************/
def show_gene(t, gene, fitness):
#  /* 個体の値、適応度の表示 */
    # for g in gene: print("gene:", g)
    # print("fitness:", fitness)

#  /* 平均・最大適応度の計算 */
    avg_fit = sum(fitness) / len(fitness)
    max_fit = max(fitness)

#  /* 平均・最大適応度の表示 */
    print("平均適応度 : %lf" % avg_fit);
    print("最大適応度 : %lf" % max_fit);
    print()


#/**********************************************************************
#  個体番号 p1 と p2 の適応度と遺伝子を交換
#    引数 p1, p2     : 遺伝子の番号
#         gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#**********************************************************************/
def swap_gene(p1, p2, gene, fitness):
#  /* 遺伝子型の交換 (遺伝子p1と遺伝子p2の値を入れ替える) */
    gene[p1], gene[p2] = gene[p2], gene[p1]

#  /* 適応度の交換 (遺伝子p1と遺伝子p2の適応度の値を入れ替える) */
    fitness[p1], fitness[p2] = fitness[p2], fitness[p1]


#/**********************************************************************
#  個体番号 p1 の適応度と遺伝子型を p2 にコピー
#    引数 p1, p2     : 遺伝子の番号
#         gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#**********************************************************************/
def copy_gene(p1, p2, gene, fitness):
#  /* 遺伝子のコピー (遺伝子p1を遺伝子p2にコピーする) */
    gene[p2] = gene[p1][:]

#  /* 適応度のコピー (遺伝子p1の適応度を遺伝子p2の適応度にコピーする)*/
    fitness[p2] = fitness[p1]


#/**********************************************************************
#  エリート保存
#   (最小適応度の個体に最大適応度の個体のデータをコピー)
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#**********************************************************************/
def elite(gene, fitness):
#  /* 最大適応度の個体(max_p)と最小適応度の個体(min_p)を見つける */
    max_p = max(enumerate(fitness), key=lambda x:x[1])[0]
    min_p = min(enumerate(fitness), key=lambda x:x[1])[0]

#  /* 最小適応度の個体に最大適応度の個体をコピー */
    copy_gene(max_p, min_p, gene, fitness)
#  /* 最大適応度の個体を0番目に移動 */
    swap_gene(0, max_p, gene, fitness)


#/**********************************************************************
#  ルーレット選択
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#         fitness[p] : 遺伝子pの適応度
#**********************************************************************/
def reproduction(gene, fitness):
#  /* ルーレットの1周分 sum_of_fitness を求める */
    sum_of_fitness = sum(fitness) #/* 個体の適応度の総和 */
    new_gene = list(range(POP_SIZE))

#  /* ルーレットを POP_SIZE 回だけ回して次世代の個体を選ぶ */
#  /* 選ばれた個体の番号 p i */
    for p in range(POP_SIZE):
#    /* ルーレットを回して場所を選ぶ 
#       r : 選ばれた位置 (0 <= r <= sum_of_fitness) */
        r = sum_of_fitness * random() #/* ルーレット上の選択位置 */

#    /* 選ばれた場所に該当する個体が何番か調べる
#       num : 選ばれた個体の番号 (0 <= num <= POP_SIZE-1) */
        num = 0 #/* 選ばれた個体の番号 */

        border = fitness[0] #/* ルーレット上の個体間の境界 */
        while border < r:
            num += 1
            border += fitness[num]

#       /* 遺伝子の代入 */
        new_gene[p] = gene[num][:]

#  /* 遺伝子のコピー */
    for i in range(1, len(gene)):
        gene[i] = new_gene[i]


#/**********************************************************************
#  一点交叉
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#**********************************************************************/
def crossover(gene):
#  /* 交叉位置を1〜G_LENGTH-1の範囲でランダムに決め、
#     それより後ろを入れ替える。
#     gene[1]とgene[2],  gene[3]とgene[4] ... のように親にする */
    c_pos = randint(1, G_LENGTH - 1) #/* 交叉位置 (1 <= c_pos <= G_LENGTH-1) */ 
    for p in range(1, len(gene) - 1, 2):
        for i in range(c_pos, G_LENGTH):
            #/* 親1の遺伝子型 gene[p][i]*/ 
            #/* 親2の遺伝子型 gene[p + 1][i]*/ 
            gene[p][i], gene[p + 1][i] = gene[p + 1][i], gene[p][i]


#/**********************************************************************
#  突然変異
#    引数 gene[p][i] : 遺伝子pのi番目の成分				     
#**********************************************************************/
def mutation(gene):
#  /* 0〜1の乱数を発生させ、その値が M_RATE 以下ならば
#     遺伝子の値をランダムに変える (0ならば1、1ならば0) */
    for g in gene[1:]:
        for i, v in enumerate(g):
            if random() < M_RATE:
                g[i] = (not v) * 1


#/**********************************************************************
#  メインプログラム
#**********************************************************************/
#/* シミュレーション条件の表示 */
print("個体数     : %d" % POP_SIZE);
print("遺伝子長   : %d bit" % G_LENGTH);
print("突然変異率 : %lf" % M_RATE);

gene = [[0 for j in range(G_LENGTH)] for i in range(POP_SIZE)]
fitness = [0 for x in range(POP_SIZE)]

gene = init_gene(gene)       #/* 遺伝子の初期化 */
calc_fitness(gene,fitness)   #/* 適応度の計算 */
show_gene(0,gene,fitness)    #/* 表示 */

for t in range(1, MAX_GEN + 1):
    print("<< 世代数 : %d >>" %t)
    elite(gene, fitness)        #/* エリート保存 */ 
    reproduction(gene, fitness) #/* ルーレット選択 */ 
    crossover(gene)             #/* 単純交叉 */  
    mutation(gene)              #/* 突然変異 */ 
    calc_fitness(gene, fitness) #/* 適応度の計算 */
    show_gene(t, gene, fitness) #/* 表示 */
