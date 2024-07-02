from basyx.aas import model
from basyx.aas.adapter import aasx
import create_aas_def 


##########################################################################################
asset,aas,aas_identifier =create_aas_def.create_aas('LinearGuideAxis')
########################################################################################
#----------------1. nameplate------------------------------------------------------------------
submodel_nameplate = create_aas_def.create_submodel1('Guide Axis')
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))
#----------------2. technical data-----------------------------------------------------------------
submodel_2=create_aas_def.create_submodel2()
aas.submodel.add(model.AASReference.from_referable(submodel_2))

# 1. FDG smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="PassiveGuideAxis", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Model", value_type=model.datatypes.String, value="FDG-40-2500-ZR-KF-GV")
prop2 = model.Property(id_short="Size", value_type=model.datatypes.String, value="40")
prop3 = model.Property(id_short="Stroke", value_type=model.datatypes.String, value="2500 mm")
prop4 = model.Property(id_short="AssemblyPosition", value_type=model.datatypes.String, value="Any")
prop5 = model.Property(id_short="Guide", value_type=model.datatypes.String, value="Recirculating ball bearing guide")
prop6 = model.Property(id_short="DesignStructure", value_type=model.datatypes.String, value="Guide axis without drive unit")
prop7 = model.Property(id_short="MaxSpeed", value_type=model.datatypes.String, value="3 m/s")
prop8 = model.Property(id_short="CorrosionResistance", value_type=model.datatypes.String, value="0 - No corrosion stress")
prop9 = model.Property(id_short="MaterialNote", value_type=model.datatypes.String, value="Free of copper and PTFE")
prop10 = model.Property(id_short="MaterialGuideComponent", value_type=model.datatypes.String, value="Steel")
prop11 = model.Property(id_short="MaterialHousing", value_type=model.datatypes.String, value="Wrought Aluminium alloy Anodised")
prop12 = model.Property(id_short="Slide", value_type=model.datatypes.String, value="Extended slide")
prop13 = model.Property(id_short="Conjugation", value_type=model.datatypes.String, value="For toothed belt axis")
prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9,prop10,prop11,prop12,prop13]
for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

# 2. DGE smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="ElectromechanicalLinearActuator", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Model", value_type=model.datatypes.String, value="DGE-40-2500-ZR-LK-RV-KG-KF-GV")
prop2 = model.Property(id_short="Size", value_type=model.datatypes.String, value="40")
prop3 = model.Property(id_short="Stroke", value_type=model.datatypes.String, value="2500 mm")
prop4 = model.Property(id_short="AssemblyPosition", value_type=model.datatypes.String, value="Any")
prop5 = model.Property(id_short="Guide", value_type=model.datatypes.String, value="Recirculating ball bearing guide")
prop6 = model.Property(id_short="DesignStructure", value_type=model.datatypes.String, value="Electric linear axis")
prop7 = model.Property(id_short="MaxSpeed", value_type=model.datatypes.String, value="3 m/s")
prop8 = model.Property(id_short="EffectiveDiameterDrivePinion", value_type=model.datatypes.String, value="39.79 mm")
prop9 = model.Property(id_short="ToothedStretch", value_type=model.datatypes.String, value="0.11 %")
prop10 = model.Property(id_short="ToothedPitch", value_type=model.datatypes.String, value="5 mm")
prop11 = model.Property(id_short="MotorType", value_type=model.datatypes.String, value="Servomotor")
prop12 = model.Property(id_short="Repetition", value_type=model.datatypes.String, value="±0.1")
prop13 = model.Property(id_short="FeedForce", value_type=model.datatypes.String, value="610 N")
prop14 = model.Property(id_short="ForceFy", value_type=model.datatypes.String, value="7300 N")
prop15 = model.Property(id_short="ForceFz", value_type=model.datatypes.String, value="7300 N")
prop16 = model.Property(id_short="TorqueMx", value_type=model.datatypes.String, value="170 Nm")
prop17 = model.Property(id_short="TorqueMy", value_type=model.datatypes.String, value="660 Nm")
prop18 = model.Property(id_short="TorqueMz", value_type=model.datatypes.String, value="660 Nm")
prop19 = model.Property(id_short="DriveFunction", value_type=model.datatypes.String, value="Toothed Belt")
prop20 = model.Property(id_short="DriveShaftLeft", value_type=model.datatypes.String, value="None on left")
prop21 = model.Property(id_short="DriveShaftRight", value_type=model.datatypes.String, value="on right front")
prop22 = model.Property(id_short="Slide", value_type=model.datatypes.String, value="Extended slide")
prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9,prop10,prop11,prop12,prop13,prop14,prop15,prop16,prop17,prop18,prop19,prop20,prop21,prop22]
for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

# add smc collections to the submodel, then add properties to this collection
smc_add = model.SubmodelElementCollectionOrdered(id_short="Material", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="ReturnPulleyHousing", value_type=model.datatypes.String, value="Anodised aluminium")
prop2 = model.Property(id_short="CoverStrip", value_type=model.datatypes.String, value="Corrosion resistant steel")
prop3 = model.Property(id_short="ToothedBelt", value_type=model.datatypes.String, value="Polychloroprene with Glascord and nylon coating")
prop4 = model.Property(id_short="Profile", value_type=model.datatypes.String, value="Anodised aluminium")
prop5 = model.Property(id_short="Slide", value_type=model.datatypes.String, value="Anodised aluminium")
prop6 = model.Property(id_short="DriveHousing", value_type=model.datatypes.String, value="Anodised aluminium")
smc_add.value.add(prop1)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
smc_add.value.add(prop4)
smc_add.value.add(prop5)
smc_add.value.add(prop6)
submodel_2.submodel_element.add(smc_add)
#----------------3. dimension drawing-----------------------------------------------------------------
submodel_3=create_aas_def.create_submodel3()
aas.submodel.add(model.AASReference.from_referable(submodel_3))
#----------------4. capability-----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Capabilities', model.IdentifierType.IRI)
submodel_4 = model.Submodel(identification=submodel_identifier_tec, id_short="Capabilities", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_4))

smc_add = model.SubmodelElementCollectionOrdered(id_short="Guide", kind=model.ModelingKind.INSTANCE)
prop = model.Property(id_short="Type", value_type=model.datatypes.String, value="Recirculating ball bearing guide")
smc_add.value.add(prop)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Motion", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Direction", value_type=model.datatypes.String, value="linear")
prop2 = model.Property(id_short="MaxSpeed", value_type=model.datatypes.String, value="3 m/s")
prop3 = model.Property(id_short="MaxAcceleration", value_type=model.datatypes.String, value="50 m/s2")
smc_add.value.add(prop)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="LoadBearing", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="MaxLoad", value_type=model.datatypes.String, value="50 kg")
smc_add.value.add(prop)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Positioning", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="Accuracy", value_type=model.datatypes.String, value="±0.1")
smc_add.value.add(prop)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Adaption", kind=model.ModelingKind.TEMPLATE)
prop = model.Property(id_short="ChoiceOfMounting", value_type=model.datatypes.String, value="wide")
prop2 = model.Property(id_short="RangeForDriveUnits", value_type=model.datatypes.String, value="wide")
smc_add.value.add(prop)
smc_add.value.add(prop2)
submodel_4.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="MechanicalOperation", kind=model.ModelingKind.TEMPLATE)
smc_son = model.SubmodelElementCollectionOrdered(id_short="MaxForce")
smc_add.value.add(smc_son)
prop1 = model.Property(id_short="Fy", value_type=model.datatypes.String, value="7300 N")
prop2 = model.Property(id_short="Fz", value_type=model.datatypes.String, value="7300 N")
prop=[prop1,prop2]
for i in prop:
        smc_son.value.add(i)
smc_son = model.SubmodelElementCollectionOrdered(id_short="MaxTorques")
smc_add.value.add(smc_son)
prop1 = model.Property(id_short="My", value_type=model.datatypes.String, value="330 Nm")
prop2 = model.Property(id_short="Mz", value_type=model.datatypes.String, value="330 Nm")
prop = model.Property(id_short="Mx", value_type=model.datatypes.String, value="170 Nm")

prop=[prop, prop1,prop2]
for i in prop:
        smc_son.value.add(i)
submodel_4.submodel_element.add(smc_add)



#----------------5. component-----------------------------------------------------------------
submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
submodel_5 = model.Submodel(identification=submodel_identifier_tec, id_short="Components", kind=model.ModelingKind.INSTANCE)
aas.submodel.add(model.AASReference.from_referable(submodel_5))

# 1.  smc fdg
smc_add = model.SubmodelElementCollectionOrdered(id_short="PassiveGuideAxis", kind=model.ModelingKind.INSTANCE)
ent1 = model.Entity(id_short="GuideAxis", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent2 = model.Entity(id_short="EmergencyBuffer", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent3 = model.Entity(id_short="ShockAbsorberKits", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent4 = model.Entity(id_short="SwitchingLug", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent5 = model.Entity(id_short="SensorBracket", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent6 = model.Entity(id_short="ProximitySensors", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent7 = model.Entity(id_short="CableWithSocket", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent8 = model.Entity(id_short="SlotNutforSlide", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent9 = model.Entity(id_short="CentringSleeve", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent10 = model.Entity(id_short="SlotCover", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent11 = model.Entity(id_short="NutForMounting", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent12 = model.Entity(id_short="CentralSupport", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent13 = model.Entity(id_short="FootMounting", entity_type=model.EntityType.CO_MANAGED_ENTITY)

ent=[ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12,ent13]
for i in ent:
        smc_add.value.add(i)
submodel_5.submodel_element.add(smc_add)

# 2.  smc dge
smc_add = model.SubmodelElementCollectionOrdered(id_short="ElectromechanicalLinearActuator", kind=model.ModelingKind.INSTANCE)
ent1 = model.Entity(id_short="ToothedBeltAxis", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent2 = model.Entity(id_short="AxialKit", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent3 = model.Entity(id_short="Motor", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent4 = model.Entity(id_short="SlotCover", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent5 = model.Entity(id_short="ProximitySensor", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent6 = model.Entity(id_short="CableWithSocket", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent7 = model.Entity(id_short="NutForMounting", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent8 = model.Entity(id_short="CentralSupport", entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent9 = model.Entity(id_short="FootMounting", entity_type=model.EntityType.CO_MANAGED_ENTITY)

ent=[ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9]
for i in ent:
        smc_add.value.add(i)
submodel_5.submodel_element.add(smc_add)




#######################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2,submodel_3,submodel_4,submodel_5])
file_store = aasx.DictSupplementaryFileContainer()
with aasx.AASXWriter("04_Linear_Guide_Axis_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)
