
from basyx.aas import model
import basyx.aas.adapter.aasx
import sys
import os


class AzureDTFile:
    '''
    Top-Level class that stores and assembles the individual parts
    of the Azure Digital Twins input file.
    '''

    def __init__(self, objects):

        self.fileInfo = '"digitalTwinsFileInfo": {"fileVersion":"1.0.0"}'
        self.twinInstances = DTDLInstanceCreator(objects).createInstanceData()
        self.relationships = TwinGraphRelationshipCreator(objects).generateRelationshipsData()
        self.twinGraph = f'"digitalTwinsGraph": {{ "digitalTwins": {self.twinInstances}, "relationships": {self.relationships}}}' 
        self.TwinModel = self.load_model() # JSON Key 'DigitalTwinModels' included in file

    def createFile(self):
        '''
        Pieces the individual parts together to form the complete file for the upload in Azure-DT.s
        '''
        completeDataSet = (f'{{{self.fileInfo}, '
                           f'{self.twinGraph}, '
                           f'{self.TwinModel} }}')

        with open("AzureInput.json", 'w', encoding='utf-8') as writer:
            writer.write(completeDataSet)

    def load_model(self):
        '''
        Helper function to load the AAS Meta-Model implemented in DTDL from an external text file.
        '''
        with open('LibAASDTDL.txt', 'r', encoding='utf-8') as reader:
            wholeModelString = reader.read()
            
        return wholeModelString


class DTDLInstanceCreator:

    def __init__(self, objects):
        
        self.allObjects = objects

        self.instanceString = ''
        self.numObjects = len(objects)
        self.version = "0.0"

        # For the Azure-DT client app each DT instance will be
        # in a seperate JSON file.
        self.allInstances = []
        self.allInstanceNames = []


    def createInstanceData(self, allObjects, parent_operation = None):
        #TODO: Add first and last [] to full instance string
        #TODO: RelationshipElement
        # Final elements are not iterable anymore.
        try:
            iterator = iter(allObjects)
        except TypeError:
            allObjects = [allObjects]

        for obj in allObjects:
            # Append string for the AAS
            if isinstance(obj, model.AssetAdministrationShell):
                self.instanceString += self.createAASInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createAASInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))

            # Append string for a Submodel
            elif isinstance(obj, model.Submodel):            
                self.instanceString += self.createSubmodelInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createSubmodelInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))
                # Submodel most likely includes additional submodel elment collections, properties, operations, capabilities, etc.
                #for sub_elm in obj:
                self.createInstanceData(obj.submodel_element)

            elif isinstance(obj, model.SubmodelElementCollection):
                self.instanceString += self.createSubmodelElementCollectionInstance(obj)                    
                self.instanceString += ','
                self.allInstances.append(self.createSubmodelElementCollectionInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))
                # Submodel element collection contains additional elemtents, recursive function call
                # to capture all depths of nesting.      
                self.createInstanceData(obj.value)

            elif isinstance(obj, model.Property):                        
                self.instanceString += self.createPropertyInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createPropertyInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))

            elif isinstance(obj, model.Capability):
                self.instanceString += self.createCapabilityInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createCapabilityInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))     

            elif isinstance(obj, model.Operation):
                self.instanceString += self.createOperationInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createOperationInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))   
                for operational_variable in (obj.input_variable + obj.in_output_variable + obj.output_variable):
                    self.createInstanceData(operational_variable, parent_operation = obj.id_short)

            # jingyun added comments
            # branch v2.0.1 support OperationVariable
            elif isinstance(obj, model.OperationVariable): 
                # print(obj.value.id_short)
                self.instanceString += self.createOperationalVariableInstance(obj, parent_operation)
                self.instanceString += ','
                self.allInstances.append(self.createOperationalVariableInstance(obj, parent_operation))
                self.allInstanceNames.append(str("OpVar"+obj.value.id_short+parent_operation)) 
            #ziyu added entity
            elif isinstance(obj, model.Entity):                        
                self.instanceString += self.createEntityInstance(obj)
                self.instanceString += ','
                self.allInstances.append(self.createEntityInstance(obj))
                self.allInstanceNames.append(str(obj.id_short))

    def createAASInstance(self, aas : model.AssetAdministrationShell):
        '''
        Creates the aas instance string.
        '''
        return (f'{{"$dtId":"{aas.id_short}", \n'
			    f'"$etag":"W/\\"dummy-etag\\"", \n'
			    f'"administration": {{"$metadata":{{}}}}, \n'
                # remove this line
			    #f'"identification": {{"$metadata":{{}}}}, \n'
			    f'"$metadata": {{ "$model":"dtmi:digitaltwins:aas:AssetAdministrationShell;1"}}'
                f'}}' )

    def createSubmodelInstance(self, submodel : model.Submodel):
        '''
        Creates the submodel instance string.
        '''
        return (f'{{"$dtId":"{submodel.id_short}", \n'
			  f'"$etag":"W/\\"dummy-etag\\"", \n'
			  f'"kind": {{"$metadata":{{}}}},\n' 
			  f'"$metadata": {{"$model":"dtmi:digitaltwins:aas:Submodel;1"}}'
		      f'}}')

    def createSubmodelElementCollectionInstance(self, sme: model.SubmodelElementCollection):
        '''
        Creates the string for the submodel element collection.
        '''
        return (f'{{"$dtId":"{sme.id_short}", \n'
				f'"$etag":"W/\\"0109bbb4-37a4-4eb2-9971-3fbeb7e0dbd4\\"", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
				f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:SubmodelElementCollection;1"}}'
			    f'}}')

    def createPropertyInstance(self, prop : model.Property):
        '''
        Createst the property instance string. A property has a value and a value type
        that need to be included in the string.
        '''
        # TODO: Include description, value_id, category
        return (f'{{"$dtId":"{prop.id_short}", \n'
				f'"$etag":"W/\\"6030225d-b379-4134-beea-ea2af2a16c34\\"", \n'
				f'"value":"{prop.value}", \n'
				f'"valueType":"{prop.value_type}", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
				f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:Property;1"}} }}')
    
    def createCapabilityInstance(self, capability : model.Capability):
        '''
        Creates the capability instance string. Right now there are no further values specified.
        '''
        return (f'{{"$dtId":"{capability.id_short}", \n'
				f'"$etag":"W/\\"0109bbb4-37a4-4eb2-9971-3fbeb7e0dbd4\\"", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
				f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:Capability;1"}}'
			    f'}}')

    def createOperationInstance(self, operation : model.Operation):
        '''
        Creates the operation instance string.
        '''
        return (f'{{"$dtId":"{operation.id_short}", \n'
				f'"$etag":"W/\\"0109bbb4-37a4-4eb2-9971-3fbeb7e0dbd4\\"", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
                # Jingyun Comment, TODO we modify Operation as SMC to let it work
				# f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:Operation;1"}}'
                f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:SubmodelElementCollection;1"}}'
			    f'}}')
    
    # jingyun added comments
    # branch v2.0.1 support OperationVariable
    def createOperationalVariableInstance(self, opVar : model.OperationVariable, parent_operation):
        '''
        Creates the OperationalVariable instance string.
        '''
        # print(opVar.value.id_short)
        return (f'{{"$dtId": "OpVar{opVar.value.id_short}{parent_operation}", \n'
                # jingyun comment: no tag, kind in model DTDL
				f'"$etag":"W/\\"0109bbb4-37a4-4eb2-9971-3fbeb7e0dbd4\\"", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
                # jingyun comment: TODO not property, but should be operational variable, we currectly set Operation as SMC to let it run.
				f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:Property;1"}}'
                # f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:OperationVariable;1"}}'
			    f'}}')
    # ziyu added entity 
    def createEntityInstance(self, prop : model.Entity):
        
        return (f'{{"$dtId":"{prop.id_short}", \n'
				f'"$etag":"W/\\"6030225d-b379-4134-beea-ea2af2a16c34\\"", \n'
				#f'"value":"{prop.value}", \n'
				#f'"valueType":"{prop.value_type}", \n'
				f'"kind":{{"$metadata":{{}}}}, \n'
				f'"$metadata":{{"$model":"dtmi:digitaltwins:aas:Entity;1"}} }}')

    def writeInstanceFiles(self, folder_name):        
        
        FILEPATH = os.getcwd()+"/AzureDTDLs/Instances/"+ folder_name+ "/"
        for instance, name in zip(self.allInstances, self.allInstanceNames):
            with open(FILEPATH+name+".json", 'w') as f:
                f.writelines(instance)
                

   
class TwinGraphRelationshipCreator:
    '''
    Creates the relationship data necessary to generate the twin graph.
    '''

    def __init__(self, objects):
        self.allObjects = objects
        # Decides if the AAS Submodel Elements "Relationship" is explicitly included as 
        # a line in the graph.
        self.explicitRelationships = False 
        # Counts the number of created relationships and thereby also provides uniqe ids
        # for the relationships.
        self.relationships_counter = 0

        self.numObjects = len(objects)
        self.version = "0.0"

        # Additional attributes to directly write to file
        self.allRelationships = []
    
    def generateRelationshipsData(self) -> str:
        # Opening brackets for the JSON-Array that is the value for the 'relationships' key
        # in the Azure-DT data file.
        next_relationship = '['
        
        # Iterating through the objects and building relationships.
        # AAS, submodels and submodel element collections can be used as sources multiple times.
        # The AAS is the root of the tree-like graph.
        # Submodel elements, e.g. properties are the leaf nodes.

        # Composition of the relationship id: Concatenation of the id_short strings plus relationship-counter. 
        
        for obj in self.allObjects:
            
            if isinstance(obj, model.Submodel):
                
                for elm in obj:
                    if isinstance(elm, model.Property) or isinstance(elm, model.SubmodelElementCollection): # TODO: Adapt for Capabilities etc. with or
                        # Move up counter
                        self.relationships_counter +=1
                        # The next id is a concatenation of the id shorts and counter
                        next_rel_id = obj.id_short + elm.id_short + str(self.relationships_counter)
                        # Create unique etags
                        next_etag = "etag" + str(self.relationships_counter)
                        # Generate the string for the next relationship.
                        # Note that the id for the the dtdl instance $dtid is the id-short
                        self.allRelationships.append(self.create_next_instance_string("submodelElement", next_rel_id, obj.id_short, elm.id_short, next_etag))

                    # Use parent class to check for instances of both unordered and ordered submodel element collections
                    if isinstance(elm, model.SubmodelElementCollection):

                        for subelm in elm:
                            
                            if isinstance(subelm, model.Property): # TODO: Adapt for Capabilities etc. with or                               
                                # Move up counter
                                self.relationships_counter +=1
                                # The next id is a concatenation of the id shorts and counter
                                next_rel_id = elm.id_short + subelm.id_short + str(self.relationships_counter)
                                # Create unique etags
                                next_etag = "etag" + str(self.relationships_counter)
                                # Generate the string for the next relationship.
                                # Note that the id for the the dtdl instance $dtid is the id-short
                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, elm.id_short, subelm.id_short, next_etag))

                            if isinstance(subelm, model.Capability):
                                self.relationships_counter += 1
                                next_rel_id = elm.id_short+subelm.id_short+str(self.relationships_counter)
                                next_etag = "etag" + str(self.relationships_counter)
                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, elm.id_short, subelm.id_short, next_etag))
                            # ziyu added entity relationshios
                            if isinstance(subelm, model.Entity):
                                self.relationships_counter += 1
                                next_rel_id = elm.id_short+subelm.id_short+str(self.relationships_counter)
                                next_etag = "etag" + str(self.relationships_counter)
                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, elm.id_short, subelm.id_short, next_etag))   

                            # Relationship elements are only considered in the graph as lines if explicitly defined.
                            if isinstance(subelm, model.RelationshipElement) and self.explicitRelationships:
                                self.relationships_counter += 1
                                rel_keys = subelm.first.key # Will provide a tuple of two keys, the second on is the target
                                target_id = rel_keys[1].value # Will return the id_short of the target 
                                source_id = elm.id_short # Source will be the name of the smc, e.g. a chess piece smc
                                next_rel_id = target_id+subelm.id_short+str(self.relationships_counter)
                                next_etag = "etag" + str(self.relationships_counter)
                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, source_id, target_id, next_etag))
                                
                            # Submodel Element Collection can contain another smc
                            if isinstance(subelm, model.SubmodelElementCollection):
                                self.relationships_counter += 1
                                next_rel_id = elm.id_short+subelm.id_short+str(self.relationships_counter)
                                next_etag = "etag" + str(self.relationships_counter)
                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, elm.id_short, subelm.id_short, next_etag))      

                                # Collect properties in the nested submodel element collection.
                                # Currently implemented for two levels of smcs.
                                for subsubelm in subelm:
                                    if isinstance(subsubelm, model.Property):
                                        self.relationships_counter += 1
                                        next_rel_id = subelm.id_short+subsubelm.id_short+str(self.relationships_counter)
                                        next_etag = "etag" + str(self.relationships_counter)
                                        self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, subelm.id_short, subsubelm.id_short, next_etag))
                                     #ziyu added new relationships
                                    if isinstance(subsubelm, model.SubmodelElementCollection):
                                        self.relationships_counter += 1
                                        next_rel_id = subelm.id_short+subsubelm.id_short+str(self.relationships_counter)
                                        next_etag = "etag" + str(self.relationships_counter)
                                        self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, subelm.id_short, subsubelm.id_short, next_etag))
                                        for subsubsubelm in subsubelm:
                                            if isinstance(subsubsubelm, model.Property):
                                                self.relationships_counter += 1
                                                next_rel_id = subsubelm.id_short+subsubsubelm.id_short+str(self.relationships_counter)
                                                next_etag = "etag" + str(self.relationships_counter)
                                                self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, subsubelm.id_short, subsubsubelm.id_short, next_etag)) 

                    if isinstance(elm, model.Operation):
                        # Handel relation from submodel to operation 
                        self.relationships_counter +=1  
                        next_rel_id = obj.id_short + elm.id_short + str(self.relationships_counter)   
                        next_etag = "etag" + str(self.relationships_counter)
                        self.allRelationships.append(self.create_next_instance_string("submodelElement", next_rel_id, obj.id_short, elm.id_short, next_etag))
                        for opVar in elm.input_variable:
                            opVarId = "OpVar"+opVar.value.id_short+elm.id_short
                            # opVarId = opVar.value.id_short
                            next_rel_id = obj.id_short + opVarId + str(self.relationships_counter)   
                            next_etag = "etag" + str(self.relationships_counter)
                            # Jingyun modified: TODO now we set relation as value to let it work 
                            # self.allRelationships.append(self.create_next_instance_string("operationalVar", next_rel_id, elm.id_short, opVarId, next_etag))
                            self.allRelationships.append(self.create_next_instance_string("value", next_rel_id, elm.id_short, opVarId, next_etag))
                    
                    # Relationship elements are only considered in the graph as lines if explicitly defined.
                    if isinstance(elm, model.RelationshipElement) and self.explicitRelationships:
                        pass



            if isinstance(obj, model.AssetAdministrationShell):         
               # List all id-s of the submodels that are refereced by the AAS
               all_submodel_ids = [s_id.key[0].value for s_id in obj.submodel]
               # Iterate over all objects ...
               for sm in self.allObjects:
                  # ... and compare submodel ids with the aas references.
                  if isinstance(sm, model.Submodel):
                      if sm.identification.id in all_submodel_ids:
                           # Move up counter
                           self.relationships_counter +=1
                           # The next id is a concatenation of the id shorts and counter
                           next_rel_id = obj.id_short + sm.id_short + str(self.relationships_counter)
                           # Create unique etags
                           next_etag = "etag" + str(self.relationships_counter)
                           # Generate the string for the next relationship.
                           # Note that the id for the the dtdl instance $dtid is the id-short
                        #    next_relationship += (f'{{"$relationshipId":"{next_rel_id}",'
                        #             f'"$sourceId":"{obj.id_short}",'
                        #             f'"$targetId":"{sm.id_short}",'
                        #             f'"$relationshipName":"submodel",'     # fixes for this type of relationship
                        #             f'"$etag":"W/\\"{next_etag}\\""}},\n')
                           self.allRelationships.append(self.create_next_instance_string("submodel", next_rel_id, obj.id_short, sm.id_short, next_etag))

        # Remove the last '\n' and ',' 
        next_relationship = next_relationship[:-2]
        # Close JSON Array
        next_relationship += ']'

        return next_relationship

    def create_next_instance_string(self, type, next_id, next_source, next_target, next_etag):

        return (f'{{"$relationshipId":"{next_id}",'
                                    f'"$sourceId":"{next_source}",'
                                    f'"$targetId":"{next_target}",'
                                    f'"$relationshipName":"{type}",'     # fixes for this type of relationship
                                    f'"$etag":"W/\\"{next_etag}\\""}},\n')

    def writeRelationshipFile(self, folder_name, rel_file_name):
            
        FILEPATH = os.getcwd()+"/AzureDTDLs/Rels/" + folder_name
                
        with open(FILEPATH+rel_file_name+".json", 'w') as f:
            for i, instance in enumerate(self.allRelationships):                
                    if i==0:
                        f.writelines("[")
                        f.writelines(instance)
                    elif i==len(self.allRelationships)-1:
                        f.writelines(instance[:-2])
                        f.writelines("]")
                    else:
                        f.writelines(instance)

    def __str__(self):
        '''
        Print info string when passed to print()
        '''
        return (f"Instance of TwinGraphRelationshipCreator\nVersion : {self.version}\nNum. Objects: {self.numObjects}\nCreated Rels.: {self.relationships_counter}")


def load_aas_data(package_name):
    # 1. Load the aasx package file
    # Create object and file stores for the AAS-Elements
    object_store: model.DictObjectStore[model.Identifiable] = model.DictObjectStore()
    file_store = basyx.aas.adapter.aasx.DictSupplementaryFileContainer()

    with basyx.aas.adapter.aasx.AASXReader(package_name) as reader:
        reader.read_into(object_store=object_store,
                        file_store=file_store)
        # new_meta_data = reader.get_core_properties()

    return object_store, file_store

def create_json(package_name_aas,title):
    object_store, file_store = load_aas_data(package_name=package_name_aas)
    if not os.path.exists(os.getcwd()+"/AzureDTDLs/"):
        os.makedirs(os.getcwd()+"/AzureDTDLs/")
    if not os.path.exists(os.getcwd()+"/AzureDTDLs/Instances"):
        os.makedirs(os.getcwd()+"/AzureDTDLs/Instances")
    if not os.path.exists(os.getcwd()+"/AzureDTDLs/Instances/"+str(title)):
        os.makedirs(os.getcwd()+"/AzureDTDLs/Instances/"+str(title))
    if not os.path.exists(os.getcwd()+"/AzureDTDLs/Rels"):
        os.makedirs(os.getcwd()+"/AzureDTDLs/Rels")
    if not os.path.exists(os.getcwd()+"/AzureDTDLs/Rels/"+str(title)):
        os.makedirs(os.getcwd()+"/AzureDTDLs/Rels/"+str(title))
            # Create the twin instances 
    dtdl_instance_creator = DTDLInstanceCreator(object_store)
    dtdl_instance_creator.createInstanceData(object_store)
    dtdl_instance_creator.writeInstanceFiles(str(title))

    # Create the relationships
    graph_creator = TwinGraphRelationshipCreator(object_store)
    graph_creator.generateRelationshipsData()
    graph_creator.writeRelationshipFile(str(title), "/"+str(title)+"Rels")
    print(file_store)





if __name__=="__main__":
    
    package_name1 = "aasCreations/01_FrankaEmika_Robot_Arm_AAS.aasx"
    package_name2 = "aasCreations/02_Storage_Zone_AAS.aasx"
    package_name3 = "aasCreations/03_myJoghurt_Products_AAS.aasx"
    package_name4 = "aasCreations/04_Linear_Guide_Axis_AAS.aasx"
    package_name5 = "aasCreations/05_Transport_Band_Conveyor_AAS.aasx"
    package_name6 = "aasCreations/06_Bottle_Switch_AAS.aasx"

create_json(package_name1,"FrankaRobot")
create_json(package_name2,"StorageZone")
create_json(package_name3,"myJoghurtProduct")
create_json(package_name4,"GuideAxis")
create_json(package_name5,"TransportConveyer")
create_json(package_name6,"Bottleswitch")