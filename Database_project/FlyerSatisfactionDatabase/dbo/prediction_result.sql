CREATE TABLE [dbo].[prediction_result]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Data_ID] [int] NOT NULL,
	[Satisfaction] [varchar](50) NOT NULL,
	[RunDate] [datetime] NOT NULL DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT PK_prediction_result PRIMARY KEY(ID)
)
