
select Script_code, Company_name, Pre_Vol, Cur_vol, Trd_dff[Trd_dff in %], update_trnx_date from dbo.Actual_Trd_Vol 
where update_trnx_date = CONVERT(varchar(10),getdate(),101)
and Pre_Vol > 10000
and Trd_dff between 200 and 1000
order by Trd_dff desc


select * from Actual_Trd_Vol where Script_code in (523405,514304,500459)
order by Script_code,update_trnx_date

select * from Actual_Trd_Vol where Script_code in (select SCRIP_CODE from Bse_BhavCopy where SC_GROUP='A')
and update_trnx_date = CONVERT(varchar(10),getdate(),101)
and Pre_Vol > 10000
and Trd_dff between 200 and 1000
order by Trd_dff desc

select * from Actual_Trd_Vol where Script_code in (select distinct(SCRIP_CODE) from Bse_BhavCopy where SC_GROUP='A')
and update_trnx_date = CONVERT(varchar(10),getdate(),101)
and Trd_dff < 0
order by Trd_dff 


select nn.Script_code,SUM(nn.Trd_dff)SUM_Vol from (select Script_code,trd_dff from Actual_Trd_Vol) nn
group by nn.Script_code
order by nn.Script_code
select * from Actual_Trd_Vol where Trd_dff = '-99'
select MIN(Trd_dff) from Actual_Trd_Vol


select distinct top 5 update_trnx_date from Actual_Trd_Vol

delete from Actual_Trd_Vol where update_trnx_date is null

dbcc shrinkdatabase(stockquote,2,TRUNCATEONLY)

DBCC CHECKCATALOG (stockquote);
DBCC shrinkfile (StockQuote_log, 1 );
dbcc shrinkdatabase(stockQuote,truncateonly)


DECLARE @LogFileName varchar(100)

SELECT rtrim(name)

FROM dbo.sysfiles

WHERE Name like '%_log%'

 

DBCC SHRINKdatabase(StockQuote, TRUNCATEONLY)

select distinct(convert(varchar(10),Trnx_DATE,101)) nn from Bse_BhavCopy where YEAR(trnx_date)='2011' order by nn desc

select * from sys.database_files

GO


select * from Bse_BhavCopy where Trnx_DATE = (select max (trnx_Date)from Bse_BhavCopy)

-- This query will get max of trnx_date for each script to identify if the script has been renamed or stopped trading.
select Script_Name,max(Trnx_date) trnx from Actual_NSE_EOD
group by Script_Name
having Max(Trnx_date) between GETDATE()-800 and  getdate() -700
--and  Script_Name like '%%' 
 order by 1

 -- This query will get all the query with min for a given date
 select a.Script_Name,min(a.Trnx_date) Trnx from Actual_NSE_EOD a
group by a.Script_Name
having min(a.Trnx_date) between getdate() -150 and getdate() -50
order by 2 desc;

 
 --script name  change query
 
 begin tran t1
update Actual_NSE_EOD set Script_Name='SITINET' where Script_Name ='SITICABLE';
commit


-- This query will shrink to the desired size execute all the lines

USE StockQuote;
GO
-- Truncate the log by changing the database recovery model to SIMPLE.
ALTER DATABASE StockQuote
SET RECOVERY SIMPLE;
GO
-- Shrink the truncated log file to 1 MB.
DBCC SHRINKFILE (StockQuote_log, 10);
GO
-- Reset the database recovery model.
ALTER DATABASE StockQuote
SET RECOVERY FULL;
GO