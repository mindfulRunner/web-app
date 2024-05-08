import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db import DB

conn = sqlite3.connect(DB.GHG_DB)

sql = f'SELECT * FROM {DB.GHG_MAIN_TABLE}'

df = pd.read_sql(sql, conn)

# Pandas: sum up multiple columns into one column 
#   https://stackoverflow.com/questions/42063716/pandas-sum-up-multiple-columns-into-one-column-without-last-column
# column_names = ['Apples', 'Bananas', 'Grapes', 'Kiwis']
# df['Fruit Total']= df[column_names].sum(axis=1)

# F2010Q1, F2010Q2, F2010Q3, F2013Q4
# ...
# F2022Q1, F2022Q2, F2022Q3, F2022Q4
year_totals = list()
for year in range(2010, 2022 + 1):
    year_total = f'{year}_total'
    year_totals.append(year_total)
    year_column_names = []
    for quarter in range(1, 4 + 1):
        year_column_names.append(f'F{year}Q{quarter}')
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html
        df[year_total] = df[year_column_names].sum(axis=1)
    # print(year_column_names)

carbon_dioxide = df[df['Gas_Type'] == 'Carbon dioxide']
# print(carbon_dioxide)

carbon_dioxide_country_group = carbon_dioxide.groupby('Country')
# carbon_dioxide_by_country = carbon_dioxide_country_group.sum()
year_sums = dict()
for year_total in year_totals:
    # country_group[year_total + '_sum'] = country_group[year_total].sum()
    # column_sum = f'{year_total}: "sum"'
    year_sums[year_total] = 'sum'
# print('year_sums:', year_sums)
carbon_dioxide_by_country = carbon_dioxide_country_group.agg(
    year_sums
)
print(carbon_dioxide_by_country)

#                                       2010_total     2011_total  ...     2021_total     2022_total
# Country                                                          ...
# Advanced Economies                  51628.065591    50858.00047  ...   42482.259086   42947.828751
# Africa                               4995.446748    4988.004351  ...    5902.862687    5939.372845
# Americas                            32722.496848   32470.022971  ...   29875.975556   30455.556163
# Asia                                69287.312108   74114.660924  ...    89129.88824   90353.344543
# Australia and New Zealand            1837.304544    1830.598696  ...    1755.681561    1770.667313
# Central Asia                         1804.303625    1800.350947  ...    2062.186276    2135.624787
# Eastern Asia                        45763.377276   49487.787968  ...   57397.386495   57243.745701
# Eastern Europe                      10801.389824   11098.031695  ...   10624.920432   10294.166618
# Emerging and Developing Economies   82951.187868   88044.935935  ...   106288.79749  107400.025315
# Europe                              25679.207928   25441.923586  ...   22044.945256    21766.00454
# G20                                113482.177127   117321.59437  ...  123837.145089  125299.452216
# G7                                  39791.958082   39073.985438  ...   34287.836175   34766.687908
# Latin America and the Caribbean      7074.128172    7356.938194  ...    6986.022052    7132.767414
# Northern Africa                      1999.227857     1984.50793  ...    2547.453953    2601.901304
# Northern America                    25648.368678   25113.084776  ...   22889.953504   23322.788751
# Northern Europe                       3775.46749    3577.977658  ...    2848.133534    2891.163668
# Oceania                              1894.789825    1888.324577  ...    1817.384838    1833.575976
# Other Oceania sub-regions              57.485281      57.725881  ...      61.703277      62.908663
# South-eastern Asia                   4955.757324    5234.779841  ...    7230.783144    7651.928141
# Southern Asia                       10389.179932   10911.052584  ...   14438.691422    15087.89232
# Southern Europe                      4127.555892     4102.65977  ...    3013.328473    3065.160621
# Sub-Saharan Africa                   2996.218892    3003.496421  ...    3355.408733    3337.471541
# Western Asia                         6374.693949    6680.689583  ...    8000.840904    8234.153594
# Western Europe                       6974.794722    6663.254463  ...    5558.562817    5515.513633
# World                              134579.253458  138902.936408  ...  148771.056578  150347.854067

# Due to groupby('Country) above, `Country` became index (not column anymore),
# therefore, carbon_dioxide_by_country['Country'] does NOT work anymore

# carbon_dioxide_by_economy = carbon_dioxide_by_country[carbon_dioxide_by_country.loc['Advanced Economies']]
# carbon_dioxide_by_economy = carbon_dioxide_by_country[carbon_dioxide_by_country.index == 'Advanced Economies' or carbon_dioxide_by_country.index == 'Emerging and Developing Economies']
# carbon_dioxide_by_economy = carbon_dioxide_by_country.loc['Advanced Economies', 'Emerging and Developing Economies']
#
# all above are not working
# need to use df.loc[['index1', 'index3', 'index7', 'other index']]
# https://note.nkmk.me/en/python-pandas-at-iat-loc-iloc/
carbon_dioxide_by_economy = carbon_dioxide_by_country.loc[['Advanced Economies', 'Emerging and Developing Economies']]
print('carbon_dioxide_by_country.columns: ===========')
print(carbon_dioxide_by_country.columns)
print('carbon_dioxide_by_country.index: ===========')
print(carbon_dioxide_by_country.index)
# carbon_dioxide_by_economy = carbon_dioxide_by_country[carbon_dioxide_by_country['Country'] == 'Advanced Economies']
print('carbon_dioxide_by_economy: ============\n', carbon_dioxide_by_economy)

img_dir = 'static/img'

# sns_plot = sns.barplot(carbon_dioxide_by_country, x='Country', y='2010_total', estimator='sum')

# sns_plot.figure.savefig(f'{img_dir}/carbon_dioxide_emission_by_country.png')


# sns_plot = sns.barplot(carbon_dioxide_by_economy, x='Country', y='2010_total', estimator='sum')

# sns_plot.figure.savefig(f'{img_dir}/carbon_dioxide_emission_by_economy.png')

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html
# carbon_dioxide_economy = carbon_dioxide.filter(axis=1, items = ['Advanced Economies', 'Emerging and Developing Economies'])
# print('carbon_dioxide_economy: ======\n', carbon_dioxide_economy)

# subplot parameters: nrows, ncols, index
plt.subplot(211)
plt.plot(carbon_dioxide_by_economy.loc['Advanced Economies'])
plt.title("Carbon Dioxide Emission by Advanced Economies")
plt.xlabel("Year")
plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(212)
plt.plot(carbon_dioxide_by_economy.loc['Emerging and Developing Economies'])
plt.title("Carbon Dioxide Emission by Emerging and Developing Economies")
plt.xlabel("Year")
plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.savefig(f"{img_dir}/carbon_dioxide_emission_trend_by_economy")

plt.close() # must close plt before drawing next graph - otherwise the next graph will have overlap of current graph

plt.subplot(321)
plt.plot(carbon_dioxide_by_country.loc['Africa'])
plt.title("By Africa")
plt.xlabel("Year")
# plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(322)
plt.plot(carbon_dioxide_by_country.loc['Asia'])
plt.title("By Asia")
plt.xlabel("Year")
# plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(323)
plt.plot(carbon_dioxide_by_country.loc['Europe'])
plt.title("By Europe")
plt.xlabel("Year")
plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(324)
plt.plot(carbon_dioxide_by_country.loc['Northern America'])
plt.title("By North America")
plt.xlabel("Year")
# plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(325)
plt.plot(carbon_dioxide_by_country.loc['Latin America and the Caribbean'])
plt.title("By Latin America")
plt.xlabel("Year")
# plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.subplot(326)
plt.plot(carbon_dioxide_by_country.loc['Oceania'])
plt.title("By Oceania")
plt.xlabel("Year")
# plt.ylabel("Carbon Dioxide Emission")
plt.xticks(rotation=45)

plt.savefig(f"{img_dir}/carbon_dioxide_emission_trend_by_region")

# plt.show()
