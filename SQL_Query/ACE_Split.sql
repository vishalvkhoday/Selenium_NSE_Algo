 insert into Temp_Actual_NSE_EOD 
 select * from Actual_NSE_EOD where Script_Name ='ACE'
 
 
 select * from Temp_Actual_NSE_EOD order by Trnx_date

 begin tran T1
 update Temp_Actual_NSE_EOD set [open] = [open]/5, high =high/5,low =low/5,[Close]=[Close]/5,Pre_Close=Pre_Close/5
 where Trnx_date <= '2008-03-12'  and Script_Name = 'ACE'

 update Temp_Actual_NSE_EOD set Pre_Close= Pre_Close/5 where Trnx_date ='2008-03-13'

 update dbo.Temp_Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'ACE' 

