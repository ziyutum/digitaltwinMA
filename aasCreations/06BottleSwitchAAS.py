from basyx.aas import model
from basyx.aas.adapter import aasx
import create_aas_def 


##########################################################################################
asset,aas,aas_identifier =create_aas_def.create_aas('RotaryBottleSwitch')
########################################################################################
#----------------1. nameplate------------------------------------------------------------------
submodel_nameplate = create_aas_def.create_submodel1('Rotary Switch for MyJoghurt Product')
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))
#----------------2. technical data-----------------------------------------------------------------
submodel_2=create_aas_def.create_submodel2()
aas.submodel.add(model.AASReference.from_referable(submodel_2))
prop1 = model.Property(id_short="Switch_Model", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Switch_Shape", value_type=model.datatypes.String, value="Cylinder")
prop3 = model.Property(id_short="Switch_Diameter", value_type=model.datatypes.String, value="145 mm")
prop4 = model.Property(id_short="Switch_Height", value_type=model.datatypes.String, value="35 mm")
prop5 = model.Property(id_short="Switch_Material", value_type=model.datatypes.String, value="")
prop6 = model.Property(id_short="Switch_BottleCapacity", value_type=model.datatypes.String, value="1")
prop7 = model.Property(id_short="Switch_BottleHoleDiameter", value_type=model.datatypes.String, value="45 mm")

prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7]
for i in prop:
        submodel_2.submodel_element.add(i)
#----------------3. dimension drawing-----------------------------------------------------------------
submodel_3=create_aas_def.create_submodel3()
aas.submodel.add(model.AASReference.from_referable(submodel_3))
#----------------4. capability-----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Capabilities', model.IdentifierType.IRI)
submodel_4 = model.Submodel(identification=submodel_identifier_tec, id_short="Switch_Capabilities", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_4))
smc_add = model.SubmodelElementCollectionOrdered(id_short="SwitchRotation", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="SwitchRotationSpeed", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="SwitchRotationDirection", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch_Positioning", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="FromBelt", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="ToBelt", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_4.submodel_element.add(smc_add)
#----------------5. skills----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Skills', model.IdentifierType.IRI)
submodel_5 = model.Submodel(identification=submodel_identifier_tec, id_short="Skills", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_5))

smc_add = model.SubmodelElementCollectionOrdered(id_short="SwitchMyJoghurtProduct", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Switch_RotationSpeed", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Switch_FeedAmountEachTime", value_type=model.datatypes.String, value="1")
prop3 = model.Property(id_short="Switch_RotationDirection", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Switch_RotationAngle", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
smc_add.value.add(prop4)
submodel_5.submodel_element.add(smc_add)
#------------6.submodel: Components---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
submodel_6 = model.Submodel(identification=submodel_identifier_tec, id_short="Components", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_6))
smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Switch_Number", value_type=model.datatypes.String, value="3")
prop2 = model.Property(id_short="Switch_Model", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
ent1 = model.Entity(id_short="Switch_CoverCap", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent2 = model.Entity(id_short="Switch_Profile", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent3 = model.Entity(id_short="Switch_SupportBase", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent=[ent1,ent2,ent3]
for i in ent:
        smc_add.value.add(i)
submodel_6.submodel_element.add(smc_add)

smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch_Motor", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="SwitchMotorModel", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_6.submodel_element.add(smc_add)

#------------7.submodel: SwitchOperationData---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/SwitchOperationData', model.IdentifierType.IRI)
submodel_7 = model.Submodel(identification=submodel_identifier_tec, id_short="SwitchOperationData", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_7))
smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch1", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Switch1_Angle", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_7.submodel_element.add(smc_add)

smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch2", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Switch2_Angle", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_7.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Switch3", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Switch3_Angle", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_7.submodel_element.add(smc_add)
#######################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2,submodel_3,submodel_4,submodel_5,submodel_6,submodel_7])
file_store = aasx.DictSupplementaryFileContainer()
with aasx.AASXWriter("06_Bottle_Switch_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)
