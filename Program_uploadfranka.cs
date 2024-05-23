using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

using Azure;
using Azure.DigitalTwins.Core;
using Azure.Identity;

//using System.Threading.Tasks;
//using System.IO;
//using System.Collections.Generic;

//using Newtonsoft.Json;
//using Newtonsoft.Json.Linq; // For JObject class

using System.Text.Json; // For DT properties
using System.Text.Json.Serialization; // For JsonPropertyName

using System.Timers;


namespace uploadDTtoAzure
{
    class Program
    {
        static string adtInstanceUrl = "https://FrankaMyJoghurtDTCreation.api.weu.digitaltwins.azure.net";

        static List<string> allModelPaths = new List<string>();
        static List<string> allInstanceStrings = new List<string>();
        static List<BasicRelationship> allRelationships = new List<BasicRelationship>();
        static string relationshipData = string.Empty;

        static string ModelInitialDirectory = "../Ontology";
        static string InstanceInitialDirectory = "../AzureDTDLs/Instances/FrankaRobot";
        static string RelInitialDirectory = "../AzureDTDLs/Rels/FrankaRobot/FrankaRobotRels.json";

        static List<string> allModelStrings = new List<string>();
        static List<BasicDigitalTwin> allInstances = new List<BasicDigitalTwin>();

//  await fuction needs aszn  The 'await' operator can only be used within an async method. Consider marking this method with the 'async' modifier and changing its return type to 'Task'.
 //A void or int returning entry point cannot be async
 // after adding async Task Main(string[] args) the error is gone
 //after uploading the model, the model is now shown in the Azure Digital Twins Explorer
 //we don't need to upload the model again, if we want to upload the model again, we need to delete the model first
 //after uploading the model, we can chane the asyn Task Main to static void Main in order to delete the instances and relationships firstly
        static void Main(string[] args)
        {
            var credential = new DefaultAzureCredential();
            DigitalTwinsClient client = new DigitalTwinsClient(new Uri(adtInstanceUrl), credential);



            // // get all model files
            //get_all_model_files();
            Console.WriteLine("\nSuccessfully read all model files. ");
            // // upload all models in Azure
            //await client.CreateModelsAsync(allModelStrings);
            Console.WriteLine("Successfully uploaded all models.");

            delete_all(client);
            Console.WriteLine("Start Deleting. Press any key to stop");
            Console.ReadKey();
        
            upload_instances_rels(client);
            Console.WriteLine("Start Uploading. Press any key to stop");
            Console.ReadKey();

        }

        static void get_all_model_files()
        {
            // Clear the existing list before loading new model data
            allModelStrings.Clear();
            allModelPaths = Directory.EnumerateFiles(ModelInitialDirectory, "*.json", SearchOption.AllDirectories).ToList();

            foreach (string modelPath in allModelPaths)
            {
                string nextModelString = File.ReadAllText(modelPath);
                allModelStrings.Add(nextModelString);
            }

        }


        static void get_all_instance_files()
        {
            // Clear the existing list before loading new instance data
            allInstanceStrings.Clear();
            // List all path to the individual files
            List<string> allInstancePaths = Directory.EnumerateFiles(InstanceInitialDirectory, "*.json", SearchOption.AllDirectories).ToList();

            foreach (string instancePath in allInstancePaths)
            {
                string nextInstanceString = File.ReadAllText(instancePath);
                allInstanceStrings.Add(nextInstanceString);
            }

        }



        static void get_all_rels()
        {

            relationshipData = File.ReadAllText(RelInitialDirectory);

            // Deserialize the string to a json array like object
            var relationshipsDeserialized = JsonSerializer.Deserialize<List<Dictionary<string, string>>>(relationshipData);

            foreach (var nextRelationshipData in relationshipsDeserialized)
            {
                var nextRelationship = new BasicRelationship
                {
                    TargetId = nextRelationshipData["$targetId"],
                    SourceId = nextRelationshipData["$sourceId"],
                    Id = nextRelationshipData["$relationshipId"],
                    Name = nextRelationshipData["$relationshipName"]
                };

                allRelationships.Add(nextRelationship);
            }

        }


        static void create_DT_Instances()
        {
            // Functions that processes the click event, creates digital twin instances from
            // the class BasicDigitalTwin and calls the upload task.

            var metadata_json_value = JsonSerializer.Deserialize<object>("{\"$metadata\":{}}");

            string TwinType = ""; // Helper variable to later fill in missing components

            foreach (string nextInstance in allInstanceStrings)
            {
                // Use-Case for JsonDocument: You don’t know the format of the JSON or the JSON could have multiple formats.
                // https://marcroussy.com/2020/08/17/deserialization-with-system-text-json/
                //var test = JsonDocument.Parse(nextInstance);

                // https://stackoverflow.com/questions/1207731/how-can-i-deserialize-json-to-a-simple-dictionarystring-string-in-asp-net
                var des = JsonSerializer.Deserialize<Dictionary<string, object>>(nextInstance);

                var dt = new BasicDigitalTwin();

                Dictionary<string, object> metadataObject;

                foreach (KeyValuePair<string, object> kvp in des)
                {
                    //Console.WriteLine(kvp.Key);

                    if (kvp.Key == "$dtId")
                    {
                        //Console.WriteLine("Found Id: " + kvp.Value.ToString());
                        dt.Id = kvp.Value.ToString();
                        continue;
                    }

                    if (kvp.Key == "$etag")
                    {
                        //Console.WriteLine("Skipping etag ...");
                        continue;
                    }

                    if (kvp.Key == "$metadata")
                    {
                        //Console.WriteLine("Found Metadata ...");
                        metadataObject = JsonSerializer.Deserialize<Dictionary<string, object>>(kvp.Value.ToString());

                        foreach (KeyValuePair<string, object> meta_kvp in metadataObject)
                        {
                            if (meta_kvp.Key == "$model")
                            {
                                dt.Metadata.ModelId = meta_kvp.Value.ToString();

                                if (dt.Metadata.ModelId == "dtmi:digitaltwins:aas:Submodel;1")
                                    TwinType = "Submodel";
                                // add type AAS
                                else if (dt.Metadata.ModelId == "dtmi:digitaltwins:aas:AssetAdministrationShell;1")
                                    TwinType = "AssetAdministrationShell";
                                else
                                    TwinType = ""; // Reset twin type again 
                            }
                        }
                        continue;
                    }

                    // Create remaining content
                    // This creates the 'administration' and 'identification' parts for the aas and
                    // contents such as 'value' and 'valueType' for properties.
                    dt.Contents.Add(kvp);

                }

                // Apparently there are some mandatory components that are not automaticaly integrated
                List<string> current_key = new List<string>();
                foreach (var dt_content in dt.Contents)
                {
                    current_key.Add(dt_content.Key);
                }
                // Check for the key "displayName" if it doesn't exist add metadata info to it.
                if (!current_key.Contains("displayName"))
                {
                    KeyValuePair<string, object> manual_displayName_kvp = new KeyValuePair<string, object>("displayName", metadata_json_value);
                    dt.Contents.Add(manual_displayName_kvp);
                }
                if (!current_key.Contains("description"))
                {
                    KeyValuePair<string, object> manual_description_kvp = new KeyValuePair<string, object>("description", metadata_json_value);
                    dt.Contents.Add(manual_description_kvp);
                }
                if (!current_key.Contains("tags"))
                {
                    KeyValuePair<string, object> manual_tags_kvp = new KeyValuePair<string, object>("tags", metadata_json_value);
                    dt.Contents.Add(manual_tags_kvp);
                }
                if (!current_key.Contains("administration") && TwinType == "Submodel")
                {
                    KeyValuePair<string, object> manual_administration_kvp = new KeyValuePair<string, object>("administration", metadata_json_value);
                    dt.Contents.Add(manual_administration_kvp);
                }
                // identification not for submodel, but for aas
                // removed the row in manual PandaAAS: "identification": {"$metadata":{}}, 
                // if (!current_key.Contains("identification") && TwinType == "AssetAdministrationShell")
                // {
                //     KeyValuePair<string, object> manual_identification_kvp = new KeyValuePair<string, object>("identification", metadata_json_value);
                //     dt.Contents.Add(manual_identification_kvp);
                // }
                if (!current_key.Contains("assetInformationShort") && TwinType == "AssetAdministrationShell")
                {
                    KeyValuePair<string, object> manual_identification_kvp = new KeyValuePair<string, object>("assetInformationShort", metadata_json_value);
                    dt.Contents.Add(manual_identification_kvp);
                    //Console.WriteLine(dt.Contents);
                }

                allInstances.Add(dt);

            }

        }



        static async Task delete_all (DigitalTwinsClient client)
        {
            // query all rels and delete them
            string query = "SELECT * FROM digitaltwins";
            AsyncPageable<BasicDigitalTwin> queryResult = client.QueryAsync<BasicDigitalTwin>(query);

            await foreach (BasicDigitalTwin twin in queryResult)
            {
                //Console.WriteLine(twin.Id);
                Pageable<IncomingRelationship> allIncoming = client.GetIncomingRelationships(twin.Id);
                foreach (IncomingRelationship incomingRel in allIncoming)
                {
                    await client.DeleteRelationshipAsync(incomingRel.SourceId, incomingRel.RelationshipId).ConfigureAwait(false);
                }
            }
            Console.WriteLine("Successfully deleted all rels");


            // query all twins and delete them
            // string query = "SELECT * FROM digitaltwins";
            // AsyncPageable<BasicDigitalTwin> queryResult = client.QueryAsync<BasicDigitalTwin>(query);

            await foreach (BasicDigitalTwin twin in queryResult)
            {
                //Console.WriteLine(twin.Id);
                await client.DeleteDigitalTwinAsync(twin.Id);
                Console.WriteLine(twin.Id);
                //Console.WriteLine(JsonSerializer.Serialize(twin));
            }
            Console.WriteLine("Successfully deleted all instances");

           

        }

        static async Task upload_instances_rels(DigitalTwinsClient client)
        {
            BasicDigitalTwin response_dt;
            BasicRelationship response_rel;
            // get all instance files and upload them in Azure
            // get all instance files
            get_all_instance_files();
            Console.WriteLine("\nSucsessfully read all instance files.");
            // create dt instances
            create_DT_Instances();
            Console.WriteLine("Successfully created all DT instances.");
            // upload all instances in Azure
            foreach (BasicDigitalTwin dt in allInstances)
            {
                //Console.WriteLine(JsonSerializer.Serialize(dt));
                try
                {
                    Console.WriteLine(dt.Id);
                    Response<BasicDigitalTwin> twin_res = await client.CreateOrReplaceDigitalTwinAsync<BasicDigitalTwin>(dt.Id, dt);
                    response_dt = twin_res.Value;
                }
                catch (RequestFailedException ex)
                {
                    Console.WriteLine(ex);
                }
                
            }
            Console.WriteLine("Successfully uploaded all instances.");

            // get all rels and create dt rels in Azure
            get_all_rels();
            Console.WriteLine("\nSucsessfully get all rels.");
            //upload all rels in Azure
            foreach (var rel in allRelationships)
            {
                Console.WriteLine("SourceId:" + rel.SourceId);
                Console.WriteLine("TargetId:" + rel.TargetId);
                try
                {
                    Response<BasicRelationship> twin_res = await client.CreateOrReplaceRelationshipAsync(rel.SourceId, rel.TargetId, rel);
                    response_rel = twin_res.Value;
                }
                catch (RequestFailedException ex)
                {
                    Console.WriteLine(ex);
                }
                
            }
            Console.WriteLine("Successfully uploaded all rels");
        }

    }

}