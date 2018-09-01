select Script_Name,max(high)High,min(low)Low ,round((max(high)-min(low))/min(low)*100,2) [Change],(min(low)*(max(high)-min(low))/min(low))+min(low)Actual,avg(Volume)Vol
 from Actual_NSE_EOD where Trnx_date > getdate() -100  
group by Script_Name  having min(low)>1 and avg(Volume) > 10000 order by 4 ;