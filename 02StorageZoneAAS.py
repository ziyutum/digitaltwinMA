
from basyx.aas import model
from basyx.aas.adapter import aasx
import pyecma376_2 # Used for writing of .aasx package files




#---------------------------1.submodel: nameplate---------------------------------------------------------------------------------------
#---------------------------2.submodel: technical data---------------------------------------------------------------------------------------
#---------------------------3.submodel: capabilities--------------------------------------------
#---------------------------4.submodel: operation data --------------------------------------------
#---------------------------5.submodel: skills--------------------------------------------
#---------------------------6.submodel: components--------------------------------------------
#################################################################################################################################################
# Step 1: Setting up an SupplementaryFileContainer and AAS & Create ASSET and AAS
####################################################################################################################################################     
 
asset_identifier = model.Identifier(id_='https://tum.ais.de/Assets/StorageZone', 
                                        id_type=model.IdentifierType.IRI)

asset = model.Asset(kind=model.AssetKind.INSTANCE,
                        identification=asset_identifier)


aas_identifier = model.Identifier('https://tum.ais.de/AAS/StorageZone',
                                       model.IdentifierType.IRI)
aas = model.AssetAdministrationShell(identification=aas_identifier,
                                         asset=model.AASReference.from_referable(asset),
                                         id_short="StorageZone")

#####################################################################################################################################################
# Step 2: Setting up submodels for  AAS 
#########################################################################################################################################################
#------------1.submodel: nameplate--------------------------------------------

submodel_identifier_nameplate = model.Identifier('https://tum.ais.de/Submodels/Nameplate', model.IdentifierType.IRI)
submodel_nameplate = model.Submodel(identification=submodel_identifier_nameplate, id_short="Nameplate",kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))

# add properties to the submodel
nameplate_1= model.Property(id_short="ManufacturerName", value_type=model.datatypes.String, value="Festo")
nameplate_2 = model.Property(id_short="ManufacturerProductDesignation", value_type=model.datatypes.String, value="MyJoghurt Products Container Storage")
nameplate_3 = model.Property(id_short="CompanyName", value_type=model.datatypes.String, value="Festo SE & Co. KG")
nameplate_4 = model.Property(id_short="ProductCountryOfOrigin", value_type=model.datatypes.String, value="de")
nameplate_5 = model.Property(id_short="YearOfConstruction", value_type=model.datatypes.String, value="")
nameplate_6 = model.Property(id_short="SerialNo", value_type=model.datatypes.String, value="")

submodel_nameplate.submodel_element.add(nameplate_1)
submodel_nameplate.submodel_element.add(nameplate_2)
submodel_nameplate.submodel_element.add(nameplate_3)
submodel_nameplate.submodel_element.add(nameplate_4)
submodel_nameplate.submodel_element.add(nameplate_5)
submodel_nameplate.submodel_element.add(nameplate_6)

# add smc collections to the submodel, then add properties to this collection
smc_add = model.SubmodelElementCollectionOrdered(id_short="Address", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Countrycode", value_type=model.datatypes.String, value="de")
prop2 = model.Property(id_short="Street", value_type=model.datatypes.String, value="Ruiter Strasse 82")
prop3 = model.Property(id_short="Zip", value_type=model.datatypes.String, value="73734")
prop4 = model.Property(id_short="CityTown", value_type=model.datatypes.String, value="Esslingen am Neckar")
prop5 = model.Property(id_short="Statecity", value_type=model.datatypes.String, value="Baden-Württemberg")

smc_add.value.add(prop1)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
smc_add.value.add(prop4)
smc_add.value.add(prop5)

submodel_nameplate.submodel_element.add(smc_add)

# add smc collections to the submodel, then add properties to this collection
smc_add = model.SubmodelElementCollectionOrdered(id_short="Marking_CE", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="CEQualificationPresent", value_type=model.datatypes.Boolean, value=1)

smc_add.value.add(prop1)
submodel_nameplate.submodel_element.add(smc_add)


#------------2.submodel: technical data---------------------------------------------------------------------------------------

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/TechnicalData', model.IdentifierType.IRI)
submodel_2 = model.Submodel(identification=submodel_identifier_tec, id_short="TechnicalData", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_2))

# 1. base platform smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="BasePlatform", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Length", value_type=model.datatypes.String, value="2.62 m")
prop2 = model.Property(id_short="Width", value_type=model.datatypes.String, value="0.16 m")
prop3 = model.Property(id_short="Height", value_type=model.datatypes.String, value="0.06 m")
prop=[prop1,prop2,prop3]

for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

# 2. cell platform
smc_add = model.SubmodelElementCollectionOrdered(id_short="CellPlatform", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="NumberOfCells", value_type=model.datatypes.String, value="126")
prop2 = model.Property(id_short="Length", value_type=model.datatypes.String, value="2.60 m")
prop3 = model.Property(id_short="Width", value_type=model.datatypes.String, value="0.15 m")
prop4 = model.Property(id_short="Height", value_type=model.datatypes.String, value="0.02 m")
prop5 = model.Property(id_short="CellsDiameter", value_type=model.datatypes.String, value="45.00 mm")
prop6 = model.Property(id_short="CellsDepth", value_type=model.datatypes.String, value="10.00 mm")

prop=[prop1,prop2,prop3,prop4,prop5,prop6]

for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_son = model.SubmodelElementCollectionOrdered(id_short="Arrangement")

prop1 = model.Property(id_short="NumberOfRows", value_type=model.datatypes.String, value="3")
prop2 = model.Property(id_short="NumberOfCellsEachRow", value_type=model.datatypes.String, value="42")

prop=[prop1,prop2]
for i in prop:
        smc_son.value.add(i)

smc_add.value.add(smc_son)

#------------3.submodel: dimensional drawing---------------------------------------------------------------------------------------

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/DimensionDrawing', model.IdentifierType.IRI)
submodel_3 = model.Submodel(identification=submodel_identifier_tec, id_short="DimensionDrawing", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_3))

smc_add = model.File(id_short="Dimensions", kind=model.ModelingKind.INSTANCE, mime_type="application/pdf")
submodel_3.submodel_element.add(smc_add)

#------------4.submodel: GrooveCell---------------------------------------------------------------------------------------

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/GrooveCell', model.IdentifierType.IRI)
submodel_4 = model.Submodel(identification=submodel_identifier_tec, id_short="GrooveCell", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_4))

prop1 = model.Property(id_short="CellsDiameter", value_type=model.datatypes.String, value="45.00 mm")
prop2 = model.Property(id_short="CellsDepth", value_type=model.datatypes.String, value="10.00 mm")

prop=[prop1,prop2]
for i in prop:
        submodel_4.submodel_element.add(i)

smc_son = model.SubmodelElementCollectionOrdered(id_short=("CellStatus"))
submodel_4.submodel_element.add(smc_son)
property_1 = model.Property(id_short="HasJoghurtProduct", value_type=model.datatypes.String, value="")
property_2 = model.Property(id_short="InRow", value_type=model.datatypes.String, value="")
property_3 = model.Property(id_short="InColumn", value_type=model.datatypes.String, value="")
property_4 = model.Property(id_short="LocationX", value_type=model.datatypes.String, value="")
property_5 = model.Property(id_short="LocationY", value_type=model.datatypes.String, value="")
smc_son.value.add(property_1)
smc_son.value.add(property_2)
smc_son.value.add(property_3)
smc_son.value.add(property_4)
smc_son.value.add(property_5)
'''
#create smc collection and add it to the submodel
for i in range(127):
        smc_son = model.SubmodelElementCollectionOrdered(id_short=('Cell'+str(i+1)))
        submodel_4.submodel_element.add(smc_son)
        property_1 = model.Property(id_short="HasJoghurtProduct", value_type=model.datatypes.String, value="")
        property_2 = model.Property(id_short="InRow", value_type=model.datatypes.String, value="")
        property_3 = model.Property(id_short="InColumn", value_type=model.datatypes.String, value="")
        property_4 = model.Property(id_short="LocationX", value_type=model.datatypes.String, value="")
        property_5 = model.Property(id_short="LocationY", value_type=model.datatypes.String, value="")
        smc_son.value.add(property_1)
        smc_son.value.add(property_2)
        smc_son.value.add(property_3)
        smc_son.value.add(property_4)
        smc_son.value.add(property_5)
'''
#------------5.submodel: Components---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
submodel_5 = model.Submodel(identification=submodel_identifier_tec, id_short="Components", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_5))

# 1.  smc screw
smc_add = model.SubmodelElementCollectionOrdered(id_short="Screw", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Number", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Size", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_5.submodel_element.add(smc_add)
#2. base smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="Base")
prop = model.Property(id_short="Material", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_5.submodel_element.add(smc_add)
#3. cellplatform smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="CellPlatform")
prop = model.Property(id_short="Material", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_5.submodel_element.add(smc_add)












#---------------------------1.submodel: nameplate---------------------------------------------------------------------------------------
#---------------------------2.submodel: technical data---------------------------------------------------------------------------------------
#---------------------------3.submodel: dimensional drawing--------------------------------------------
#---------------------------4.submodel: groove cell --------------------------------------------
#---------------------------5.submodel: components--------------------------------------------

######################################################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2, submodel_3, submodel_4, submodel_5])
file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXWriter("02_Storage_Zone_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)

print('Finisched writing aasx file')