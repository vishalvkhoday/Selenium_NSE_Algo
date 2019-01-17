
/*
select [Scrip Code],count(*) from ListOfScrips
group by [Scrip Code] */

--select * from ListOfScrips where [Scrip Id] like '%eq%'


select Industry,count(*)Occurance from (
select ae.Script_Name,round (sum(ae.Change),2)Chg,avg(ae.Volume)Vol,ls.Industry Industry from Actual_NSE_EOD ae inner join ListOfScrips ls on
ae.Script_Name = ls.[Scrip Id]
where Trnx_date > getdate() -100 and Volume > 400000
group by ae.Script_Name,ls.Industry
having sum(Change) < '0';
) as t1
group by Industry
order by 2 desc


select ae.Script_Name,round (sum(ae.Change),2)Chg,max(ae.[Close])High,min(low)Low,avg(ae.Volume)Vol,ls.Industry Industry from Actual_NSE_EOD ae inner join ListOfScrips ls on
ae.Script_Name = ls.[Scrip Id]
where Trnx_date > getdate() -200 and Volume > 400000
and ae.Pre_Close > 15
and ls.Industry ='Auto Parts &amp; Equipment'
group by ae.Script_Name,ls.Industry
--having sum(Change) < 0 



FEDERALBNK	-79.46	334.7	2013-10-17
FEDERALBNK	-50.98	153.8	2015-07-08


select * from Actual_NSE_EOD
where Script_Name ='JAMNAAUTO'
--and Trnx_date ='2017-09-28'
and Change < -10
order by Trnx_date desc


truncate table Temp_Actual_NSE_EOD


insert into Temp_Actual_NSE_EOD
select * from Actual_NSE_EOD where Script_Name='JAMNAAUTO'


select * from Temp_Actual_NSE_EOD
where Script_Name ='JAMNAAUTO'
and Trnx_date between '2015-11-03' and '2015-12-03'
--and Change < -10
order by Trnx_date


begin Tran T1

update Actual_NSE_EOD set Pre_Close = round((Pre_Close/2),2),[Open]= round(( [Open]/2),2),High=round((High/2),2),Low=round((Low/2),2),[Close]=round(([Close]/2),2)
where Script_Name = 'JAMNAAUTO' and Trnx_date < '2015-12-03'


update Actual_NSE_EOD set Pre_Close = round((Pre_Close/5),2),[Open]= round(( [Open]/5),2),High=round((High/5),2),Low=round((Low/5),2),[Close]=round(([Close]/5),2)
where Script_Name = 'JAMNAAUTO' and Trnx_date < '2017-10-05'

update Actual_NSE_EOD set Pre_Close = round((Pre_Close/2),2) where Script_Name ='JAMNAAUTO' and Trnx_date ='2015-12-03'
update Actual_NSE_EOD set Pre_Close = round((Pre_Close/5),2) where Script_Name ='JAMNAAUTO' and Trnx_date ='2017-10-05'

update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'JAMNAAUTO' 

commit

/*

select ls.Industry Ind,COUNT(*) Occurance ,sum(a1.Change) Chg,a1.Trnx_date Trnx_date from Actual_NSE_EOD a1 inner join ListOfScrips ls on
a1.Script_Name = ls.[Scrip Id]
where a1.Trnx_date > getdate() -100 and ls.Industry <>'Null'
group by ls.Industry,a1.Trnx_date
order by a1.Trnx_date desc,ls.Industry
*/



select * from (
select a1.Change Chg,a1.Trnx_date Trnx_date,ls.Industry Ind from Actual_NSE_EOD a1 inner join ListOfScrips ls on
a1.Script_Name = ls.[Scrip Id]
where a1.Trnx_date > getdate() -50 and ls.Industry <>'Null'

) as T1

pivot
(
sum (chg) for [Trnx_date] in (Banks,"Finance (including NBFCs)","Financial Institutions","Agrochemicals","Airlines","Aluminium","Asset Management Cos.","Auto Parts &amp; Equipment","Auto Tyres &amp; Rubber Products","Biotechnology","BPO/KPO")
--in ("2017-11-10","2017-11-13","2017-11-14","2017-11-15","2017-11-16","2017-11-17")
--in (Banks,"Finance (including NBFCs)","Financial Institutions","Agrochemicals","Airlines","Aluminium","Asset Management Cos.","Auto Parts &amp; Equipment","Auto Tyres &amp; Rubber Products","Biotechnology","BPO/KPO")

)as Pvt1

advace query for selecting all old records

select ane.Script_Name,min(ane.Low)Low,max(ane.high) High, round(sum(ane.Change),2)Chg from Actual_NSE_EOD ANE
where ane.Script_Name in(
select Script_Name from (
select Script_Name,count(*) as Occur from Actual_NSE_EOD Ane
where ane.Script_Name in (select Script_Name from Actual_NSE_EOD where Trnx_date = (select max(Trnx_date) from Actual_NSE_EOD)) and year(ane.Trnx_date) > '2015'
group by Script_Name
having count(*) > 500
) as T1
)
group by ane.Script_Name
having sum(ane.Change) > 0  and max(ane.high) < 300 and min(ane.low) > 30
order by ane.Script_Name





select a2.Script_Name,ls1.Industry,ls1.[Face Value],max(a2.High) High,min(a2.low) Low,avg(a2.Volume) Vol from Actual_NSE_EOD a2 inner join ListOfScrips ls1 on
a2.Script_Name = ls1.[Scrip Id]
and ls1.Industry in('Agrochemicals','Travel Support Services','Education')
where Trnx_date > getdate() -150
group by a2.Script_Name,ls1.Industry,ls1.[Face Value]
having avg(a2.Volume) > 10000
order by a2.Script_Name

select a2.Script_Name,ls1.Industry,ls1.[Face Value],max(a2.High) High,min(a2.low) Low,avg(a2.Volume) Vol,round((max(a2.High) - min(a2.Low))/max(a2.High)*100,2) Chg from Actual_NSE_EOD a2 inner join ListOfScrips ls1 on
a2.Script_Name = ls1.[Scrip Id]
and ls1.Industry in('Agrochemicals')
where Trnx_date > getdate() -150
group by a2.Script_Name,ls1.Industry,ls1.[Face Value]
having avg(a2.Volume) > 10000
order by a2.Script_Name


Get data based on company count

select ne.Script_Name,ls1.Industry,max(ne.High)High,min(ne.low)Low,sum(ne.Change)Chg_tot,avg(ne.Volume) Vol from NSE_EOD ne inner join ListOfScrips ls1
on ne.Script_Name=ls1.[Scrip Id]
where ls1.Industry in( 

select Industry from (
select ls.Industry,count(*)Items from ListOfScrips ls
group by ls.Industry
having count(*) between 5 and 9
) as T1
)
and ne.Trnx_date > getdate()-30 and ne.[Close] > 10
group by ne.Script_Name,ls1.Industry
having avg(ne.Volume) > 10000


--update BSE stock as per NSE stock


begin tran T3
update Bse_Results set Script_Name = nse.Script_Name from Bse_Results bse inner join Stock_Info nse on  bse.ISIN=nse.ISIN and Bse.Script_Name != nse.Script_Name 




select distinct Bse.*,nse.Sector,round(avg(ANE.[Close]),2)cls from Bse_Results  Bse inner join Stock_Info nse on
nse.ISIN=Bse.ISIN 
and  nse.Script_Name=Bse.Script_Name
inner join Actual_NSE_EOD ANE on
Bse.Script_Name = ANE.Script_Name
and datepart(q,Bse.[Quarter]) = datepart(q,ANE.Trnx_date)
and YEAR(bse.[Quarter]) = YEAR(Trnx_date)
where Bse.[quarter] is not null and Bse.EPS <>0
group by Bse.Script_Name,Bse.ISIN,Bse.[Quarter],Bse.CEPS,Bse.Depreciation,Bse.EPS,Bse.Equity,Bse.Expenditure,Bse.Interest,Bse.Net_Profit,Bse.NPM,Bse.OPM,
Bse.Other_Income,Bse.PBDT,Bse.PBT,Bse.Revenue,Bse.Tax,Bse.Total_Income,nse.Sector
order by Bse.Script_Name,bse.[Quarter]


