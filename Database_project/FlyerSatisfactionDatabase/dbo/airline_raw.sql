﻿CREATE TABLE [dbo].[airline_raw](
	[ID] [int] NOT NULL IDENTITY(1,1),
	[User_Id] [int] NULL,
	[Gender] [varchar](50) NOT NULL,
	[CustomerType] [varchar](50) NULL,
	[Age] [int] NULL,
	[TravelType] [varchar](50) NULL,
	[Class] [varchar](50) NULL,
	[Distance] [int] NULL DEFAULT 0,
	[InflightWifi] [int] NULL DEFAULT 1,
	[DeptArriveConvenience] [int] NULL DEFAULT 1,
	[OnlineBooking] [int] NULL DEFAULT 1,
	[GateLocation] [int] NULL DEFAULT 1,
	[Food] [int] NULL DEFAULT 1,
	[OnlineBoarding] [int] NULL DEFAULT 1,
	[SeatComfort] [int] NULL DEFAULT 1,
	[InflightEntertainment] [int] NULL DEFAULT 1,
	[OnboardService] [int] NULL DEFAULT 1,
	[LegRoom] [int] NULL DEFAULT 1,
	[Baggage] [int] NULL DEFAULT 1,
	[Checkin] [int] NULL DEFAULT 1,
	[InflightService] [int] NULL DEFAULT 1,
	[Cleanliness] [int] NULL DEFAULT 1,
	[DepartDelay] [int] NULL DEFAULT 1,
	[ArriveDelay] [int] NULL DEFAULT 1,
	[Satisfaction] [varchar](50) NULL DEFAULT ('neutral or dissatisfied') ,
	[DataDate] [date] NULL DEFAULT CURRENT_TIMESTAMP,
	[IsTrain] [int] DEFAULT(0)

	CONSTRAINT PK_airline_raw PRIMARY KEY(ID)
)
