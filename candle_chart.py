import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import pandas as pd
import plotly.graph_objects as go

from mpl_finance import candlestick2_ohlc

def chart(df)
    ## DB에서 데이터 호출
    df = select('SELECT 날짜, 종가 , 시가, 고가, 저가, 거래량, 변동, 종목명, currid FROM DB.TABLE')
    
    ## chart 에 한글표현이 안되어 추가
    path = 'C:/Users/moonki/vue_project/backend/fastapi/nanum-myeongjo/NanumMyeongjoBold.ttf'
    fontprop = fm.FontProperties(fname=path)
    
    # chart size 지정
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot(111)
    
    # 매달 01일에만 index를 생성해서 01일만 찍어줌.
    day_list = []
    name_list = []
    for i, day in enumerate(sub_df.날짜):
        #if day.isoweekday() == 1: ## 월요일만 찍어줌.
        if day.strftime('%d') == '01':
            day_list.append(i)
            name_list.append(day.strftime('%m/%d') + '\n(Mon)')
    
    ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))
    
    ## chat title tjfwjd
    ax.set_title(sub_df.loc[0, '종목명'], fontsize=22, fontproperties=fontprop)
    ## xlabel 설정
    ax.set_xlabel('Date', fontproperties=fontprop)
    ## y라벨 설정
    ax.set_ylabel('Dollar', fontproperties=fontprop)
    
    ## candlestick 을 그려줌
    candlestick2_ohlc(ax, df['시가'], df['고가'],
                      df['저가'], df['종가'],
                      width=0.8, colorup='r', colordown='b')
    ax.legend()
    plt.grid()
    ## chart 이미지 저장
    plt.savefig("C:/chart.png", transparent = True, pad_inches = 0)
