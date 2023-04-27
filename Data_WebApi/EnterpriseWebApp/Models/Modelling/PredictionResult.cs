using Newtonsoft.Json;
using EnterpriseWebApp.Models.Attributes;

namespace EnterpriseWebApp.Models.Modelling
{
    public class PredictionResult : IDataEntityObjects
    {

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore, PropertyName = "Result_ID")]
        [ModelViewColumn(DisplayName = "Result_ID", ToDisplay = true)]
        public int ID { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore, PropertyName = "AirlineDataID")]
        [ModelViewColumn(DisplayName = "AirlineDataID", ToDisplay = true)]
        public int Data_ID { get; set; }


        [JsonProperty(PropertyName = "Satisfaction")]
        [ModelViewColumn(DisplayName = "Satisfaction", ToDisplay = true)]
        public string Satisfaction { get; set; }

        [JsonProperty(PropertyName = "RunDate")]
        [ModelViewColumn(DisplayName = "RunDate", ToDisplay = true)]
        public DateTime RunDate { get; set; }

        public PredictionResult()
        {

        }

        public PredictionResult(int iD, int data_ID, string satisfaction, DateTime runDate)
        {
            ID = iD;
            Data_ID = data_ID;
            Satisfaction = satisfaction;
            RunDate = runDate;
        }

    }
}
