import math
import sys

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

print(pd.__version__)
# 1.0.5

print(mpl.__version__)
# 3.3.0

print(sns.__version__)
# 0.10.1

print(sys.version)
# 3.8.5 (default, Jul 21 2020, 10:48:26) 
# [Clang 11.0.3 (clang-1103.0.32.62)]

df = pd.read_csv('data/130001_tokyo_covid19_patients_20200731.csv')

# df = pd.read_csv('https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv')

print(df.shape)
# (12691, 16)

print(df.head())
#    No  全国地方公共団体コード 都道府県名  市区町村名      公表_年月日 曜日  発症_年月日  患者_居住地 患者_年代 患者_性別  \
# 0   1       130001   東京都    NaN  2020-01-24  金     NaN  湖北省武漢市   40代    男性   
# 1   2       130001   東京都    NaN  2020-01-25  土     NaN  湖北省武漢市   30代    女性   
# 2   3       130001   東京都    NaN  2020-01-30  木     NaN  湖南省長沙市   30代    女性   
# 3   4       130001   東京都    NaN  2020-02-13  木     NaN      都内   70代    男性   
# 4   5       130001   東京都    NaN  2020-02-14  金     NaN      都内   50代    女性   
# 
#    患者_属性  患者_状態  患者_症状  患者_渡航歴の有無フラグ  備考  退院済フラグ  
# 0    NaN    NaN    NaN           NaN NaN     1.0  
# 1    NaN    NaN    NaN           NaN NaN     1.0  
# 2    NaN    NaN    NaN           NaN NaN     1.0  
# 3    NaN    NaN    NaN           NaN NaN     1.0  
# 4    NaN    NaN    NaN           NaN NaN     1.0  

print(df.tail())
#           No  全国地方公共団体コード 都道府県名  市区町村名      公表_年月日 曜日  発症_年月日 患者_居住地 患者_年代  \
# 12686  12532       130001   東京都    NaN  2020-07-31  金     NaN    NaN   70代   
# 12687  12558       130001   東京都    NaN  2020-07-31  金     NaN    NaN   70代   
# 12688  12563       130001   東京都    NaN  2020-07-31  金     NaN    NaN   70代   
# 12689  12144       130001   東京都    NaN  2020-07-31  金     NaN    NaN   80代   
# 12690  12517       130001   東京都    NaN  2020-07-31  金     NaN    NaN   80代   
# 
#       患者_性別  患者_属性  患者_状態  患者_症状  患者_渡航歴の有無フラグ  備考  退院済フラグ  
# 12686    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12687    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12688    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12689    女性    NaN    NaN    NaN           NaN NaN     NaN  
# 12690    男性    NaN    NaN    NaN           NaN NaN     NaN  

df
#           No  全国地方公共団体コード 都道府県名  市区町村名      公表_年月日 曜日  発症_年月日  患者_居住地 患者_年代  \
# 0          1       130001   東京都    NaN  2020-01-24  金     NaN  湖北省武漢市   40代   
# 1          2       130001   東京都    NaN  2020-01-25  土     NaN  湖北省武漢市   30代   
# 2          3       130001   東京都    NaN  2020-01-30  木     NaN  湖南省長沙市   30代   
# 3          4       130001   東京都    NaN  2020-02-13  木     NaN      都内   70代   
# 4          5       130001   東京都    NaN  2020-02-14  金     NaN      都内   50代   
# ...      ...          ...   ...    ...         ... ..     ...     ...   ...   
# 12686  12532       130001   東京都    NaN  2020-07-31  金     NaN     NaN   70代   
# 12687  12558       130001   東京都    NaN  2020-07-31  金     NaN     NaN   70代   
# 12688  12563       130001   東京都    NaN  2020-07-31  金     NaN     NaN   70代   
# 12689  12144       130001   東京都    NaN  2020-07-31  金     NaN     NaN   80代   
# 12690  12517       130001   東京都    NaN  2020-07-31  金     NaN     NaN   80代   
# 
#       患者_性別  患者_属性  患者_状態  患者_症状  患者_渡航歴の有無フラグ  備考  退院済フラグ  
# 0        男性    NaN    NaN    NaN           NaN NaN     1.0  
# 1        女性    NaN    NaN    NaN           NaN NaN     1.0  
# 2        女性    NaN    NaN    NaN           NaN NaN     1.0  
# 3        男性    NaN    NaN    NaN           NaN NaN     1.0  
# 4        女性    NaN    NaN    NaN           NaN NaN     1.0  
# ...     ...    ...    ...    ...           ...  ..     ...  
# 12686    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12687    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12688    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 12689    女性    NaN    NaN    NaN           NaN NaN     NaN  
# 12690    男性    NaN    NaN    NaN           NaN NaN     NaN  
# 
# [12691 rows x 16 columns]

print(df.count())
# No              12691
# 全国地方公共団体コード     12691
# 都道府県名           12691
# 市区町村名               0
# 公表_年月日          12691
# 曜日              12691
# 発症_年月日              0
# 患者_居住地          12228
# 患者_年代           12691
# 患者_性別           12691
# 患者_属性               0
# 患者_状態               0
# 患者_症状               0
# 患者_渡航歴の有無フラグ        0
# 備考                  0
# 退院済フラグ           7186
# dtype: int64

print(df.nunique())
# No              12691
# 全国地方公共団体コード         1
# 都道府県名               1
# 市区町村名               0
# 公表_年月日            164
# 曜日                  7
# 発症_年月日              0
# 患者_居住地              8
# 患者_年代              13
# 患者_性別               5
# 患者_属性               0
# 患者_状態               0
# 患者_症状               0
# 患者_渡航歴の有無フラグ        0
# 備考                  0
# 退院済フラグ              1
# dtype: int64

print(df['患者_居住地'].unique())
# ['湖北省武漢市' '湖南省長沙市' '都内' '都外' '―' '調査中' '－' "'-" nan]

print(df['患者_居住地'].value_counts(dropna=False))
# 都内        11271
# 都外          531
# NaN         463
# ―           336
# 調査中          85
# 湖北省武漢市        2
# 湖南省長沙市        1
# '-            1
# －             1
# Name: 患者_居住地, dtype: int64

print(df['患者_性別'].unique())
# ['男性' '女性' "'-" '―' '不明']

print(df['患者_性別'].value_counts())
# 男性    7550
# 女性    5132
# '-       7
# 不明       1
# ―        1
# Name: 患者_性別, dtype: int64

df = df[['公表_年月日', '患者_年代', '退院済フラグ']].copy()

df.rename(columns={'公表_年月日': 'date_str', '患者_年代': 'age_org', '退院済フラグ': 'discharged'},
          inplace=True)

print(df)
#          date_str age_org  discharged
# 0      2020-01-24     40代         1.0
# 1      2020-01-25     30代         1.0
# 2      2020-01-30     30代         1.0
# 3      2020-02-13     70代         1.0
# 4      2020-02-14     50代         1.0
# ...           ...     ...         ...
# 12686  2020-07-31     70代         NaN
# 12687  2020-07-31     70代         NaN
# 12688  2020-07-31     70代         NaN
# 12689  2020-07-31     80代         NaN
# 12690  2020-07-31     80代         NaN
# 
# [12691 rows x 3 columns]

print(df['age_org'].unique())
# ['40代' '30代' '70代' '50代' '60代' '80代' '20代' '10歳未満' '90代' '10代' '100歳以上'
#  '不明' "'-"]

print(df['age_org'].value_counts())
# 20代       4166
# 30代       2714
# 40代       1741
# 50代       1362
# 60代        832
# 70代        713
# 80代        455
# 10代        281
# 90代        214
# 10歳未満      200
# 不明           6
# 100歳以上       5
# '-           2
# Name: age_org, dtype: int64

df = df[~df['age_org'].isin(['不明', "'-"])]

print(df)
#          date_str age_org  discharged
# 0      2020-01-24     40代         1.0
# 1      2020-01-25     30代         1.0
# 2      2020-01-30     30代         1.0
# 3      2020-02-13     70代         1.0
# 4      2020-02-14     50代         1.0
# ...           ...     ...         ...
# 12686  2020-07-31     70代         NaN
# 12687  2020-07-31     70代         NaN
# 12688  2020-07-31     70代         NaN
# 12689  2020-07-31     80代         NaN
# 12690  2020-07-31     80代         NaN
# 
# [12683 rows x 3 columns]

print(df['age_org'].unique())
# ['40代' '30代' '70代' '50代' '60代' '80代' '20代' '10歳未満' '90代' '10代' '100歳以上']

df['age'] = (
    df['age_org'].replace(['10歳未満', '10代'], '0-19')
    .replace(['20代', '30代'], '20-39')
    .replace(['40代', '50代'], '40-59')
    .replace(['60代', '70代', '80代', '90代', '100歳以上'], '60-')
)

print(df['age'].unique())
# ['40-59' '20-39' '60-' '0-19']

print(df['age'].value_counts())
# 20-39    6880
# 40-59    3103
# 60-      2219
# 0-19      481
# Name: age, dtype: int64

df['date'] = pd.to_datetime(df['date_str'])

print(df.dtypes)
# date_str              object
# age_org               object
# discharged           float64
# age                   object
# date          datetime64[ns]
# dtype: object

df_ct = pd.crosstab(df['date'], df['age'])

print(df_ct)
# age         0-19  20-39  40-59  60-
# date                               
# 2020-01-24     0      0      1    0
# 2020-01-25     0      1      0    0
# 2020-01-30     0      1      0    0
# 2020-02-13     0      0      0    1
# 2020-02-14     0      0      1    1
# ...          ...    ...    ...  ...
# 2020-07-27     5     79     34   13
# 2020-07-28    13    168     65   20
# 2020-07-29     9    160     56   25
# 2020-07-30    11    236     83   37
# 2020-07-31    10    332     82   39
# 
# [164 rows x 4 columns]

print(type(df_ct.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

df_ct_week = df_ct.resample('W', label='left').sum()

print(df_ct_week)
# age         0-19  20-39  40-59  60-
# date                               
# 2020-01-19     0      1      1    0
# 2020-01-26     0      1      0    0
# 2020-02-02     0      0      0    0
# 2020-02-09     0      2      5    9
# 2020-02-16     0      1      3    6
# 2020-02-23     0      2      3    5
# 2020-03-01     2      5      9    9
# 2020-03-08     0      5     10   11
# 2020-03-15     0     10     27   12
# 2020-03-22     7    100     88  102
# 2020-03-29    16    244    198  148
# 2020-04-05    21    421    369  271
# 2020-04-12    30    350    375  280
# 2020-04-19    32    286    267  264
# 2020-04-26    29    216    165  260
# 2020-05-03     7    105     69  120
# 2020-05-10     2     46     16   46
# 2020-05-17     3     22     10   15
# 2020-05-24     4     43     16   21
# 2020-05-31     2     89     34   22
# 2020-06-07     5    113     17   26
# 2020-06-14     6    177     29   28
# 2020-06-21    10    236     65   23
# 2020-06-28    34    460    107   51
# 2020-07-05    79    824    191   68
# 2020-07-12    66   1006    295  117
# 2020-07-19    78   1140    414  171
# 2020-07-26    48    975    320  134

df_ct_week[:-1].plot.bar(stacked=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

plt.figure()
df_ct_week[:-1].plot.bar(stacked=True)
plt.savefig('image/bar_chart.png', bbox_inches='tight')
plt.close('all')

df_ct_week_str = df_ct_week.copy()
df_ct_week_str.index = df_ct_week_str.index.strftime('%Y-%m-%d')

df_ct_week_str[:-1].plot.bar(stacked=True, figsize=(8, 4))
# <AxesSubplot:xlabel='date'>
# <Figure size 576x288 with 1 Axes>

df_ct_week_str_norm = (df_ct_week_str.T / df_ct_week_str.sum(axis=1)).T

df_ct_week_str_norm.plot.bar(stacked=True, figsize=(8, 4))
# <AxesSubplot:xlabel='date'>
# <Figure size 576x288 with 1 Axes>

df_ct_week_str[:-1][['20-39', '60-']].plot.bar(figsize=(8, 4))
# <AxesSubplot:xlabel='date'>
# <Figure size 576x288 with 1 Axes>

df_week_ratio = df_ct_week / df_ct_week.shift()

print(df_week_ratio)
# age             0-19      20-39     40-59       60-
# date                                               
# 2020-01-19       NaN        NaN       NaN       NaN
# 2020-01-26       NaN   1.000000  0.000000       NaN
# 2020-02-02       NaN   0.000000       NaN       NaN
# 2020-02-09       NaN        inf       inf       inf
# 2020-02-16       NaN   0.500000  0.600000  0.666667
# 2020-02-23       NaN   2.000000  1.000000  0.833333
# 2020-03-01       inf   2.500000  3.000000  1.800000
# 2020-03-08  0.000000   1.000000  1.111111  1.222222
# 2020-03-15       NaN   2.000000  2.700000  1.090909
# 2020-03-22       inf  10.000000  3.259259  8.500000
# 2020-03-29  2.285714   2.440000  2.250000  1.450980
# 2020-04-05  1.312500   1.725410  1.863636  1.831081
# 2020-04-12  1.428571   0.831354  1.016260  1.033210
# 2020-04-19  1.066667   0.817143  0.712000  0.942857
# 2020-04-26  0.906250   0.755245  0.617978  0.984848
# 2020-05-03  0.241379   0.486111  0.418182  0.461538
# 2020-05-10  0.285714   0.438095  0.231884  0.383333
# 2020-05-17  1.500000   0.478261  0.625000  0.326087
# 2020-05-24  1.333333   1.954545  1.600000  1.400000
# 2020-05-31  0.500000   2.069767  2.125000  1.047619
# 2020-06-07  2.500000   1.269663  0.500000  1.181818
# 2020-06-14  1.200000   1.566372  1.705882  1.076923
# 2020-06-21  1.666667   1.333333  2.241379  0.821429
# 2020-06-28  3.400000   1.949153  1.646154  2.217391
# 2020-07-05  2.323529   1.791304  1.785047  1.333333
# 2020-07-12  0.835443   1.220874  1.544503  1.720588
# 2020-07-19  1.181818   1.133201  1.403390  1.461538
# 2020-07-26  0.615385   0.855263  0.772947  0.783626

df_week_ratio['2020-05-03':'2020-07-25'].plot(grid=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

df['age_detail'] = df['age_org'].replace(
    {'10歳未満': '0-9', '10代': '10-19', '20代': '20-29', '30代': '30-39', '40代': '40-49', '50代': '50-59',
     '60代': '60-69', '70代': '70-79', '80代': '80-89', '90代': '90-', '100歳以上': '90-'}
)

df_ct_hm = pd.crosstab(df['date_str'], df['age_detail']).T[::-1]

plt.figure(figsize=(15, 5))
sns.heatmap(df_ct_hm, cmap='hot')
# <AxesSubplot:xlabel='date_str', ylabel='age_detail'>
# <Figure size 1080x360 with 2 Axes>

df_ct_hm_re = df_ct_hm.replace({0: 0.1})

min_value = df_ct_hm_re.values.min()
max_value = df_ct_hm_re.values.max()

log_norm = mpl.colors.LogNorm(vmin=min_value, vmax=max_value)
cbar_ticks = [math.pow(10, i) for i in range(math.floor(math.log10(min_value)),
                                             1 + math.ceil(math.log10(max_value)))]

plt.figure(figsize=(15, 5))
sns.heatmap(df_ct_hm_re, norm=log_norm, cbar_kws={"ticks": cbar_ticks})
# /usr/local/lib/python3.8/site-packages/seaborn/matrix.py:301: MatplotlibDeprecationWarning: Passing parameters norm and vmin/vmax simultaneously is deprecated since 3.3 and will become an error two minor releases later. Please pass vmin/vmax directly to the norm when creating it.
#   mesh = ax.pcolormesh(self.plot_data, vmin=self.vmin, vmax=self.vmax,
# 
# <AxesSubplot:xlabel='date_str', ylabel='age_detail'>
# <Figure size 1080x360 with 2 Axes>

print(df['discharged'].unique())
# [ 1. nan]

df['discharged'] = df['discharged'].fillna(0).astype('int')

print(df['discharged'].unique())
# [1 0]

print(pd.crosstab(df['date'], df['discharged']).resample('W', label='left').sum()[:-1].plot.bar(stacked=True))
# AxesSubplot(0.125,0.125;0.775x0.755)
# 
# <Figure size 432x288 with 1 Axes>

df_dc = pd.crosstab(df['date'], [df['age'], df['discharged']]).resample('W', label='left').sum()

print(df_dc)
# age        0-19     20-39      40-59       60-     
# discharged    0   1     0    1     0    1    0    1
# date                                               
# 2020-01-19    0   0     0    1     0    1    0    0
# 2020-01-26    0   0     0    1     0    0    0    0
# 2020-02-02    0   0     0    0     0    0    0    0
# 2020-02-09    0   0     0    2     0    5    0    9
# 2020-02-16    0   0     0    1     0    3    0    6
# 2020-02-23    0   0     0    2     0    3    0    5
# 2020-03-01    0   2     0    5     0    9    0    9
# 2020-03-08    0   0     0    5     0   10    1   10
# 2020-03-15    0   0     0   10     0   27    0   12
# 2020-03-22    0   7     0  100     0   88    2  100
# 2020-03-29    0  16     1  243     4  194    9  139
# 2020-04-05    0  21     5  416     1  368   11  260
# 2020-04-12    1  29     0  350     6  369   10  270
# 2020-04-19    2  30     3  283     6  261   17  247
# 2020-04-26    1  28     8  208     4  161   33  227
# 2020-05-03    1   6     6   99     5   64   23   97
# 2020-05-10    0   2     7   39     3   13    8   38
# 2020-05-17    2   1    10   12     2    8    9    6
# 2020-05-24    3   1    18   25     8    8    5   16
# 2020-05-31    0   2    13   76     8   26    9   13
# 2020-06-07    1   4    17   96     7   10   12   14
# 2020-06-14    3   3    84   93    13   16   17   11
# 2020-06-21    4   6    75  161    18   47    8   15
# 2020-06-28    4  30    37  423    19   88   20   31
# 2020-07-05   44  35   211  613    92   99   46   22
# 2020-07-12   62   4   803  203   250   45  113    4
# 2020-07-19   78   0  1140    0   414    0  171    0
# 2020-07-26   48   0   975    0   320    0  134    0

df_dc
# age        0-19     20-39      40-59       60-     
# discharged    0   1     0    1     0    1    0    1
# date                                               
# 2020-01-19    0   0     0    1     0    1    0    0
# 2020-01-26    0   0     0    1     0    0    0    0
# 2020-02-02    0   0     0    0     0    0    0    0
# 2020-02-09    0   0     0    2     0    5    0    9
# 2020-02-16    0   0     0    1     0    3    0    6
# 2020-02-23    0   0     0    2     0    3    0    5
# 2020-03-01    0   2     0    5     0    9    0    9
# 2020-03-08    0   0     0    5     0   10    1   10
# 2020-03-15    0   0     0   10     0   27    0   12
# 2020-03-22    0   7     0  100     0   88    2  100
# 2020-03-29    0  16     1  243     4  194    9  139
# 2020-04-05    0  21     5  416     1  368   11  260
# 2020-04-12    1  29     0  350     6  369   10  270
# 2020-04-19    2  30     3  283     6  261   17  247
# 2020-04-26    1  28     8  208     4  161   33  227
# 2020-05-03    1   6     6   99     5   64   23   97
# 2020-05-10    0   2     7   39     3   13    8   38
# 2020-05-17    2   1    10   12     2    8    9    6
# 2020-05-24    3   1    18   25     8    8    5   16
# 2020-05-31    0   2    13   76     8   26    9   13
# 2020-06-07    1   4    17   96     7   10   12   14
# 2020-06-14    3   3    84   93    13   16   17   11
# 2020-06-21    4   6    75  161    18   47    8   15
# 2020-06-28    4  30    37  423    19   88   20   31
# 2020-07-05   44  35   211  613    92   99   46   22
# 2020-07-12   62   4   803  203   250   45  113    4
# 2020-07-19   78   0  1140    0   414    0  171    0
# 2020-07-26   48   0   975    0   320    0  134    0

df_dc[:-1]['20-39'].plot.bar(stacked=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

df_dc[:-1]['60-'].plot.bar(stacked=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

x_young = df_dc[9:-1]['20-39']
x_young_norm = (x_young.T / x_young.sum(axis=1)).T

print(x_young_norm)
# discharged         0         1
# date                          
# 2020-03-22  0.000000  1.000000
# 2020-03-29  0.004098  0.995902
# 2020-04-05  0.011876  0.988124
# 2020-04-12  0.000000  1.000000
# 2020-04-19  0.010490  0.989510
# 2020-04-26  0.037037  0.962963
# 2020-05-03  0.057143  0.942857
# 2020-05-10  0.152174  0.847826
# 2020-05-17  0.454545  0.545455
# 2020-05-24  0.418605  0.581395
# 2020-05-31  0.146067  0.853933
# 2020-06-07  0.150442  0.849558
# 2020-06-14  0.474576  0.525424
# 2020-06-21  0.317797  0.682203
# 2020-06-28  0.080435  0.919565
# 2020-07-05  0.256068  0.743932
# 2020-07-12  0.798211  0.201789
# 2020-07-19  1.000000  0.000000

x_young_norm.plot.bar(stacked=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

x_old = df_dc[9:-1]['60-']
x_old_norm = (x_old.T / x_old.sum(axis=1)).T

print(x_old_norm)
# discharged         0         1
# date                          
# 2020-03-22  0.019608  0.980392
# 2020-03-29  0.060811  0.939189
# 2020-04-05  0.040590  0.959410
# 2020-04-12  0.035714  0.964286
# 2020-04-19  0.064394  0.935606
# 2020-04-26  0.126923  0.873077
# 2020-05-03  0.191667  0.808333
# 2020-05-10  0.173913  0.826087
# 2020-05-17  0.600000  0.400000
# 2020-05-24  0.238095  0.761905
# 2020-05-31  0.409091  0.590909
# 2020-06-07  0.461538  0.538462
# 2020-06-14  0.607143  0.392857
# 2020-06-21  0.347826  0.652174
# 2020-06-28  0.392157  0.607843
# 2020-07-05  0.676471  0.323529
# 2020-07-12  0.965812  0.034188
# 2020-07-19  1.000000  0.000000

x_old_norm.plot.bar(stacked=True)
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

pd.DataFrame({'20-39': x_young_norm[0], '60-': x_old_norm[0]}).plot.bar()
# <AxesSubplot:xlabel='date'>
# <Figure size 432x288 with 1 Axes>

s_total = df['date'].value_counts().sort_index()

print(s_total)
# 2020-01-24      1
# 2020-01-25      1
# 2020-01-30      1
# 2020-02-13      1
# 2020-02-14      2
#              ... 
# 2020-07-27    131
# 2020-07-28    266
# 2020-07-29    250
# 2020-07-30    367
# 2020-07-31    463
# Name: date, Length: 164, dtype: int64

print(type(s_total))
# <class 'pandas.core.series.Series'>

print(type(s_total.index))
# <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

s_total.plot.bar()
# <AxesSubplot:>
# <Figure size 432x288 with 1 Axes>

s_total.plot()
# /usr/local/lib/python3.8/site-packages/pandas/plotting/_matplotlib/converter.py:256: MatplotlibDeprecationWarning: 
# The epoch2num function was deprecated in Matplotlib 3.3 and will be removed two minor releases later.
#   base = dates.epoch2num(dt.asi8 / 1.0e9)
# 
# <AxesSubplot:>
# <Figure size 432x288 with 1 Axes>

s_total_re = s_total.reindex(
    index=pd.date_range(s_total.index[0], s_total.index[-1]),
    fill_value=0
)

print(s_total_re)
# 2020-01-24      1
# 2020-01-25      1
# 2020-01-26      0
# 2020-01-27      0
# 2020-01-28      0
#              ... 
# 2020-07-27    131
# 2020-07-28    266
# 2020-07-29    250
# 2020-07-30    367
# 2020-07-31    463
# Freq: D, Name: date, Length: 190, dtype: int64

s_total_re.plot()
# <AxesSubplot:>
# <Figure size 432x288 with 1 Axes>

s_total_re.plot(logy=True)
# <AxesSubplot:>
# <Figure size 432x288 with 1 Axes>

s_total_re.plot.bar()
# <AxesSubplot:>
# <Figure size 432x288 with 1 Axes>

fig, ax = plt.subplots(figsize=(12, 4))

ax.xaxis.set_major_locator(mpl.dates.AutoDateLocator())
ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%Y-%m-%d'))

ax.xaxis.set_tick_params(rotation=90)

ax.bar(s_total.index, s_total)
# <BarContainer object of 164 artists>
# <Figure size 864x288 with 1 Axes>

fig, ax = plt.subplots(figsize=(12, 4))

ax.xaxis.set_major_locator(mpl.dates.AutoDateLocator())
ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%Y-%m-%d'))

ax.xaxis.set_tick_params(rotation=90)

ax.set_yscale('log')

ax.bar(s_total.index, s_total)
# <BarContainer object of 164 artists>
# <Figure size 864x288 with 1 Axes>

print(s_total.rolling(7).mean())
# 2020-01-24           NaN
# 2020-01-25           NaN
# 2020-01-30           NaN
# 2020-02-13           NaN
# 2020-02-14           NaN
#                  ...    
# 2020-07-27    252.285714
# 2020-07-28    256.428571
# 2020-07-29    258.142857
# 2020-07-30    258.285714
# 2020-07-31    287.285714
# Name: date, Length: 164, dtype: float64

fig, ax = plt.subplots(figsize=(12, 4))

ax.xaxis.set_major_locator(mpl.dates.AutoDateLocator())
ax.xaxis.set_minor_locator(mpl.dates.DayLocator())
ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%Y-%m-%d'))

ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

ax.grid(linestyle='--')
ax.margins(x=0)

ax.bar(s_total.index, s_total, width=1, color='#c0e0c0', edgecolor='black')
ax.plot(s_total.index, s_total.rolling(7).mean(), color='red')
# [<matplotlib.lines.Line2D at 0x11a3489a0>]
# <Figure size 864x288 with 1 Axes>
