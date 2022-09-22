from datetime import datetime, timedelta
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np
import pandas as pd

#CMA()
nc = Dataset(r'/data/zyzhang/conserve/CMA/CMAregionalregrid.nc','r')
prcpvar = nc.variables['data'][:][:]
prcpvar1 = prcpvar[:,24:42,90:107]
data = np.mean(np.mean(prcpvar1,2),1)
data = [                                                  np.mean(data[151:151+91]),np.mean(data[516:516+91]),
        np.mean(data[881:881+365]),np.mean(data[1247:1247+91]),np.mean(data[1612:1612+91]),np.mean(data[1977:1977+91]),
        np.mean(data[2342:2342+91]),np.mean(data[2708:2708+91]),np.mean(data[3073:3073+91]),np.mean(data[3438:3438+91]),
        np.mean(data[3803:3803+91]),np.mean(data[4169:4169+91]),np.mean(data[4534:4534+91]),np.mean(data[4899:4899+91]),
        np.mean(data[5264:5264+91]),np.mean(data[5630:5630+91]),np.mean(data[5995:5995+91]),np.mean(data[6360:6360+91]),
        np.mean(data[6725:6725+91]),np.mean(data[7091:7091+91]),np.mean(data[7456:7456+91]),np.mean(data[7821:7821+91]),
        np.mean(data[8186:8186+91]),np.mean(data[8552:8552+91]),np.mean(data[8917:8917+91]),np.mean(data[9282:9282+91]),
        np.mean(data[9647:9647+91]),np.mean(data[10013:10013+91]),np.mean(data[10378:10378+91]),np.mean(data[10743:10743+91]),
        np.mean(data[11108:11108+91]),np.mean(data[11474:11474+91]),np.mean(data[11839:11839+91]),np.mean(data[12204:12204+91]),
        np.mean(data[12569:12569+91]),np.mean(data[12935:12935+91]),np.mean(data[13300:13300+91]),np.mean(data[13665:13665+91]),
        np.mean(data[14030:14030+91]),np.mean(data[14396:14396+91]),np.mean(data[14761:15761+91]),np.mean(data[15126:15126+91]),
        np.mean(data[15491:15491+91]),np.mean(data[15857:15857+91]),np.mean(data[16222:16222+91]),np.mean(data[16587:16587+91]),
        np.mean(data[16952:16952+91])]

plt.figure(figsize=(24,8),dpi=90)
x_axis_data = pd.date_range('19611231','20080101',freq='1y')
y_axis_data = data
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='CMA')
plt.legend(fontsize=24,loc="upper left")

plt.tick_params(width=0.5,labelsize=28)
plt.xlabel('date(year)',fontdict={'weight':'normal','size':28})
plt.ylabel('precip(mm/day)',fontdict={'weight':'normal','size':28})
plt.title('114.75~122.75E 26.75~35.25N summer precipitation',fontdict={'weight':'normal','size':40})

#GPCP()
nc = Dataset(r'/data/zyzhang/conserve/GPCP/GPCPmaskregrid.nc','r')
prcpvar = nc.variables['precip'][:][:]
prcpvar1 = prcpvar[:,233:250,229:246]
data = np.mean(np.mean(prcpvar1,2),1)
data1 = [np.mean(data[5:8]),np.mean(data[17:30]),np.mean(data[29:32]),np.mean(data[41:44]),np.mean(data[53:56]),np.mean(data[65:68]),
       np.mean(data[77:80]),np.mean(data[89:92]),np.mean(data[101:104]),np.mean(data[113:116]),np.mean(data[125:128]),np.mean(data[137:140]),
       np.mean(data[149:152]),np.mean(data[161:164]),np.mean(data[173:176]),np.mean(data[185:188]),np.mean(data[197:200]),np.mean(data[209:212]),
       np.mean(data[221:224]),np.mean(data[233:236]),np.mean(data[245:248]),np.mean(data[257:260]),np.mean(data[269:272]),np.mean(data[281:284]),
       np.mean(data[293:296]),np.mean(data[305:308]),np.mean(data[317:320]),np.mean(data[329:332]),np.mean(data[341:344]),np.mean(data[353:356]),
       np.mean(data[365:368]),np.mean(data[377:380]),np.mean(data[389:392]),np.mean(data[401:404]),np.mean(data[413:416]),np.mean(data[425:428]),
       np.mean(data[437:440])]

x_axis_data = pd.date_range('1979','2016',freq='1y')
y_axis_data = data1
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='GPCP')
plt.legend(fontsize=24,loc="upper left")

#CMORPH()

nc1998 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask1998regrid.nc','r')
prcpvar = nc1998.variables['precip'][:][:]
prcpvar1998 = prcpvar[:,173:191,229:246]
data1998 = np.mean(np.mean(prcpvar1998,2),1)

nc1999 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask1999regrid.nc','r')
prcpvar = nc1999.variables['precip'][:][:]
prcpvar1999 = prcpvar[:,173:191,229:246]
data1999 = np.mean(np.mean(prcpvar1999,2),1)

nc2000 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2000regrid.nc','r')
prcpvar = nc2000.variables['precip'][:][:]
prcpvar2000 = prcpvar[:,173:191,229:246]
data2000 = np.mean(np.mean(prcpvar2000,2),1)

nc2001 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2001regrid.nc','r')
prcpvar = nc2001.variables['precip'][:][:]
prcpvar2001 = prcpvar[:,173:191,229:246]
data2001 = np.mean(np.mean(prcpvar2001,2),1)

nc2002 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2002regrid.nc','r')
prcpvar = nc2002.variables['precip'][:][:]
prcpvar2002 = prcpvar[:,173:191,229:246]
data2002 = np.mean(np.mean(prcpvar2002,2),1)

nc2003 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2003regrid.nc','r')
prcpvar = nc2003.variables['precip'][:][:]
prcpvar2003 = prcpvar[:,173:191,229:246]
data2003 = np.mean(np.mean(prcpvar2003,2),1)

nc2004 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2004regrid.nc','r')
prcpvar = nc2004.variables['precip'][:][:]
prcpvar2004 = prcpvar[:,173:191,229:246]
data2004 = np.mean(np.mean(prcpvar2004,2),1)

nc2005 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2005regrid.nc','r')
prcpvar = nc2005.variables['precip'][:][:]
prcpvar2005 = prcpvar[:,173:191,229:246]
data2005 = np.mean(np.mean(prcpvar2005,2),1)

nc2006 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2006regrid.nc','r')
prcpvar = nc2006.variables['precip'][:][:]
prcpvar2006 = prcpvar[:,173:191,229:246]
data2006 = np.mean(np.mean(prcpvar2006,2),1)

nc2007 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2007regrid.nc','r')
prcpvar = nc2007.variables['precip'][:][:]
prcpvar2007 = prcpvar[:,173:191,229:246]
data2007 = np.mean(np.mean(prcpvar2007,2),1)

nc2008 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2008regrid.nc','r')
prcpvar = nc2008.variables['precip'][:][:]
prcpvar2008 = prcpvar[:,173:191,229:246]
data2008 = np.mean(np.mean(prcpvar2008,2),1)

nc2009 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2009regrid.nc','r')
prcpvar = nc2009.variables['precip'][:][:]
prcpvar2009 = prcpvar[:,173:191,229:246]
data2009 = np.mean(np.mean(prcpvar2009,2),1)

nc2010 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2010regrid.nc','r')
prcpvar = nc2010.variables['precip'][:][:]
prcpvar2010 = prcpvar[:,173:191,229:246]
data2010 = np.mean(np.mean(prcpvar2010,2),1)

nc2011 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2011regrid.nc','r')
prcpvar = nc2011.variables['precip'][:][:]
prcpvar2011 = prcpvar[:,173:191,229:246]
data2011 = np.mean(np.mean(prcpvar2011,2),1)

nc2012 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2012regrid.nc','r')
prcpvar = nc2012.variables['precip'][:][:]
prcpvar2012 = prcpvar[:,173:191,229:246]
data2012 = np.mean(np.mean(prcpvar2012,2),1)

nc2013 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2013regrid.nc','r')
prcpvar = nc2013.variables['precip'][:][:]
prcpvar2013 = prcpvar[:,173:191,229:246]
data2013 = np.mean(np.mean(prcpvar2013,2),1)

nc2014 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2014regrid.nc','r')
prcpvar = nc2014.variables['precip'][:][:]
prcpvar2014 = prcpvar[:,173:191,229:246]
data2014 = np.mean(np.mean(prcpvar2014,2),1)

nc2015 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2015regrid.nc','r')
prcpvar = nc2015.variables['precip'][:][:]
prcpvar2015 = prcpvar[:,173:191,229:246]
data2015 = np.mean(np.mean(prcpvar2015,2),1)

nc2016 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2016regrid.nc','r')
prcpvar = nc2016.variables['precip'][:][:]
prcpvar2016 = prcpvar[:,173:191,229:246]
data2016 = np.mean(np.mean(prcpvar2016,2),1)

nc2017 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2017regrid.nc','r')
prcpvar = nc2017.variables['precip'][:][:]
prcpvar2017 = prcpvar[:,173:191,229:246]
data2017 = np.mean(np.mean(prcpvar2017,2),1)

nc2018 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2018regrid.nc','r')
prcpvar = nc2018.variables['precip'][:][:]
prcpvar2018 = prcpvar[:,173:191,229:246]
data2018 = np.mean(np.mean(prcpvar2018,2),1)

nc2019 = Dataset(r'/data/zyzhang/conserve/cmorphmask/CMORPHmask2019regrid.nc','r')
prcpvar = nc2019.variables['precip'][:][:]
prcpvar2019 = prcpvar[:,173:191,229:246]
data2019 = np.mean(np.mean(prcpvar2019,2),1)

data = [np.mean(data1998[151:151+91]),np.mean(data1999[151:151+91]),
        np.mean(data2000[152:152+91]),np.mean(data2001[151:151+91]),
        np.mean(data2002[151:151+91]),np.mean(data2003[151:151+91]),
        np.mean(data2004[152:152+91]),np.mean(data2005[151:151+91]),
        np.mean(data2006[151:151+91]),np.mean(data2007[151:151+91]),
        np.mean(data2008[152:152+91]),np.mean(data2009[151:151+91]),
        np.mean(data2010[151:151+91]),np.mean(data2011[151:151+91]),
        np.mean(data2012[152:152+91]),np.mean(data2013[151:151+91]),
        np.mean(data2014[151:151+91]),np.mean(data2015[151:151+91]),
        np.mean(data2016[152:152+91]),np.mean(data2017[151:151+91]),
        np.mean(data2018[151:151+91]),np.mean(data2019[151:151+91])]


x_axis_data = pd.date_range('1998','2020',freq='1y')
y_axis_data = data
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='CMORPH')
plt.legend(fontsize=24,loc="upper left")

#GHCN()
nc = Dataset(r'/data/zyzhang/conserve/GHCN/GHCNbbregrid.nc','r')
prcpvar = nc.variables['data'][:][:]
prcpvar1 = prcpvar[:,233:250,229:246]
data1 = np.mean(np.mean(prcpvar1,2),1)
data =[]
for i in range(59):
    data.append(np.sum(data1[605+i*12:608+i*12])*10/91)

x_axis_data = pd.date_range('1950','2009',freq='1y')
y_axis_data = data
plt.plot(x_axis_data, y_axis_data, alpha=0.8, linewidth=3, label='GHCN')
plt.legend(fontsize=24,loc="upper left")


plt.show()  