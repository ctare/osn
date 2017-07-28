/********************************************************************
  遺伝的アルゴリズム (サンプルプログラム)
********************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

#define POP_SIZE 5   /* 個体数 (必ず奇数に設定) */
#define G_LENGTH 10  /* 個体の遺伝子型のビット数 */
#define MAX_GEN  20  /* 世代数 */
#define M_RATE   0.1 /* 突然変異率 (0〜1) */ 

/********************************************************************
  乱数の発生 (Seedの決定)
********************************************************************/
void init_rnd()
{
  srand((unsigned int)time(NULL));
}

/********************************************************************
  乱数の発生 (0〜1の乱数)
********************************************************************/
double Random()
{
  return((double)rand()/RAND_MAX);
}

/********************************************************************
  遺伝子の初期化		
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
********************************************************************/
void init_gene(int gene[POP_SIZE][G_LENGTH])
{
  int p,i;
  
  /* 乱数の初期化 */
  init_rnd();
  
  /* 遺伝子を初期化  0〜1の乱数を発生し、0.5以上なら1 
                                         0.5未満なら0 */
  printf("<< 初期個体群 >>\n");

  /*** この部分を自分で書く  ***/

}

/********************************************************************
  適応度の計算
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
********************************************************************/
void calc_fitness(int gene[POP_SIZE][G_LENGTH], double fitness[POP_SIZE])
{
  int p,i;

  /* 適応度の計算 前半の5bitは0の数 後半の5bitは1の数 */

  /*** この部分を自分で書く  ***/

}

/**********************************************************************
  遺伝子の表示 & 最大適応度・平均適応度の計算 & ファイルへの書き出し
    引数 t          : 世代数
         gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
         *fp        : ファイルポインタ
**********************************************************************/
void show_gene(int t, int gene[POP_SIZE][G_LENGTH], 
	       double fitness[POP_SIZE],
	       FILE *fp)
{
  int p,i;
  double avg_fit;  /* 平均適応度  */
  double max_fit;  /* 最大適応度  */
  
  /* 個体の値、適応度の表示 */

  /*** この部分を自分で書く  ***/

  
  /* 平均・最大適応度の計算 */

  /*** この部分を自分で書く  ***/


  /* 平均・最大適応度の表示 */
  printf("平均適応度 : %lf\n",avg_fit);
  printf("最大適応度 : %lf\n",max_fit);

  /* 平均・最大適応度をファイルに書き込む */
  fprintf(fp,"%d %lf %lf\n",t,avg_fit,max_fit);
}

/**********************************************************************
  個体番号 p1 と p2 の適応度と遺伝子を交換
    引数 p1, p2     : 遺伝子の番号
         gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
**********************************************************************/
void swap_gene(int p1, int p2, int gene[POP_SIZE][G_LENGTH], 
	       double fitness[POP_SIZE] )
{
  int tmp;
  double f;
  int i;
  
  /* 遺伝子型の交換 (遺伝子p1と遺伝子p2の値を入れ替える) */

  /*** この部分を自分で書く  ***/


  /* 適応度の交換 (遺伝子p1と遺伝子p2の適応度の値を入れ替える) */

  /*** この部分を自分で書く  ***/


}

/**********************************************************************
  個体番号 p1 の適応度と遺伝子型を p2 にコピー
    引数 p1, p2     : 遺伝子の番号
         gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
**********************************************************************/
void copy_gene(int p1, int p2, int gene[POP_SIZE][G_LENGTH], 
	       double fitness[POP_SIZE] )
{
  int i;
  
  /* 遺伝子のコピー (遺伝子p1を遺伝子p2にコピーする) */

  /*** この部分を自分で書く  ***/


  /* 適応度のコピー (遺伝子p1の適応度を遺伝子p2の適応度にコピーする)*/

  /*** この部分を自分で書く  ***/


}

/**********************************************************************
  エリート保存
   (最小適応度の個体に最大適応度の個体のデータをコピー)
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
**********************************************************************/
void elite(int gene[POP_SIZE][G_LENGTH], double fitness[POP_SIZE])
{
  int p,i;
  double max_fitness=fitness[0];
  double min_fitness=fitness[0];
  int max_p=0;
  int min_p=0;
  
  /* 最大適応度の個体(max_p)と最小適応度の個体(min_p)を見つける */
 
  /*** この部分を自分で書く  ***/



  /* 最小適応度の個体に最大適応度の個体をコピー */
  copy_gene(max_p,min_p,gene,fitness);
  /* 最大適応度の個体を0番目に移動 */
  swap_gene(0,max_p,gene,fitness);
}

/**********************************************************************
  ルーレット選択
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
         fitness[p] : 遺伝子pの適応度
**********************************************************************/
void reproduction(int gene[POP_SIZE][G_LENGTH], double fitness[POP_SIZE])
{
  double sum_of_fitness; /* 個体の適応度の総和 */
  double border;         /* ルーレット上の個体間の境界 */
  double r;              /* ルーレット上の選択位置 */
  int p,i;               /* 選ばれた個体の番号 */
  int num;               /* 0 <= num <= POP_SIZE-1 */
  int new_gene[POP_SIZE][G_LENGTH];
  
  /* ルーレットの1周分 sum_of_fitness を求める */
  sum_of_fitness = 0.0;
  for(p=0;p<POP_SIZE;p++){
    sum_of_fitness += fitness[p];
  }
  
  /* ルーレットを POP_SIZE 回だけ回して次世代の個体を選ぶ */
  for(p=1;p<POP_SIZE;p++){
    /* ルーレットを回して場所を選ぶ 
       r : 選ばれた位置 (0 <= r <= sum_of_fitness) */
    r=sum_of_fitness*Random();
    /* 選ばれた場所に該当する個体が何番か調べる
       num : 選ばれた個体の番号 (0 <= num <= POP_SIZE-1) */
    num=0;
    border = fitness[0]; /* 個体間の境界 */
    while(border<r){
      num++;
      border+=fitness[num];
    }
    
    /* 遺伝子の代入 */
    for(i=0;i<G_LENGTH;i++){
      new_gene[p][i]=gene[num][i];
    }
  }
  
  /* 遺伝子のコピー */
  for(p=1;p<POP_SIZE;p++){
    for(i=0;i<G_LENGTH;i++){
      gene[p][i]=new_gene[p][i];
    }
  }
}

/**********************************************************************
  一点交叉
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
**********************************************************************/
void crossover(int gene[POP_SIZE][G_LENGTH])
{
  int gene1[G_LENGTH]; /* 親1の遺伝子型 */ 
  int gene2[G_LENGTH]; /* 親2の遺伝子型 */ 
  int i,j;
  int c_pos;   /* 交叉位置 (1 <= c_pos <= G_LENGTH-1) */ 

  /* 交叉位置を1〜G_LENGTH-1の範囲でランダムに決め、
     それより後ろを入れ替える。
     gene[1]とgene[2],  gene[3]とgene[4] ... のように親にする */

  /*** この部分を自分で書く  ***/


}

/**********************************************************************
  二点交叉 (余裕があれば)
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
**********************************************************************/
void two_crossover(int gene[POP_SIZE][G_LENGTH])
{
  int gene1[G_LENGTH]; /* 親1の遺伝子型 */ 
  int gene2[G_LENGTH]; /* 親2の遺伝子型 */ 
  int p,i;
  int c_pos1, c_pos2;  /* 交叉位置 (1 <= c_pos1,2 <= G_LENGTH-1) */ 
  int tmp;
  
  /* 交叉位置を1〜G_LENGTH-1の範囲でランダムに2つ決め、その間を入れ替える。
     gene[1]とgene[2],  gene[3]とgene[4] ... のように親にする */

  /*** この部分を自分で書く  ***/

}

/**********************************************************************
  突然変異
    引数 gene[p][i] : 遺伝子pのi番目の成分				     
**********************************************************************/
void mutation(int gene[POP_SIZE][G_LENGTH])
{
  int p,i;
  
  /* 0〜1の乱数を発生させ、その値が M_RATE 以下ならば
     遺伝子の値をランダムに変える (0ならば1、1ならば0) */

  /*** この部分を自分で書く  ***/

}

/**********************************************************************
  メインプログラム
**********************************************************************/
int main(int argc, char *argv[])
{
  int gene[POP_SIZE][G_LENGTH];     
  double fitness[POP_SIZE];         
  int t;
  FILE *fp;

  /* 適応度の変化を記録するファイルのオープン */
  if((fp=fopen("result.dat","w"))==NULL){
    printf("Cannot open \"result.dat\"\n");
    exit(1);
  }
  
  /* シミュレーション条件の表示 */
  printf("個体数     : %d\n",POP_SIZE);
  printf("遺伝子長   : %d bit\n",G_LENGTH);
  printf("突然変異率 : %lf\n",M_RATE);
  
  
  init_gene(gene);              /* 遺伝子の初期化 */
  calc_fitness(gene,fitness);   /* 適応度の計算 */
  show_gene(0,gene,fitness,fp); /* 表示 */
  
  for(t=1;t<=MAX_GEN;t++){
    printf("<< 世代数 : %d >>\n",t);
    elite(gene,fitness);           /* エリート保存 */
    reproduction(gene,fitness);    /* ルーレット選択 */
    crossover(gene);               /* 単純交叉 */ 
    //two_crossover(gene);         /* 二点交叉 */ 
    mutation(gene);                /* 突然変異 */
    calc_fitness(gene,fitness);    /* 適応度の計算 */
    show_gene(t,gene,fitness,fp);  /* 表示 */
  }

  /* ファイルのクローズ */
  fclose(fp);

  return 0;
}

	





