
insert into dbo.Trd_vol (Script_code, Company_name, Cur_Vol)
select SCRIP_CODE,CompanyName,NO_OF_SHRS from dbo.Bse_BhavCopy 
where trnx_Date ='04/01/2011'  

select * from Trd_Vol where update_trnx_date is null

update dbo.Trd_vol set pre_vol =  a.NO_OF_SHRS from dbo.Bse_BhavCopy a inner join dbo.Trd_vol b on
a.SCRIP_CODE = b.Script_code and a.CompanyName = b.Company_name
where a.trnx_date = '03/31/2011'  

update dbo.Trd_vol set update_trnx_date ='04/01/2011' where pre_vol is not null

update dbo.Trd_vol set Trd_dff = ((cur_vol - Pre_vol)*100 / Pre_vol) where Pre_vol is not null

insert into dbo.Actual_Trd_Vol (Script_code, Company_name, Pre_Vol, Cur_vol, Trd_dff, update_trnx_date)
select Script_code, Company_name, Pre_Vol, Cur_vol, Trd_dff, update_trnx_date from dbo.Trd_vol
where pre_vol is not null

select * from dbo.Actual_Trd_Vol where Pre_Vol is null

truncate table dbo.Trd_vol

select * from dbo.Actual_Trd_Vol where Pre_vol is not null order by script_code,update_trnx_date

select * from actual_trd_vol where update_trnx_Date = convert(varchar(10),getdate(),101) 
and pre_vol > 1000 
and trd_dff between 500 and 1000 order by trd_dff desc 

backup database stockquote to disk ='d:\DailyStock\stockQuote.bak'

Pivot


select * from (

select ane4.Script_Name as Script, ane4.Change as chg,Year(ane4.Trnx_date) as YRs, left(DATENAME(M,ane4.Trnx_date),3) as mon from Actual_NSE_EOD ane4
where ane4.Script_Name ='FDC'


) as S1
pivot
(
sum(chg) for [mon] in (JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC)

) as pvt 


************************************************************************************************************************************

select * from (

select year(ane1.Trnx_date) Yrs,'up' as side,ane1.Change as Occurance,left(datename (month ,ane1.Trnx_date),3) as mon from Actual_NSE_EOD ane1
where ane1.Change >=0 and ane1.Script_Name ='FDC'

) as S1
pivot
(
count(Occurance) for [mon] in (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
) as pvt1

union all


select * from (

select year(ane1.Trnx_date) Yrs,'Down' as side,ane1.Change as Occurance,left(datename (month ,ane1.Trnx_date),3) as mon from Actual_NSE_EOD ane1
where  ane1.Change <0 and ane1.Script_Name ='FDC'

) as S1
pivot
(
count(Occurance) for [mon] in (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
) as pvt1
order by 1,2;

************************************************************************************************************************************

select * from (
select ane.Script_Name,round(ane.Change,2) as chg,year(ane.Trnx_date) Yrs,left(datename(month,ane.Trnx_date),3)as mon
from Actual_NSE_EOD ane 
where  year(ane.Trnx_date) > '2010' and ane.Script_Name ='FDC'

) as S
pivot
(
sum(chg)
for [mon] IN (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
) as pvt;


select * from (

select ane1.Script_Name,ane1.Change as Occurance,MONTH(ane1.Trnx_date) as mon_no,left(datename (month ,ane1.Trnx_date),3) as mon,  year(ane1.Trnx_date) Yrs from Actual_NSE_EOD ane1
where ane1.Change >0 and ane1.Script_Name ='BHEL'

) as S1
pivot
(
--count(Occurance) for [Yrs] in ([2010])
sum(Occurance) for [Yrs] in ([2010],[2011],[2012],[2013],[2014],[2015],[2016],[2017])
) as pvt1
order by mon_no;


select * from (
select ane2.Script_Name,ane2.Change as chg,year(ane2.Trnx_date) as Yrs ,datename(WEEKDAY,ane2.Trnx_date) as WkDy from Actual_NSE_EOD ane2
where ane2.Script_Name='BHEL' and ane2.Change > =0
) s3
pivot
(
count(chg) for [WkDy] in (Monday,Tuesday,Wednesday,Thursday,Friday)

) as pvt3

select * from (
select ane2.Script_Name,ane2.Change as chg,year(ane2.Trnx_date) as Yrs ,datename(WEEKDAY,ane2.Trnx_date) as WkDy from Actual_NSE_EOD ane2
where ane2.Script_Name='BHEL' and ane2.Change > =0
) s3
pivot
(
sum(chg) for [WkDy] in (Monday,Tuesday,Wednesday,Thursday,Friday)

) as pvt3


select DATENAME(weekday,getdate()+3)