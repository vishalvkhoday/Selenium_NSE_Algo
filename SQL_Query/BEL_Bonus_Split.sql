
begin Tran T1
update Actual_NSE_EOD set Pre_Close = round((Pre_Close/3),2),[Open]= round(( [Open]/3),2),High=round((High/3),2),Low=round((Low/3),2),[Close]=round(([Close]/3),2)
where Script_Name = 'BEL' and Trnx_date < '2015-09-14'
update Actual_NSE_EOD set Pre_Close = round((Pre_Close/3),2) where Script_Name ='BEL' and Trnx_date ='2015-09-14'

update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'BEL' 


update Actual_NSE_EOD set Pre_Close = round((Pre_Close/10),2),[Open]= round(( [Open]/10),2),High=round((High/10),2),Low=round((Low/10),2),[Close]=round(([Close]/10),2)
where Script_Name = 'BEL' and Trnx_date < '2017-03-16'

update Actual_NSE_EOD set Pre_Close = round((Pre_Close/10),2) where Script_Name ='BEL' and Trnx_date ='2017-03-16'

update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'BEL' 

commit