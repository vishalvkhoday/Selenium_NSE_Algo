
 begin tran T1
 update Actual_NSE_EOD set [open] = [open]/2, high =high/2,low =low/2,[Close]=[Close]/2,Pre_Close=Pre_Close/2
 where Trnx_date <= '2015-10-06' and Script_Name = 'BATAINDIA'

 update Actual_NSE_EOD set Pre_Close= Pre_Close/2 where Trnx_date ='2015-10-07' and Script_Name = 'BATAINDIA'

 update dbo.Actual_NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Script_Name = 'BATAINDIA' 

 commit