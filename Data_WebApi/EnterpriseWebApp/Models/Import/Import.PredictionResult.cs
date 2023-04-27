using Newtonsoft.Json;
using EnterpriseWebApp.Models.Attributes;

namespace EnterpriseWebApp.Models.Import
{
    public class ImportPredictionResult : IDataEntityObjects
    {

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore, PropertyName = "Result_ID")]
        [ModelViewColumn(DisplayName = "Result_ID", ToDisplay = true)]
        public int ID { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore, PropertyName = "Data_ID")]
        [ModelViewColumn(DisplayName = "Data_ID", ToDisplay = true)]
        public int Data_ID { get; set; }


        [JsonProperty(PropertyName = "Satisfaction")]
        [ModelViewColumn(DisplayName = "Satisfaction", ToDisplay = true)]
        public string Satisfaction { get; set; }

        public ImportPredictionResult()
        {

        }

        public ImportPredictionResult(int iD, int data_ID, string satisfaction)
        {
            ID = iD;
            Data_ID = data_ID;
            Satisfaction = satisfaction;
        }
    }
}
