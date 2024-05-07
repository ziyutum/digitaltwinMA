
from basyx.aas import model
from basyx.aas.adapter import aasx
import pyecma376_2 # Used for writing of .aasx package files





#########################################################################################
# Step 1: Setting up an SupplementaryFileContainer and AAS & Create ASSET and AAS
#########################################################################################   
     
asset_identifier = model.Identifier(id_='https://tum.ais.de/Assets/MyJoghurtProduct', 
                                        id_type=model.IdentifierType.IRI)

asset = model.Asset(kind=model.AssetKind.INSTANCE,
                        identification=asset_identifier)


aas_identifier = model.Identifier('https://tum.ais.de/AAS/MyJoghurtProduct',
                                       model.IdentifierType.IRI)
aas = model.AssetAdministrationShell(identification=aas_identifier,
                                         asset=model.AASReference.from_referable(asset),
                                         id_short="MyJoghurtProduct")



#########################################################################################
# Step 2: Setting up submodels for  AAS 
#########################################################################################
#------------1.submodel: nameplate--------------------------------------------



submodel_identifier_nameplate = model.Identifier('https://tum.ais.de/Submodels/Nameplate', model.IdentifierType.IRI)
submodel_nameplate = model.Submodel(identification=submodel_identifier_nameplate, 
id_short="Nameplate")
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))




nameplate_1= model.Property(id_short="ManufacturerName", value_type=model.datatypes.String, value="tum")
nameplate_2 = model.Property(id_short="ManufacturerProductDesignation", value_type=model.datatypes.String, value="myJoghurt Products")
nameplate_3 = model.Property(id_short="ProductCountryOfOrigin", value_type=model.datatypes.String, value="de")
nameplate_4 = model.Property(id_short="YearOfConstruction", value_type=model.datatypes.String, value="")
submodel_nameplate.submodel_element.add(nameplate_1)
submodel_nameplate.submodel_element.add(nameplate_2)
submodel_nameplate.submodel_element.add(nameplate_3)
submodel_nameplate.submodel_element.add(nameplate_4)

smc_add = model.SubmodelElementCollectionOrdered(id_short="Address")
prop1 = model.Property(id_short="Countrycode", value_type=model.datatypes.String, value="de")
prop2 = model.Property(id_short="Street", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Zip", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="CityTown", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="Statecity", value_type=model.datatypes.String, value="")

smc_add.value.add(prop1)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
smc_add.value.add(prop4)
smc_add.value.add(prop5)

submodel_nameplate.submodel_element.add(smc_add)

#---------------2---------------------------------------------------------------------------------#

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/TechnicalData', model.IdentifierType.IRI)
submodel_2 = model.Submodel(identification=submodel_identifier_tec, 
id_short="TechnicalData")
aas.submodel.add(model.AASReference.from_referable(submodel_2))






object_store = model.DictObjectStore([aas, submodel_2, submodel_nameplate])
file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXWriter("01_FrankaEmika_Robot_Arm_AAS66666.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)




