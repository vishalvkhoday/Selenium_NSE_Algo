
begin Tran T1
update Actual_NSE_EOD set Pre_Close = round((Pre_Close/5),2),[Open]= round(( [Open]/5),2),High=round((High/5),2),Low=round((Low/5),2),[Close]=round(([Close]/5),2)
where Script_Name = 'AXISBANK' and Trnx_date < '2014-07-28'

update Actual_NSE_EOD set Pre_Close = round((Pre_Close/5),2) where Script_Name ='AXISBANK' and Trnx_date ='2014-07-28'

update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'AXISBANK' 


commit