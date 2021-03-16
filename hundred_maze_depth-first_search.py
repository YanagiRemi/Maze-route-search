from collections import deque   #collectionsモジュールのデキュー型をインポート
import numpy as np              #numpyをnpという名前でインポート
start_line=1                    #スタートの行の位置
start_row=1                     #スタートの列の位置
gole_line=99                    #ゴールの行の位置
gole_row=99                     #ゴールの列の位置

#課題2のプログラム部分
def next(a,b,C):
    A=[]                                                   #空リストA作成
    if (a[0]-1,a[1]) not in b and C[a[0]-1][a[1]]!='1':    #次に進めるか判定
        A.append((a[0]-1,a[1]))                            #リストAに追加
    if (a[0]+1, a[1]) not in b and C[a[0]+1][a[1]]!= '1':
        A.append((a[0]+1, a[1]))
    if (a[0], a[1]-1) not in b and C[a[0]][a[1]-1]!= '1':
        A.append((a[0], a[1]-1))
    if (a[0], a[1]+1) not in b and C[a[0]][a[1]+1]!= '1':
        A.append((a[0], a[1]+1))
    return A                                               #リストAを返す

memory=[]        #メモリ量のリストmemoryを作成
calc=[]          #計算量のリストcalcを作成
k=0              #ファイルの番号を格納する変数k作成 0で初期化

while k < 100:   #while文開始 kが100よりも小さい間繰り返す
    X=0          #現在のOLが保存してる座標情報のサイズを格納する変数X作成 0で初期化
    count=0      #next関数が呼び出される回数を格納する変数count作成 0で初期化
    maze=[]      #迷路ファイルを2次元配列リストとするための空リストmaze作成

    f = open('8059/map%d'% k,'r')       #ファイルを開く
    line = f.readline()                 #最初の行を変数lineに代入
    while line:
        line = line.replace('\n', '')   #改行文字削除
        maze.append(list(line))         #lineの内容をリスト化したものをmazeに追加
        line = f.readline()             #次の行をlineに代入
    f.close                             #ファイルを閉じる

    OL = [(start_line, start_row)]    #スタート位置の座標が入ったオープンリスト作成　構造はスタック
    CL = []                           #空のクローズドリスト作成　

    while True:                               #while文開始
        if (X < len(OL)):                     #変数XよりOLの要素数が大きければXにOLの要素数を代入
            X = len(OL)
        if (OL == []):  # もしオープンリストの中身が空であればwhile文を抜ける
            break
        st = OL.pop()                         #OLをpopして取り出した座標をstに代入
        CL.append(st)                         #クローズドリストにstの座標を追加
        if (st == (gole_line, gole_row)):     #stがゴールの座標であればwhile文を抜ける
            break
        else:
            B = next(st, CL, maze)            # 変数Bにnext関数の返り値代入
            count += 1                        #変数countの値に1を足す
            for i in B:                       #リストBの中身を順にpushしてオープンリストに追加
                OL.append(i)
    calc.append(count)                        #countの値をリストcalcに追加
    memory.append(X)                          #Xの値をリストmemoryに追加
    k+=1                                      #kの値に1を足す
calc=np.array(calc)                           #リストcalcを配列化
memory=np.array(memory)                       #リストmemoryを配列化
print('計算量の平均:''{:.2f}'.format(np.mean(calc)))          #計算量の平均値表示
print('計算量の分散:''{:.2f}'.format(np.var(calc)))           #計算量の分散表示
print('最悪計算量:''{:.2f}'.format(np.max(calc)))             #最悪計算量の表示
print('最良計算量:''{:.2f}'.format(np.min(calc)))             #最良計算量の表示
print('メモリ量の平均:''{:.2f}'.format(np.mean(memory)))      #メモリ量の平均値表示
print('メモリ量の分散:''{:.2f}'.format(np.var(memory)))       #メモリ量の分散表示
print('最悪メモリ量:''{:.2f}'.format(np.max(memory)))         #最悪メモリ量の表示
print('最良メモリ量:''{:.2f}'.format(np.min(memory)))         #最良メモリ量の表示