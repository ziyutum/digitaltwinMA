from basyx.aas import model
from basyx.aas.adapter import aasx
import create_aas_def 

#modul 8032692,8033135
##########################################################################################
asset,aas,aas_identifier =create_aas_def.create_aas('TransportConveyor')
########################################################################################
#----------------1. nameplate------------------------------------------------------------------
submodel_nameplate = create_aas_def.create_submodel1('Conveyor module')
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))
#----------------2. technical data-----------------------------------------------------------------
submodel_2=create_aas_def.create_submodel2()
aas.submodel.add(model.AASReference.from_referable(submodel_2))
prop1 = model.Property(id_short="Conveyor_OperatingVoltage", value_type=model.datatypes.String, value="24 V DC")
prop2 = model.Property(id_short="Conveyor_ElectricalConnection", value_type=model.datatypes.String, value="15-pin D-Sub HD (3 rows) ")
prop3 = model.Property(id_short="Conveyor_Dimensions", value_type=model.datatypes.String, value="350 mm x 170 mm x 140 mm  ")
submodel_2.submodel_element.add(prop3)
submodel_2.submodel_element.add(prop1)
submodel_2.submodel_element.add(prop2)
smc_add = model.SubmodelElementCollectionOrdered(id_short="MiniDigitalTerminal", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="ConveyorDigitalTerminal_Inputs", value_type=model.datatypes.String, value="Max. 24 V DC")
prop2 = model.Property(id_short="ConveyorDigitalTerminal_Outputs", value_type=model.datatypes.String, value="Max. 2 A per output")
prop3 = model.Property(id_short="ConveyorDigitalTerminal_Mini_4DI_4DO", value_type=model.datatypes.String, value="Max. 4 A total")
prop=[prop1,prop2,prop3]
for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="MiniAnalogueTerminal", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="ConveyorAnalogueTerminal_Inputs", value_type=model.datatypes.String, value="0 to 10 V DC ")
prop2 = model.Property(id_short="ConveyorAnalogueTerminal_Outputs", value_type=model.datatypes.String, value="± 10 V DC ")
prop3 = model.Property(id_short="ConveyorAnalogueTerminal_Mini_2DI_1DO", value_type=model.datatypes.String, value="")
prop=[prop1,prop2,prop3]
for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ConveyorSensors", kind=model.ModelingKind.TEMPLATE)
smc_son = model.SubmodelElementCollectionOrdered(id_short="ConveyorSensor1", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="ConveyorSensorType", value_type=model.datatypes.String, value="Through-beam sensor ")
prop2 = model.Property(id_short="ConveyorSensorNumber", value_type=model.datatypes.String, value="1 ")
prop=[prop1,prop2]
for i in prop:
        smc_son.value.add(i)
smc_add.value.add(smc_son)
smc_son = model.SubmodelElementCollectionOrdered(id_short="ConveyorSensor2", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="SensorType", value_type=model.datatypes.String, value="Diffuse sensor  ")
prop2 = model.Property(id_short="SensorNumber", value_type=model.datatypes.String, value="2 ")
prop=[prop1,prop2]
for i in prop:
        smc_son.value.add(i)
smc_add.value.add(smc_son)
submodel_2.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ConveyorMotor", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="ConveyorMotor_NominalVoltage", value_type=model.datatypes.String, value="24 V DC ")
prop2 = model.Property(id_short="ConveyorMotor_NominalCurrent", value_type=model.datatypes.String, value="1.5 A")
prop3 = model.Property(id_short="ConveyorMotor_NominalSpeed_DriveShaft", value_type=model.datatypes.String, value="65 r.p.m.")
prop4 = model.Property(id_short="ConveyorMotor_ReductionStages", value_type=model.datatypes.String, value="1")
prop5 = model.Property(id_short="ConveyorMotor_NominalTorque", value_type=model.datatypes.String, value="1 Nm")
prop6 = model.Property(id_short="ConveyorMotor_Reversible", value_type=model.datatypes.Boolean, value=1)
prop7 = model.Property(id_short="ConveyorMotor_StartingTorque", value_type=model.datatypes.String, value="7 Nm")
prop8 = model.Property(id_short="ConveyorMotor_Connection", value_type=model.datatypes.String, value="2 flat pins ")
prop9 = model.Property(id_short="ConveyorMotor_Weight", value_type=model.datatypes.String, value="450 g")
prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9]
for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)
#----------------3. dimension drawing-----------------------------------------------------------------
submodel_3=create_aas_def.create_submodel3()
aas.submodel.add(model.AASReference.from_referable(submodel_3))
#----------------4. capability-----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Capabilities', model.IdentifierType.IRI)
submodel_4 = model.Submodel(identification=submodel_identifier_tec, id_short="ConveyorCapabilities", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_4))

smc_add = model.SubmodelElementCollectionOrdered(id_short="TransportCapabilty", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="TransportDirection", value_type=model.datatypes.String, value="linear")
prop2 = model.Property(id_short="TransportMaxSpeed", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="TransportMaxAcceleration", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ControlSupplyCapabilty", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Supply_MaxCapability", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Supply_FeedSeperator", value_type=model.datatypes.String, value="1 each time")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ReadingInformationCapabilty", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Conveyor_CodeScanner", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="InformationReadTime", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Conveyor_ScannerSerial", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ObjectDetectionCapabilty", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="IsOnConveyer", value_type=model.datatypes.String, value="")
submodel_4.submodel_element.add(smc_add)
#----------------5. skills----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Skills', model.IdentifierType.IRI)
submodel_5 = model.Submodel(identification=submodel_identifier_tec, id_short="Skills", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_5))

smc_add = model.SubmodelElementCollectionOrdered(id_short="TransportMyJoghurtProduct", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Conveyor_Speed", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_5.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="SeperateMyJoghurtProduct", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Conveyor_FeedAmount", value_type=model.datatypes.String, value="1")
smc_add.value.add(prop)
submodel_5.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="ScanningMyJoghurtProductBarcode", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="MyJoghurtProductCode", value_type=model.datatypes.String, value="")
smc_add.value.add(prop)
submodel_5.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="DetectMyJoghurtProduct", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="ProductIsOnConveyer", value_type=model.datatypes.String, value="")
submodel_5.submodel_element.add(smc_add)

#------------6.submodel: Components---------------------------------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
submodel_6 = model.Submodel(identification=submodel_identifier_tec, id_short="ConveyorComponents", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_6))
# 1.  smc conveyor
smc_add = model.SubmodelElementCollectionOrdered(id_short="TransportConveyor", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="ConveyorNumber", value_type=model.datatypes.String, value="4")
prop2 = model.Property(id_short="ConveyorModel", value_type=model.datatypes.String, value="8032692/8033135")
smc_add.value.add(prop)
smc_add.value.add(prop2)
ent1 = model.Entity(id_short="Conveyor_DriveHead", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent2 = model.Entity(id_short="Conveyor_DeflectionHead", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent3 = model.Entity(id_short="Conveyor_SupportFoot", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent4 = model.Entity(id_short="Conveyor_GuardrailHolder", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent5 = model.Entity(id_short="Conveyor_Profile_IPM_PN", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent6 = model.Entity(id_short="Conveyor_GuardrailProfile", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent7 = model.Entity(id_short="Conveyor_ConveyorBelt", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent8 = model.Entity(id_short="Conveyor_CoverCap", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent=[ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8]
for i in ent:
        smc_add.value.add(i)
submodel_6.submodel_element.add(smc_add)

smc_add = model.SubmodelElementCollectionOrdered(id_short="Motor", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="ConveyorMotor_Model", value_type=model.datatypes.String, value="374134")
smc_add.value.add(prop)
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Through_Beam_Sensor", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="TBS_NumberInEachModule", value_type=model.datatypes.String, value="1")
smc_add.value.add(prop)
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Diffuse_Sensor", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="DS_NumberInEachModule", value_type=model.datatypes.String, value="2")
smc_add.value.add(prop)
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="BarcodeScanner", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="BarcodeScannerNumber", value_type=model.datatypes.String, value="2")
smc_add.value.add(prop)
submodel_6.submodel_element.add(smc_add)


#######################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2,submodel_3,submodel_4,submodel_5,submodel_6])
file_store = aasx.DictSupplementaryFileContainer()
with aasx.AASXWriter("05_Transport_Band_Conveyor_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)
