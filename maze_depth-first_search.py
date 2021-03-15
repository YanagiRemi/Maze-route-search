filename="map1010.txt"   #ファイル名指定
start_line=1             #スタートの行の位置
start_row=1              #スタートの列の位置
gole_line=9              #ゴールの行の位置
gole_row=9               #ゴールの列の位置

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

maze=[]      #迷路ファイルを2次元配列リストとするための空リストmaze作成

#課題1のプログラム部分
f=open(filename,"r")            #ファイルを開く
line=f.readline()               #最初の行を変数lineに代入
while line:
    line=line.replace('\n','')  #改行文字削除
    print(line)
    maze.append(list(line))     #lineの内容をリスト化したものをmazeに追加
    line=f.readline()           #次の行をlineに代入
f.close                         #ファイルを閉じる

OL=[(start_line,start_row)]     #スタート位置の座標が入ったオープンリスト作成　構造はスタック
CL=[]                           #空のクローズドリスト作成　

while True:                            #while文開始
    if (OL == []):  # もしオープンリストの中身が空であればwhile文を抜ける
        break
    st=OL.pop()                        #OLをpopして取り出した座標をstに代入
    CL.append(st)                      #クローズドリストにstの座標を追加
    if(st == (gole_line, gole_row)):   #stがゴールの座標であればwhile文を抜ける
        break
    else:
        B = next(st, CL, maze)         # 変数Bにnext関数の返り値代入
        for i in B:                    # リストBの中身を順にpushしてオープンリストに追加
            OL.append(i)
if(st!=(gole_line,gole_row)):                   #stの座標がゴールでなければ「ゴールにたどり着けなかった」と出力
    print("ゴールにはたどり着けなかった。")
for i in CL:                                    #クローズドリストの中身を順に出力
    print(i)
