USE [master]
GO
/****** Object:  Database [StockQuote]    Script Date: 9/7/2014 12:22:42 PM ******/
CREATE DATABASE [StockQuote]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'StockQuote', FILENAME = N'C:\Vishal\DB\NSE_EOD\StockQuote.mdf' , SIZE = 318016KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'StockQuote_log', FILENAME = N'C:\Vishal\DB\NSE_EOD\StockQuote_log.ldf' , SIZE = 1024KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
GO
ALTER DATABASE [StockQuote] SET COMPATIBILITY_LEVEL = 100
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [StockQuote].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [StockQuote] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [StockQuote] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [StockQuote] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [StockQuote] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [StockQuote] SET ARITHABORT OFF 
GO
ALTER DATABASE [StockQuote] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [StockQuote] SET AUTO_CREATE_STATISTICS ON 
GO
ALTER DATABASE [StockQuote] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [StockQuote] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [StockQuote] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [StockQuote] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [StockQuote] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [StockQuote] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [StockQuote] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [StockQuote] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [StockQuote] SET  DISABLE_BROKER 
GO
ALTER DATABASE [StockQuote] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [StockQuote] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [StockQuote] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [StockQuote] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [StockQuote] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [StockQuote] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [StockQuote] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [StockQuote] SET RECOVERY FULL 
GO
ALTER DATABASE [StockQuote] SET  MULTI_USER 
GO
ALTER DATABASE [StockQuote] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [StockQuote] SET DB_CHAINING OFF 
GO
ALTER DATABASE [StockQuote] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [StockQuote] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO
USE [StockQuote]
GO
/****** Object:  StoredProcedure [dbo].[Candle_supp]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Candle_supp]
	As
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select an.Script_Name,avg((an.[Open]+an.[Close])/2)Supp from Actual_NSE_EOD an where an.Trnx_date >(
select top 1 (Trnx_date)from (
select distinct top 6 (trnx_date) from Actual_NSE_EOD order by Trnx_date desc ) as T1 order by Trnx_date asc)
group by an.Script_Name order by an.Script_Name;
END

GO
/****** Object:  StoredProcedure [dbo].[DMA20Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DMA20Days]
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   
insert into dbo.MA20Days ([Script_Name], [20DMA], [20Day_vol], Trnx_date)
select Script_Name,AVG([Close])[20DMA],avg(Volume)[20Day_Vol],max(Trnx_date)[Trd Date] from NSE_EOD 
where Trnx_date >= ( select top 1 (Trnx_date) from NSE_EOD where Trnx_date in (
select distinct top 20  (trnx_date)  from NSE_EOD  order by Trnx_date desc)
order by Trnx_date 
)
group by Script_Name

END

GO
/****** Object:  StoredProcedure [dbo].[DMA50Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DMA50Days]
	
AS
BEGIN
	
	SET NOCOUNT ON;

   
insert into dbo.MA50Days ([Script_Name], [50DMA], [50Day_vol], Trnx_date)
select Script_Name,AVG([Close])[50DMA],avg(Volume)[50Day_Vol],max(Trnx_date)[Trd Date] from NSE_EOD 
where Trnx_date >= ( select top 1 (Trnx_date) from NSE_EOD where Trnx_date in (
select distinct top 50  (trnx_date)  from NSE_EOD  order by Trnx_date desc)
order by Trnx_date 
)
group by Script_Name



END

GO
/****** Object:  StoredProcedure [dbo].[DMA5Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[DMA5Days]
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   
insert into dbo.MA5Days ([Script_Name], [5DMA], [5Day_vol], Trnx_date)
select Script_Name,AVG([Close])[5DMA],avg(Volume)[5Day_Vol],max(Trnx_date)[Trd Date] from NSE_EOD 
where Trnx_date >= ( select top 1 (Trnx_date) from NSE_EOD where Trnx_date in (
select distinct top 5  (trnx_date)  from NSE_EOD  order by Trnx_date desc)
order by Trnx_date 
)
group by Script_Name



END

GO
/****** Object:  StoredProcedure [dbo].[NSE_EOD_Insert]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[NSE_EOD_Insert] 
	-- Add the parameters for the stored procedure here
	@script varchar(100),
	@Open float,
	@High float,
	@Low float,
	@Close float,
	@vol bigint,
	@Trn_date date
	
AS
BEGIN
SET DATEFORMAT YMD
    -- Insert statements for procedure here
	Insert into dbo.NSE_EOD values(@script,@Open,@High,@Low,@Close,@vol,'',0,@Trn_date)
	
END

GO
/****** Object:  StoredProcedure [dbo].[RPT_CoDetails]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[RPT_CoDetails]
	-- Add the parameters for the stored procedure here
	@Coname  varchar(50)
	
AS
BEGIN
	SET DATEFORMAT DMY
	select DATENAME(MM,Trnx_date)[Month],YEAR(Trnx_date)[Year],DATEPART(M,trnx_date)MM ,Script_Name,[Open],High,Low,[Close],Change,Volume,convert(varchar(10),Trnx_date,104)Trnx_date from dbo.Actual_NSE_EOD where Script_Name like @Coname
	order by YEAR(Trnx_date),DATEPART(M,trnx_date),Trnx_date
	
END

GO
/****** Object:  StoredProcedure [dbo].[RPT_CoDetails_Month]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[RPT_CoDetails_Month]
	-- Add the parameters for the stored procedure here
	@Coname  varchar(50),
	@Month	int
	
AS
BEGIN
	SET DATEFORMAT DMY
	select DATENAME(MM,Trnx_date)[Month],YEAR(Trnx_date)[Year],
	Script_Name,[Open],High,Low,[Close],Change,Volume,convert(varchar(10),Trnx_date,104)Trnx_date 
	from dbo.Actual_NSE_EOD where Script_Name like @Coname and DATEPART(m,Trnx_date) =@Month
	order by YEAR(Trnx_date),DATEPART(M,trnx_date),Trnx_date
	
END

GO
/****** Object:  StoredProcedure [dbo].[SP_Hotpick]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SP_Hotpick]
	-- Add the parameters for the stored procedure here
	AS
BEGIN
	
	insert into dbo.HotPick (Script_Name, ClosingPrice, Volume, Trnx_date)
select ANE.Script_Name,ANE.[Close],ANE.Volume,ANE.Trnx_date from dbo.Actual_NSE_EOD ANE 
inner join dbo.MA20Days MA20 on ANE.Script_Name = MA20.Script_Name and ANE.Trnx_date= MA20.Trnx_date 
where ANE.[Close] > (MA20.[20DMA] +(MA20.[20DMA]* 0.05))   and ANE.Volume > 250000 
and MA20.[20Day_vol] < ANE.Volume and ANE.[Close] between 20 and 1350 and ANE.Trnx_date = 
(select MAX(Trnx_date)from Actual_NSE_EOD) order by ANE.Script_Name
END

GO
/****** Object:  StoredProcedure [dbo].[Update_preClose]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Update_preClose]
	@ScriptName varchar (100),
	@Pre_dt  date
	
AS
BEGIN
	
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

Declare @Cur_dt date;
Declare @ClsPrice float;

SET DATEFORMAT YMD

/*set @pre_dt = ( select top 1 trnx_date from NSE_EOD where Trnx_date in (
select distinct  top 2 (trnx_date)Trnx_Date from NSE_EOD order by Trnx_date desc)
order by Trnx_date);*/

set @Cur_dt = (select distinct MAX (trnx_date)from dbo.NSE_EOD )

set @ClsPrice = (select distinct [close] from dbo.NSE_EOD where Script_Name = @ScriptName and Trnx_date = @Pre_dt)
    -- Insert statements for procedure here
	update dbo.NSE_EOD set Pre_Close = @ClsPrice where Script_Name = @ScriptName and Trnx_date= @Cur_dt
	--update dbo.NSE_EOD set Change = round(([Close]- Pre_Close )/Pre_Close * 100,2) where Trnx_date= @Cur_dt
End

GO
/****** Object:  Table [dbo].[Actual_NSE_EOD]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[Actual_NSE_EOD](
	[Script_Name] [varchar](100) NOT NULL,
	[Open] [float] NOT NULL,
	[High] [float] NOT NULL,
	[Low] [float] NOT NULL,
	[Close] [float] NOT NULL,
	[Volume] [bigint] NOT NULL,
	[Pre_Close] [float] NULL,
	[Change] [float] NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[HotPick]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HotPick](
	[Script_Name] [nchar](100) NULL,
	[ClosingPrice] [float] NULL,
	[Volume] [bigint] NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[MA20Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[MA20Days](
	[Script_Name] [varchar](50) NOT NULL,
	[20DMA] [float] NOT NULL,
	[20Day_vol] [float] NOT NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[MA50Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[MA50Days](
	[Script_Name] [varchar](50) NOT NULL,
	[50DMA] [float] NOT NULL,
	[50Day_vol] [float] NOT NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[MA5Days]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[MA5Days](
	[Script_Name] [varchar](50) NOT NULL,
	[5DMA] [float] NOT NULL,
	[5Day_vol] [float] NOT NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[NSE_EOD]    Script Date: 9/7/2014 12:22:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[NSE_EOD](
	[Script_Name] [varchar](100) NOT NULL,
	[Open] [float] NOT NULL,
	[High] [float] NOT NULL,
	[Low] [float] NOT NULL,
	[Close] [float] NOT NULL,
	[Volume] [bigint] NOT NULL,
	[Pre_Close] [float] NULL,
	[Change] [float] NULL,
	[Trnx_date] [date] NOT NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
SET ANSI_PADDING ON

GO
/****** Object:  Index [INd_Script]    Script Date: 9/7/2014 12:22:42 PM ******/
CREATE CLUSTERED INDEX [INd_Script] ON [dbo].[NSE_EOD]
(
	[Script_Name] ASC,
	[Trnx_date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [StockQuote] SET  READ_WRITE 
GO
