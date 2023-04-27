using Newtonsoft.Json;
using EnterpriseWebApp.Models.Attributes;

namespace EnterpriseWebApp.Models.Extract
{
    public class ExtractPredictionResult : IDataEntityObjects
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

        public ExtractPredictionResult() { }

        public ExtractPredictionResult(int iD, int data_ID, string satisfaction, DateTime runDate)
        {
            ID = iD;
            Data_ID = data_ID;
            Satisfaction = satisfaction;
            RunDate = runDate;
        }

        public static ExtractPredictionResult Map(Modelling.PredictionResult item) => new ExtractPredictionResult
        {
            ID = item.ID,
            Data_ID = item.Data_ID,
            RunDate = item.RunDate,
            Satisfaction = item.Satisfaction
        };
    }
}
