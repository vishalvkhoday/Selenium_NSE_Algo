

select * from Actual_NSE_EOD where Trnx_date between '2016-09-25' and  '2016-10-15'
and Script_Name = 'BHEL'
order by Trnx_date 

truncate table Actual_NSE_EOD


insert into Actual_NSE_EOD
select * from StockQuote.dbo.Actual_NSE_EOD where Script_Name ='BHEL' order by Trnx_date



begin tran T1
update Actual_NSE_EOD set [Open] = [Open]/5 where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29'

update Actual_NSE_EOD set High = High/5 where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29'

update Actual_NSE_EOD set Low = low/5 where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29'

update Actual_NSE_EOD set [Close] = [Close]/5 where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29'

update Actual_NSE_EOD set Pre_Close = Pre_Close/5 where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29' 


-- Bonus 3:2 

begin Tran T2

update Actual_NSE_EOD set [Open] = round( (([Open] *2)/3),2) where Script_Name = 'BHEL' and Trnx_date <= '2017/09/27'

update Actual_NSE_EOD set High = round(((High *2)/3),2) where Script_Name = 'BHEL' and Trnx_date <= '2017/09/27'

update Actual_NSE_EOD set Low = round (((low * 2)/3),2) where Script_Name = 'BHEL' and Trnx_date <= '2017/09/27'

update Actual_NSE_EOD set [Close] = round ((([Close]* 2)/3),2) where Script_Name = 'BHEL' and Trnx_date <= '2017/09/27'

update Actual_NSE_EOD set Pre_Close =  round (((Pre_Close * 2 )/3),2) where Script_Name = 'BHEL' and Trnx_date <= '2017/09/27'


begin Tran T3

update Actual_NSE_EOD set Pre_Close = '222.17' where Trnx_date = '2011-10-05'

update Actual_NSE_EOD set Pre_Close = '83.1' where Trnx_date ='2017-09-28'

--1174

select * from Actual_NSE_EOD where Script_Name = 'BHEL' and Trnx_date <= '2011-09-29';

begin Tran T4
update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'BHEL' 


commit