from matplotlib import pyplot

#基本再生産数（通常活動時の感染者一人当たりの新規感染者数）
R = 2.5
#自粛期間中の行動率（1が通常時）
activity = 0.2
#初期感染者数
x0 = 200
#隔離or回復までの日数
infection_days = 14
#計算上のタイムステップ
dt = 1/infection_days
#自粛開始日（この日以降行動率が1→activityになる）
stop_day = 30
#自粛を終了して通常の活動を再開する日
start_day = 150
#総シミュレーション日数
total_day = 180

#現在の感染者数
x = [x0]
#新規感染者数
new = [0]

#値の更新（差分法）
for day in range(1,total_day):
    p = 1
    if day >= stop_day:
        p = activity
    if day >= start_day:
        p = 1
    x.append(x[day-1]+x[day-1]*(R*p-1.0)*dt)
    new.append(x[day-1]*R*p*dt)

#グラフ表示
pyplot.plot(x,label='Infected persons')
pyplot.plot(new,label='New infected persons')
pyplot.xlabel('days')
pyplot.ylabel('Persons')
pyplot.legend()
pyplot.show()