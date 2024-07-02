
from basyx.aas import model
from basyx.aas.adapter import aasx
import pyecma376_2 # Used for writing of .aasx package files





    
 
asset_identifier = model.Identifier(id_='https://tum.ais.de/Assets/MyJoghurtProduct', 
                                        id_type=model.IdentifierType.IRI)

asset = model.Asset(kind=model.AssetKind.INSTANCE,
                        identification=asset_identifier)


aas_identifier = model.Identifier('https://tum.ais.de/AAS/MyJoghurtProduct',
                                       model.IdentifierType.IRI)
aas = model.AssetAdministrationShell(identification=aas_identifier,
                                         asset=model.AASReference.from_referable(asset),
                                         id_short="MyJoghurtProduct")



#------------1.submodel: nameplate---------------------------------------------------------------------------------------------
submodel_identifier_nameplate = model.Identifier('https://tum.ais.de/Submodels/Nameplate', model.IdentifierType.IRI)
submodel_nameplate = model.Submodel(identification=submodel_identifier_nameplate, 
id_short="Nameplate",kind=model.ModelingKind.TEMPLATE)
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

#--------------2.submodel: technical data------------------------------------------------------------------------#

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/TechnicalData', model.IdentifierType.IRI)
submodel_2 = model.Submodel(identification=submodel_identifier_tec, 
id_short="TechnicalData",kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_2))

# 1. yoghurt container smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="MyJoghurtProductContainer", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Material", value_type=model.datatypes.String, value="glass")
prop2 = model.Property(id_short="Mouth", value_type=model.datatypes.String, value="wide")
prop3 = model.Property(id_short="Capability", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Height", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="MouthSize", value_type=model.datatypes.String, value="")
prop6 = model.Property(id_short="OuterDiameter", value_type=model.datatypes.String, value="")
prop7 = model.Property(id_short="NeckOuterDiameter", value_type=model.datatypes.String, value="")
prop8 = model.Property(id_short="Weight", value_type=model.datatypes.String, value="")


prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8]

for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add) 

#------------3.submodel: dimensional drawing---------------------------------------------------------------------------------------

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/DimensionDrawing', model.IdentifierType.IRI)
submodel_3 = model.Submodel(identification=submodel_identifier_tec, id_short="DimensionDrawing", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_3))

smc_add = model.File(id_short="Dimensions", kind=model.ModelingKind.INSTANCE, mime_type="application/pdf")
submodel_3.submodel_element.add(smc_add)

#------------4.submodel: status---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Status', model.IdentifierType.IRI)
submodel_4 = model.Submodel(identification=submodel_identifier_tec, id_short="Status", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_4))

prop1 = model.Property(id_short="Barcode", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="HasClosure", value_type=model.datatypes.String, value="no")
prop3 = model.Property(id_short="IsEmpty", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="InCellID", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="FillingMaterial", value_type=model.datatypes.String, value="")
prop6 = model.Property(id_short="FillingAmount", value_type=model.datatypes.String, value="")
prop7 = model.Property(id_short="StorageTemperature", value_type=model.datatypes.String, value="")
prop8 = model.Property(id_short="ProductionDate", value_type=model.datatypes.String, value="")
prop9 = model.Property(id_short="ExpirationDate", value_type=model.datatypes.String, value="")


prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9]
for i in prop:
        submodel_4.submodel_element.add(i)

# 1.  smc ingredient
smc_add = model.SubmodelElementCollectionOrdered(id_short="Ingredients", kind=model.ModelingKind.INSTANCE)
prop1 = model.Property(id_short="Milk", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Strawberry", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Chocolate", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Honey", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="Caramel", value_type=model.datatypes.String, value="")

prop=[prop1,prop2,prop3,prop4,prop5]
for i in prop:
        smc_add.value.add(i)
submodel_4.submodel_element.add(smc_add)
#------------5.submodel: status---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/QualityControl', model.IdentifierType.IRI)
submodel_5 = model.Submodel(identification=submodel_identifier_tec, id_short="QualityControl", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_5))

prop1 = model.Property(id_short="QualityInspectionResult", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="InspectionDate", value_type=model.datatypes.String, value="no")
prop3 = model.Property(id_short="Inspector", value_type=model.datatypes.String, value="")

prop=[prop1,prop2,prop3]
for i in prop:
        submodel_5.submodel_element.add(i)

#------------6.submodel: sale information---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/MaketingInformation', model.IdentifierType.IRI)
submodel_6 = model.Submodel(identification=submodel_identifier_tec, id_short="MaketingInformation", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_6))

prop1 = model.Property(id_short="SaleDate", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="SaleLocation", value_type=model.datatypes.String, value="no")
prop3 = model.Property(id_short="SalesChannel", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="SalePrice", value_type=model.datatypes.String, value="")

prop=[prop1,prop2,prop3,prop4]
for i in prop:
        submodel_6.submodel_element.add(i)

#------------7.submodel: monitoring information---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/MonitoringInformation', model.IdentifierType.IRI)
submodel_7 = model.Submodel(identification=submodel_identifier_tec, id_short="MonitoringInformation", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_7))

prop1 = model.Property(id_short="MonitoringDate", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="MonitoringLocation", value_type=model.datatypes.String, value="no")

prop=[prop1,prop2]
for i in prop:
        submodel_7.submodel_element.add(i)
# 1.  smc ingredient
smc_add = model.SubmodelElementCollectionOrdered(id_short="EnvironmentalMonitoringData", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Temperature", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Humidity", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Sanitation", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="WaterQuality", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="AirQuality", value_type=model.datatypes.String, value="")

prop=[prop1,prop2,prop3,prop4,prop5]
for i in prop:
        smc_add.value.add(i)
submodel_7.submodel_element.add(smc_add)

#------------8.submodel: Components---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
submodel_8 = model.Submodel(identification=submodel_identifier_tec, id_short="Components", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_8))

# 1.  smc bottle
smc_add = model.SubmodelElementCollectionOrdered(id_short="BottleContainer", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Number", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Capability", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_8.submodel_element.add(smc_add)
#2.  smc  yogurt
smc_add = model.SubmodelElementCollectionOrdered(id_short="myJoghurtProduct")
prop = model.Property(id_short="Flavor", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_8.submodel_element.add(smc_add)


#################################################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2, submodel_3,submodel_4,submodel_5,submodel_6,submodel_7,submodel_8])
file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXWriter("03_myJoghurt_Products_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)




