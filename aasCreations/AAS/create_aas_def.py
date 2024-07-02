from basyx.aas import model
from basyx.aas.adapter import aasx

######################################################################################################################################################
# the aas cration and the fiest 3 submodels have generality, so I made 4 functions here, in order to be used when generating the aasx files.
# if the prodicts are made by festo, the nameplate sunmodel can be used directly, otherwise, it would be add it correctly manually.
##################################################################################################################################################
def create_aas(name):

    asset_identifier = model.Identifier(id_='https://tum.ais.de/Assets/'+name, 
                                            id_type=model.IdentifierType.IRI)
    asset = model.Asset(kind=model.AssetKind.INSTANCE,
                            identification=asset_identifier)


    aas_identifier = model.Identifier('https://tum.ais.de/AAS/'+name,
                                        model.IdentifierType.IRI)
    aas = model.AssetAdministrationShell(identification=aas_identifier,
                                            asset=model.AASReference.from_referable(asset),
                                            id_short=name)
    return asset,aas,aas_identifier



def create_submodel1(product):
    submodel_identifier_nameplate = model.Identifier('https://tum.ais.de/Submodels/Nameplate', model.IdentifierType.IRI)
    submodel_nameplate = model.Submodel(identification=submodel_identifier_nameplate, 
    id_short="Nameplate", kind=model.ModelingKind.TEMPLATE)
    

    nameplate_1= model.Property(id_short="ManufacturerName", value_type=model.datatypes.String, value="Festo")
    nameplate_2 = model.Property(id_short="ManufacturerProductDesignation", value_type=model.datatypes.String, value=product)
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

    smc_add = model.SubmodelElementCollectionOrdered(id_short="Address")
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
    smc_add = model.SubmodelElementCollectionOrdered(id_short="Marking_CE", kind=model.ModelingKind.TEMPLATE)
    prop1 = model.Property(id_short="CEQualificationPresent", value_type=model.datatypes.Boolean, value=1)

    smc_add.value.add(prop1)
    submodel_nameplate.submodel_element.add(smc_add)
    return submodel_nameplate

def create_submodel2():

    submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/TechnicalData', model.IdentifierType.IRI)
    submodel_2 = model.Submodel(identification=submodel_identifier_tec, id_short="TechnicalData", kind=model.ModelingKind.TEMPLATE)
    return submodel_2

def create_submodel3():
    submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/DimensionDrawing', model.IdentifierType.IRI)
    submodel_3 = model.Submodel(identification=submodel_identifier_tec, id_short="DimensionDrawing", kind=model.ModelingKind.TEMPLATE)
    

    smc_add = model.File(id_short="Dimensions", kind=model.ModelingKind.INSTANCE, mime_type="application/pdf")
    submodel_3.submodel_element.add(smc_add)
    return submodel_3
  
