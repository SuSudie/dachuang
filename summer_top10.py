import os
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from netCDF4 import Dataset

# 读入数据
# CMA
nc = Dataset(r'/data/zyzhang/conserve/CMA/CMAregionalregrid.nc','r')
prcpvar = nc.variables['data'][:][:]
prcpvar1 = prcpvar[:,24:42,90:107]
data = np.mean(np.mean(prcpvar1,2),1)
# 排序后存入CMA数组
ordered_CMA = [                                                  sorted(data[151:151+91]),sorted(data[516:516+91]),
        sorted(data[881:881+365]),sorted(data[1247:1247+91]),sorted(data[1612:1612+91]),sorted(data[1977:1977+91]),
        sorted(data[2342:2342+91]),sorted(data[2708:2708+91]),sorted(data[3073:3073+91]),sorted(data[3438:3438+91]),
        sorted(data[3803:3803+91]),sorted(data[4169:4169+91]),sorted(data[4534:4534+91]),sorted(data[4899:4899+91]),
        sorted(data[5264:5264+91]),sorted(data[5630:5630+91]),sorted(data[5995:5995+91]),sorted(data[6360:6360+91]),
        sorted(data[6725:6725+91]),sorted(data[7091:7091+91]),sorted(data[7456:7456+91]),sorted(data[7821:7821+91]),
        sorted(data[8186:8186+91]),sorted(data[8552:8552+91]),sorted(data[8917:8917+91]),sorted(data[9282:9282+91]),
        sorted(data[9647:9647+91]),sorted(data[10013:10013+91]),sorted(data[10378:10378+91]),sorted(data[10743:10743+91]),
        sorted(data[11108:11108+91]),sorted(data[11474:11474+91]),sorted(data[11839:11839+91]),sorted(data[12204:12204+91]),
        sorted(data[12569:12569+91]),sorted(data[12935:12935+91]),sorted(data[13300:13300+91]),sorted(data[13665:13665+91]),
        sorted(data[14030:14030+91]),sorted(data[14396:14396+91]),sorted(data[14761:15761+91]),sorted(data[15126:15126+91]),
        sorted(data[15491:15491+91]),sorted(data[15857:15857+91]),sorted(data[16222:16222+91]),sorted(data[16587:16587+91]),
        sorted(data[16952:16952+91])]

# 取出第top10%的数据
CMA_top10 = []
for i in range(len(ordered_CMA)):
    CMA_top10.append(ordered_CMA[i][-9])

x_axis_data = pd.date_range('19611231','20080101',freq='1y')
y_axis_data = CMA_top10
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='CMA')
plt.legend(fontsize=24,loc="upper left")

plt.tick_params(width=0.5,labelsize=28)
plt.xlabel('date(year)',fontdict={'weight':'normal','size':28})
plt.ylabel('precip(mm/day)',fontdict={'weight':'normal','size':28})
plt.title('East and South China Summer top 10% precipitation',fontdict={'weight':'normal','size':30})

# CMORPH_ordered
CMORPH_ordered = []
year = ['1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
        '2011','2012','2013','2014','2015','2016','2017','2018','2019']
path = '/data/zyzhang/conserve/cmorphmask'
for i in range(len(year)):
    FileName = 'CMORPHmask' + year[i] + 'regrid.nc'
    nc = Dataset(os.path.join(path,FileName))
    precip = nc.variables['precip'][:][:]
    precip_regional = precip[:,173:191,229:246]
    precip_average = np.mean(np.mean(precip_regional,2),1)
    year_int = int(year[i])
    if (year_int % 4) == 0 and (year_int % 100) != 0 or (year_int % 400) == 0:
        CMORPH_ordered.append(sorted(precip_average[152:152+91]))
    else:
        CMORPH_ordered.append(sorted(precip_average[151:151+91]))

CMORPH_top10 = []
for i in range(len(CMORPH_ordered)):
    CMORPH_top10.append(CMORPH_ordered[i][-9])

x_axis_data = pd.date_range('1998','2020',freq='1y')
y_axis_data = CMORPH_top10
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='CMORPH')
plt.legend(fontsize=24,loc="upper left")
plt.grid(b = True, linestyle='--', linewidth=1)

plt.show()