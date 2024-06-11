
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
 
asset_identifier = model.Identifier(id_='https://tum.ais.de/Assets/FrankaRobot', 
                                        id_type=model.IdentifierType.IRI)

asset = model.Asset(kind=model.AssetKind.INSTANCE,
                        identification=asset_identifier)


aas_identifier = model.Identifier('https://tum.ais.de/AAS/FrankaRobot',
                                       model.IdentifierType.IRI)
aas = model.AssetAdministrationShell(identification=aas_identifier,
                                         asset=model.AASReference.from_referable(asset),
                                         id_short="FrankaRobot")



#####################################################################################################################################################
# Step 2: Setting up submodels for  AAS 
#########################################################################################################################################################
#------------1.submodel: nameplate--------------------------------------------

submodel_identifier_nameplate = model.Identifier('https://tum.ais.de/Submodels/Nameplate', model.IdentifierType.IRI)
submodel_nameplate = model.Submodel(identification=submodel_identifier_nameplate, id_short="Nameplate",kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_nameplate))

# add properties to the submodel
nameplate_1= model.Property(id_short="ManufacturerName", value_type=model.datatypes.String, value="Franka Emika")
nameplate_2 = model.Property(id_short="ManufacturerProductDesignation", value_type=model.datatypes.String, value="research robot arm")
nameplate_3 = model.Property(id_short="CompanyName", value_type=model.datatypes.String, value="Franka Emika GmbH")
nameplate_4 = model.Property(id_short="ProductCountryOfOrigin", value_type=model.datatypes.String, value="de")
nameplate_5 = model.Property(id_short="YearOfConstruction", value_type=model.datatypes.String, value="2021")
submodel_nameplate.submodel_element.add(nameplate_1)
submodel_nameplate.submodel_element.add(nameplate_2)
submodel_nameplate.submodel_element.add(nameplate_3)
submodel_nameplate.submodel_element.add(nameplate_4)
submodel_nameplate.submodel_element.add(nameplate_5)

# add smc collections to the submodel, then add properties to this collection
smc_add = model.SubmodelElementCollectionOrdered(id_short="Address", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Countrycode", value_type=model.datatypes.String, value="de")
prop2 = model.Property(id_short="Street", value_type=model.datatypes.String, value="Frei-Otto-Strasse 20")
prop3 = model.Property(id_short="Zip", value_type=model.datatypes.String, value="80797")
prop4 = model.Property(id_short="CityTown", value_type=model.datatypes.String, value="Munich")
prop5 = model.Property(id_short="Statecity", value_type=model.datatypes.String, value="Bayern")

smc_add.value.add(prop1)
smc_add.value.add(prop2)
smc_add.value.add(prop3)
smc_add.value.add(prop4)
smc_add.value.add(prop5)

submodel_nameplate.submodel_element.add(smc_add)

#------------2.submodel: technical data---------------------------------------------------------------------------------------

submodel_identifier_tec = model.Identifier('https://tum.ais.de/Submodels/TechnicalData', model.IdentifierType.IRI)
submodel_2 = model.Submodel(identification=submodel_identifier_tec, id_short="TechnicalData", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_2))

# 1.smc robor arm
smc_add = model.SubmodelElementCollectionOrdered(id_short="RobotArm", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="RobotDegreesOfFreedome", value_type=model.datatypes.String, value="7")
prop2 = model.Property(id_short="RobotPayload", value_type=model.datatypes.String, value="3 kg")
prop3 = model.Property(id_short="RobotSensitivities", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="RobotMaximunReach", value_type=model.datatypes.String, value="855 mm")
prop5 = model.Property(id_short="RobotMaximumCartesianVelocity", value_type=model.datatypes.String, value="2 m/s")
prop6 = model.Property(id_short="RobotRepeatability", value_type=model.datatypes.String, value="+/- 0.1 mm")
prop7 = model.Property(id_short="RobotMountingFlange", value_type=model.datatypes.String, value="DIN ISO 9409-1-A50")
prop8 = model.Property(id_short="RobotInstallationPosition", value_type=model.datatypes.String, value="upright")
prop9 = model.Property(id_short="RobotMaximumWeight", value_type=model.datatypes.String, value="18 kg")
prop10 = model.Property(id_short="RobotProtectionRating", value_type=model.datatypes.String, value="IP 30")
prop11= model.Property(id_short="RobotTypicalAmbientTemperature", value_type=model.datatypes.String, value="+15/+25 degree celsius")
prop12= model.Property(id_short="RobotExtendedAmbientTemperature", value_type=model.datatypes.String, value="+5/+45 degree celsius")


prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8,prop9,prop10,prop11,prop12]

for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_jpl = model.SubmodelElementCollectionOrdered(id_short="JointPositionLimits")

prop1 = model.Property(id_short="A1", value_type=model.datatypes.String, value="-166/166 deg")
prop2 = model.Property(id_short="A2", value_type=model.datatypes.String, value="-101/101 deg")
prop3 = model.Property(id_short="A3", value_type=model.datatypes.String, value="-166/166 deg")
prop4 = model.Property(id_short="A4", value_type=model.datatypes.String, value="-176/-4 deg")
prop5 = model.Property(id_short="A5", value_type=model.datatypes.String, value="-166/166 deg")
prop6 = model.Property(id_short="A6", value_type=model.datatypes.String, value="-1/215 deg")
prop7 = model.Property(id_short="A7", value_type=model.datatypes.String, value="-166/166 deg")

prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7]
for i in prop:
        smc_jpl.value.add(i)

smc_add.value.add(smc_jpl)

#create smc collection and add it to the submodel
smc_jvl = model.SubmodelElementCollectionOrdered(id_short="JointVelocityLimits")

prop1 = model.Property(id_short="A1", value_type=model.datatypes.String, value="150 deg/s")
prop2 = model.Property(id_short="A2", value_type=model.datatypes.String, value="150 deg/s")
prop3 = model.Property(id_short="A3", value_type=model.datatypes.String, value="150 deg/s")
prop4 = model.Property(id_short="A4", value_type=model.datatypes.String, value="150 deg/s")
prop5 = model.Property(id_short="A5", value_type=model.datatypes.String, value="180 deg/s")
prop6 = model.Property(id_short="A6", value_type=model.datatypes.String, value="180 deg/s")
prop7 = model.Property(id_short="A7", value_type=model.datatypes.String, value="180 deg/s")

prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7]
for i in prop:
        smc_jvl.value.add(i)

smc_add.value.add(smc_jvl)

#create smc collection and add it to the submodel
smc_int = model.SubmodelElementCollectionOrdered(id_short="RobotInterfaces")

prop1 = model.Property(id_short="Robot_NumberOfInterfaces", value_type=model.datatypes.String, value="5")
prop2 = model.Property(id_short="Robot_TCP_IP", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Robot_EnableDeviceInput", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Robot_SafeguardInput", value_type=model.datatypes.String, value="")
prop5 = model.Property(id_short="Robot_ControlConnector", value_type=model.datatypes.String, value="")
prop6 = model.Property(id_short="Robot_HandConnector", value_type=model.datatypes.String, value="")


prop=[prop1,prop2,prop3,prop4,prop5,prop6]
for i in prop:
        smc_int.value.add(i)

smc_add.value.add(smc_int)

# 2.smc control box
smc_add = model.SubmodelElementCollectionOrdered(id_short="RobotControlBox", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="MinimumSupplyVoltage", value_type=model.datatypes.String, value="100 V")
prop2 = model.Property(id_short="MaximumSupplyVoltage", value_type=model.datatypes.String, value="240 V")
prop3 = model.Property(id_short="MainFrequency", value_type=model.datatypes.String, value="47-63 Hz")
prop4 = model.Property(id_short="ActivePowerFactorCorrection", value_type=model.datatypes.Boolean, value= 1)
prop5 = model.Property(id_short="Weight", value_type=model.datatypes.String, value="7 kg")
prop6 = model.Property(id_short="ProtectionRating", value_type=model.datatypes.String, value="IP 20")
prop7 = model.Property(id_short="AirHumidity", value_type=model.datatypes.String, value="20%-80%")



prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7]

for i in prop:
        smc_add.value.add(i)
submodel_2.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_inter = model.SubmodelElementCollectionOrdered(id_short="ControlBoxInterfaces")

prop1 = model.Property(id_short="Box_NumberOfPorts", value_type=model.datatypes.String, value="3")
prop2 = model.Property(id_short="Box_Ethernet_TCP_IP", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Box_V_Lock", value_type=model.datatypes.String, value="IEC 60320-C14")
prop4 = model.Property(id_short="Box_ArmConnector", value_type=model.datatypes.String, value="")


prop=[prop1,prop2,prop3,prop4]
for i in prop:
        smc_inter.value.add(i)

smc_add.value.add(smc_inter)

#create smc collection and add it to the submodel
smc_cs = model.SubmodelElementCollectionOrdered(id_short="BoxControllerSize")

prop1 = model.Property(id_short="ControlBoxDepth", value_type=model.datatypes.String, value="355 mm")
prop2 = model.Property(id_short="ControlBoxWidth", value_type=model.datatypes.String, value="483 mm")
prop3 = model.Property(id_short="ControlBoxHeight", value_type=model.datatypes.String, value="89 mm")

prop=[prop1,prop2,prop3]
for i in prop:
        smc_cs.value.add(i)

smc_add.value.add(smc_cs)

#create smc collection and add it to the submodel
smc_power = model.SubmodelElementCollectionOrdered(id_short="PowerConsumption")

prop1 = model.Property(id_short="MaximumPowerConsumption", value_type=model.datatypes.String, value="600 W")
prop2 = model.Property(id_short="AveragePowerConsumption", value_type=model.datatypes.String, value="300 W")



prop=[prop1,prop2]
for i in prop:
        smc_power.value.add(i)

smc_add.value.add(smc_power)

#create smc collection and add it to the submodel
smc_at = model.SubmodelElementCollectionOrdered(id_short="AmbientTemperature")

prop1 = model.Property(id_short="TypicalAmbientTemperature", value_type=model.datatypes.String, value="+15/+25 degree celsius")
prop2 = model.Property(id_short="ExtendedAmbientTemperature", value_type=model.datatypes.String, value="+5/+45 degree celsius")



prop=[prop1,prop2]
for i in prop:
        smc_at.value.add(i)

smc_add.value.add(smc_at)

# 3.smc robot hand
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_EndEffector", kind=model.ModelingKind.TEMPLATE)
prop1 = model.Property(id_short="Robot_EndEffector_Weight", value_type=model.datatypes.String, value="7 kg")

smc_add.value.add(prop1)

submodel_2.submodel_element.add(smc_add)

#create smc collection and add it to the submodel collection
smc_pg = model.SubmodelElementCollectionOrdered(id_short="ParallelGripper")



smc_add.value.add(smc_pg)

#create smc collection and add it to the submodel
smc_gf = model.SubmodelElementCollectionOrdered(id_short="GraspingForce")

prop1 = model.Property(id_short="ContinuousForce", value_type=model.datatypes.String, value="70 N")
prop2 = model.Property(id_short="MaximumForce", value_type=model.datatypes.String, value="140 N")


prop=[prop1,prop2]
for i in prop:
        smc_gf.value.add(i)

smc_add.value.add(smc_gf)

#create smc collection and add it to the submodel
smc_travel = model.SubmodelElementCollectionOrdered(id_short="Gripper_Travel")

prop1 = model.Property(id_short="Gripper_TravelingSpan", value_type=model.datatypes.String, value="80 mm")
prop2 = model.Property(id_short="Gripper_TravelingSpeedPerFinger", value_type=model.datatypes.String, value="50 mm/s")



prop=[prop1,prop2]
for i in prop:
        smc_travel.value.add(i)

smc_add.value.add(smc_travel)

#create smc collection and add it to the submodel
smc_ft = model.SubmodelElementCollectionOrdered(id_short="Footprint")

prop1 = model.Property(id_short="Footprint_OverallLength", value_type=model.datatypes.String, value="190 mm")
prop2 = model.Property(id_short="Footprint_OverallWidth", value_type=model.datatypes.String, value="226 mm")
prop3 = model.Property(id_short="Footprint_OverallHeight", value_type=model.datatypes.String, value="10 mm")




prop=[prop1,prop2,prop3]
for i in prop:
        smc_ft.value.add(i)

smc_add.value.add(smc_ft)

###########################################################################################################################################################################################################
#------------3.submodel: capabilities--------------------------------------------

submodel_identifier = model.Identifier('https://tum.ais.de/Submodels/Capabilities', model.IdentifierType.IRI)
submodel_3 = model.Submodel(identification=submodel_identifier, id_short="Capabilities", kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_3))

# 1. smc collision 
smc_add = model.SubmodelElementCollectionOrdered(id_short="CollisionBehavior", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_low1 = model.SubmodelElementCollectionOrdered(id_short="Lower_torque_thresholds_acceleration")


for i in range(7):
        property_tau = model.Property(id_short=('tau'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_low1.value.add(property_tau) 


smc_add.value.add(smc_low1)

#create smc collection and add it to the submodel
smc_up1 = model.SubmodelElementCollectionOrdered(id_short="Upper_torque_thresholds_acceleration")


for i in range(7):
        property_tau = model.Property(id_short=('tau'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_up1.value.add(property_tau) 

smc_add.value.add(smc_up1)

#create smc collection and add it to the submodel
smc_low2 = model.SubmodelElementCollectionOrdered(id_short="Lower_torque_thresholds_nominal")


for i in range(7):
        property_tau = model.Property(id_short=('tau'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_low2.value.add(property_tau) 

smc_add.value.add(smc_low2)

#create smc collection and add it to the submodel
smc_up2 = model.SubmodelElementCollectionOrdered(id_short="Upper_torque_thresholds_nominal")


for i in range(7):
        property_tau = model.Property(id_short=('tau'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_up2.value.add(property_tau) 

smc_add.value.add(smc_up2)

#create smc collection and add it to the submodel
smc_low3 = model.SubmodelElementCollectionOrdered(id_short="Lower_force_thresholds_acceleration")

ids = ['x', 'y', 'z', 'R', 'P', 'Y']
for i in ids :
        property_force = model.Property(id_short=('Force'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_low3.value.add(property_force) 

smc_add.value.add(smc_low3)

#create smc collection and add it to the submodel
smc_up3 = model.SubmodelElementCollectionOrdered(id_short="Upper_force_thresholds_acceleration")

ids = ['x', 'y', 'z', 'R', 'P', 'Y']
for i in ids :
        property_force = model.Property(id_short=('Force'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_up3.value.add(property_force) 

smc_add.value.add(smc_up3)

#create smc collection and add it to the submodel
smc_low4 = model.SubmodelElementCollectionOrdered(id_short="Lower_force_thresholds_nominal")

ids = ['x', 'y', 'z', 'R', 'P', 'Y']
for i in ids :
        property_force = model.Property(id_short=('Force'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_low4.value.add(property_force) 

smc_add.value.add(smc_low4)

#create smc collection and add it to the submodel
smc_up4 = model.SubmodelElementCollectionOrdered(id_short="Upper_force_thresholds_nominal")

ids = ['x', 'y', 'z', 'R', 'P', 'Y']
for i in ids :
        property_force = model.Property(id_short=('Force'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_up4.value.add(property_force) 

smc_add.value.add(smc_up4)

# 2. smc update state
smc_add = model.SubmodelElementCollectionOrdered(id_short="UpdateRobotState", kind=model.ModelingKind.TEMPLATE)
submodel_3.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_read = model.SubmodelElementCollectionOrdered(id_short="ReadOnce")
smc_add.value.add(smc_read)

# 3. smc update state
smc_add = model.SubmodelElementCollectionOrdered(id_short="UpdateGripperState", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

#create smc collection and add it to the submodel
smc_read = model.SubmodelElementCollectionOrdered(id_short="ReadOnce")


smc_add.value.add(smc_read)

# 4. smc update state
smc_add = model.SubmodelElementCollectionOrdered(id_short="CartesianMotionFunction", kind=model.ModelingKind.TEMPLATE)


prop1 = model.Property(id_short="CMF_StartTime", value_type=model.datatypes.String, value="0.0")
prop2 = model.Property(id_short="CMF_EndTime", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="CMF_CurrentPose", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="CMF_kRadius", value_type=model.datatypes.String, value= "")
prop5 = model.Property(id_short="CMF_Angle", value_type=model.datatypes.String, value="")
prop6 = model.Property(id_short="CMF_DeltaX", value_type=model.datatypes.String, value="")
prop7 = model.Property(id_short="CMF_DeltaY", value_type=model.datatypes.String, value="")
prop8 = model.Property(id_short="CMF_DeltaZ", value_type=model.datatypes.String, value="")



prop=[prop1,prop2,prop3,prop4,prop5,prop6,prop7,prop8]

for i in prop:
        smc_add.value.add(i)
submodel_3.submodel_element.add(smc_add)

#create smc collection and add it to the submodel collection
smc_motion = model.SubmodelElementCollectionOrdered(id_short="RobotMotionGenerator")
smc_add.value.add(smc_motion)

prop1 = model.Property(id_short="RobotMotionSpeed", value_type=model.datatypes.String, value="")
smc_motion.value.add(prop1)

smc_goal = model.SubmodelElementCollectionOrdered(id_short="JointGoal")
smc_motion.value.add(smc_goal)

for i in range(7):
        property_goal = model.Property(id_short=('q_goal'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_goal.value.add(property_goal) 

# 5. smc Gripper movement
smc_add = model.SubmodelElementCollectionOrdered(id_short="GripperMovement", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

prop1 = model.Property(id_short="GripperMove", value_type=model.datatypes.Boolean, value=1)
prop2 = model.Property(id_short="GripperStop", value_type=model.datatypes.Boolean, value=0)
prop3 = model.Property(id_short="OpeningWidth", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="ClosingSpeed", value_type=model.datatypes.String, value= "")
prop=[prop1,prop2,prop3,prop4]

for i in prop:
        smc_add.value.add(i)

# 6. smc Grasping
smc_add = model.SubmodelElementCollectionOrdered(id_short="GraspingFunction", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

prop1 = model.Property(id_short="Gripper_Grasp", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Gripper_Width", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Gripper_Speed", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Gripper_Force", value_type=model.datatypes.String, value= "")
prop5 = model.Property(id_short="Gripper_EpsilonInner", value_type=model.datatypes.String, value= "0.005 m")
prop6 = model.Property(id_short="Gripper_EpsilonOuter", value_type=model.datatypes.String, value= "0.005 m")

prop=[prop1,prop2,prop3,prop4,prop5,prop6]

for i in prop:
        smc_add.value.add(i)

# 7. smc homing
smc_add = model.SubmodelElementCollectionOrdered(id_short="GripperHoming", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

prop = model.Property(id_short="Gripper_Homing", value_type=model.datatypes.Boolean, value=1)
smc_add.value.add(prop)

# 8. smc homing
smc_add = model.SubmodelElementCollectionOrdered(id_short="RobotPoseHoming", kind=model.ModelingKind.TEMPLATE)

submodel_3.submodel_element.add(smc_add)

prop = model.Property(id_short="RobotPose_Homing", value_type=model.datatypes.Boolean, value=1)
smc_add.value.add(prop)

#############################################################################################################################################################################################
#------------4.submodel: operation data --------------------------------------------

submodel_identifier_operational_data = model.Identifier('https://tum.ais.de/Submodels/OperationalData', model.IdentifierType.IRI)
semantic_reference_operational_data = model.Reference( (model.Key( type_=model.KeyElements.GLOBAL_REFERENCE,
                                                                      local=False,
                                                                      value='TBD Reference to definition of OperationalData',
                                                                      id_type=model.KeyType.IRI  ),) )
submodel_4 = model.Submodel(identification=submodel_identifier_operational_data,
                                                id_short="OperationalData",
                                                semantic_id=semantic_reference_operational_data)
aas.submodel.add(model.AASReference.from_referable(submodel_4))


#4.1 add prpperty to this submodel
property_OperatingTime = model.Property(id_short="Robot_TotalOperatingTime", value_type=model.datatypes.Duration, value=None)
submodel_4.submodel_element.add(property_OperatingTime)

#4.2 smc 
smc_add = model.SubmodelElementCollectionOrdered(id_short="EndEffectorPoseBaseFrame")

submodel_4.submodel_element.add(smc_add)



ids = ['x', 'y', 'z', 'dx', 'dy', 'dz','cx', 'cy', 'cz']
for i in ids :
        property_tee= model.Property(id_short=('OTEE'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_add.value.add(property_tee) 
#4.3 smc EndEffectorPoseFlangeFrame
smc_add = model.SubmodelElementCollectionOrdered(id_short="EndEffectorPoseFlangeFrame")
submodel_4.submodel_element.add(smc_add)

ids = ['x', 'y', 'z']
for i in ids :
        property_1=model.Property(id_short=('FTEE'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        property_2=model.Property(id_short=('FTNE'+i), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_add.value.add(property_1)
        smc_add.value.add(property_2)

#4.4 smc joint data
smc_add = model.SubmodelElementCollectionOrdered(id_short="JointData")
submodel_4.submodel_element.add(smc_add)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="MeasuredJointPosition")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('JointPosition'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos) 
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="DesiredJointPosition")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('DesiredJointPosition'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos) 
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="MeasuredJointVelocity")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('MeasuredJointVelocity_dq'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="DesiredJointVelocity")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('dqd'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="DesiredJointAccelation")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('ddqd'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="MeasuredJointTorque")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('tau_q'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="DesiredJointTorque")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('tau_qd'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)
#create smc collection and add it to the submodel collection
smc_joint = model.SubmodelElementCollectionOrdered(id_short="DerivativeJointTorque")
smc_add.value.add(smc_joint)

for i in range(7):
        property_jointpos = model.Property(id_short=('dtau_q'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_joint.value.add(property_jointpos)


#4.5 smc gripper data
smc_add = model.SubmodelElementCollectionOrdered(id_short="GripperData")
submodel_4.submodel_element.add(smc_add)

prop1 = model.Property(id_short="GripperData_Width", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="GripperData_MaxWidth", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="GripperData_Speed", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="GripperData_IsGrasped", value_type=model.datatypes.String, value= "")
prop5 = model.Property(id_short="GripperData_GripperDurationTime", value_type=model.datatypes.String, value= "0.005 m")
prop6 = model.Property(id_short="GripperData_GripperModel", value_type=model.datatypes.String, value= "0.005 m")

prop=[prop1,prop2,prop3,prop4,prop5,prop6]

for i in prop:
        smc_add.value.add(i)

#4.6 smc MotorData data
smc_add = model.SubmodelElementCollectionOrdered(id_short="MotorData")
submodel_4.submodel_element.add(smc_add)

#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MotorPosition")
smc_add.value.add(smc_son)

for i in range(7):
        property_son = model.Property(id_short=('theta'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MotorVelocity")
smc_add.value.add(smc_son)

for i in range(7):
        property_son = model.Property(id_short=('dtheta'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)

#4.7 smc ElbowData data
smc_add = model.SubmodelElementCollectionOrdered(id_short="ElbowData")
submodel_4.submodel_element.add(smc_add)

#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="ElbowConfiguration")
smc_add.value.add(smc_son)
for i in range(2):
        property_son = model.Property(id_short=('elbow'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="DesiredElbowConfiguration")
smc_add.value.add(smc_son)
for i in range(2):
        property_son = model.Property(id_short=('desired_elbow'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="CommandedElbowConfiguration")
smc_add.value.add(smc_son)
for i in range(2):
        property_son = model.Property(id_short=('commanded_elbow'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="CommandedElbowVelocity")
smc_add.value.add(smc_son)
for i in range(2):
        property_son = model.Property(id_short=('vel_elbow'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="CommandedElbowAcceleration")
smc_add.value.add(smc_son)
for i in range(2):
        property_son = model.Property(id_short=('acc_elbow'+str(i+1)), 
                                                 value_type=model.datatypes.String,
                                                 value=None)
        smc_son.value.add(property_son)

############################################################################################################################################
#---------------------------5.submodel: skills--------------------------------------------
submodel_identifier_sk = model.Identifier('https://tum.ais.de/Submodels/Skills', model.IdentifierType.IRI)
semantic_reference = model.Reference( (model.Key( type_=model.KeyElements.GLOBAL_REFERENCE,
                                                 local=False,
                                                 value= 'reference to the skills',
                                                 id_type=model.KeyType.IRI   ),) )
submodel_5 = model.Submodel(identification=submodel_identifier_sk,
                                                id_short="Skills",
                                                semantic_id=semantic_reference)
aas.submodel.add(model.AASReference.from_referable(submodel_5))


#  5.1 add smc to this submodel
smc_add = model.SubmodelElementCollectionOrdered(id_short="Pick_and_Place_JoghurtProducts")
submodel_5.submodel_element.add(smc_add)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MovingDown")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="GraspingBottle")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MovingUpVertically")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MovingAround")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="PlacingBottle")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="MovingToInitial")
smc_add.value.add(smc_son)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="DetectProduct")
smc_add.value.add(smc_son)

#################################################################################################################################################################################################################################
#---------------------------6.submodel: components--------------------------------------------
submodel_identifier_Components = model.Identifier('https://tum.ais.de/Submodels/Components', model.IdentifierType.IRI)
semantic_reference = model.Reference( (model.Key( type_=model.KeyElements.GLOBAL_REFERENCE,
                                                 local=False,
                                                 value='Refernce to components',
                                                 id_type=model.KeyType.IRI ),) )
submodel_6 = model.Submodel(identification=submodel_identifier_Components,
                                                id_short="Components",
                                                semantic_id=semantic_reference, kind=model.ModelingKind.TEMPLATE)
aas.submodel.add(model.AASReference.from_referable(submodel_6))
#   6.1- 6.5 add smc to this submodel
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_Base")
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_StatusLight")
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_Shoulder")
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_SoftProtector")
submodel_6.submodel_element.add(smc_add)
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_Elbow")
submodel_6.submodel_element.add(smc_add)

# 6.6 add smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="Robot_Pilot")
submodel_6.submodel_element.add(smc_add)
prop1 = model.Property(id_short="PilotMode", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Pilot_Cancel", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Pilot_Enter", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Pilot_Save", value_type=model.datatypes.String, value= "")
prop5 = model.Property(id_short="Pilot_StatusLight", value_type=model.datatypes.String, value= "0.005 m")

prop=[prop1,prop2,prop3,prop4,prop5]
for i in prop:
        smc_add.value.add(i)
#create smc collection and add it to the submodel collection
smc_son = model.SubmodelElementCollectionOrdered(id_short="DirectionsKeys")
smc_add.value.add(smc_son)
prop1 = model.Property(id_short="Key_Up", value_type=model.datatypes.String, value="")
prop2 = model.Property(id_short="Key_Down", value_type=model.datatypes.String, value="")
prop3 = model.Property(id_short="Key_Left", value_type=model.datatypes.String, value="")
prop4 = model.Property(id_short="Key_Right", value_type=model.datatypes.String, value= "")
prop=[prop1,prop2,prop3,prop4]
for i in prop:
        smc_add.value.add(i)

# 6.7 add smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="Disc")
submodel_6.submodel_element.add(smc_add)
# 6.8 add smc
smc_add = model.SubmodelElementCollectionOrdered(id_short="Grip")
submodel_6.submodel_element.add(smc_add)
ent1 = model.Entity(id_short="Grip_Flange",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent2 = model.Entity(id_short="Grip_Finger",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent3 = model.Entity(id_short="Grip_Fingertip",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent4 = model.Entity(id_short="Grip_Scews",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent5 = model.Entity(id_short="Grip_CylindricalPin",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent6 = model.Entity(id_short="Grip_Links",entity_type=model.EntityType.CO_MANAGED_ENTITY)
ent7 = model.Entity(id_short="Grip_Joints",entity_type=model.EntityType.CO_MANAGED_ENTITY)

prop1 = model.Property(id_short="Grip_Numbers", value_type=model.datatypes.String, value="2")
prop2 = model.Property(id_short="Grip_Specification", value_type=model.datatypes.String, value="DIN7984")
prop3 = model.Property(id_short="Grip_Size", value_type=model.datatypes.String, value="M6X12")

prop=[prop1,prop2,prop3]
for i in prop:
        ent4.statement.add(i)
prop1 = model.Property(id_short="Grip_CylindricalPinNumbers", value_type=model.datatypes.String, value="1")
prop2 = model.Property(id_short="Grip_CylindricalPinSpecification", value_type=model.datatypes.String, value="ISO2338B")
prop3 = model.Property(id_short="Grip_CylindricalPinSize", value_type=model.datatypes.String, value="6X10 h8 A2")

prop=[prop1,prop2,prop3]
for i in prop:
        ent5.statement.add(i)

ent=[ent1,ent2,ent3,ent4,ent5,ent6,ent7]
for i in ent:
        smc_add.value.add(i)

# 6.9 add smc links
smc_add = model.SubmodelElementCollectionOrdered(id_short="Links")
submodel_6.submodel_element.add(smc_add)
prop1 = model.Property(id_short="NumberOfLinks", value_type=model.datatypes.String, value="5")
smc_add.value.add(prop1)

Length=["0.333 m","0.316 m","0.384 m","0.088 m","0.107 m"]
for i in range(5):
        ent_link = model.Entity(id_short=('Link'+str(i+1)), entity_type=model.EntityType.CO_MANAGED_ENTITY)
        prop=model.Property(id_short="LinkageLength", value_type=model.datatypes.String, value=Length[i])
        ent_link.statement.add(prop)
        smc_add.value.add(ent_link)
# 6.10 add smc joints
smc_add = model.SubmodelElementCollectionOrdered(id_short="Joints")
submodel_6.submodel_element.add(smc_add)
prop1 = model.Property(id_short="NumberOfJoints", value_type=model.datatypes.String, value="7 ")
smc_add.value.add(prop1)

Max=["2.7437 rad","1.7837 rad","2.9007 rad","-0.1518 rad","2.8065 rad","4.5169 rad","3.0159 rad"]
Min=["-2.7437 rad","-1.7837 rad","-2.9007 rad","-3.0421 rad","-2.8065 rad","0.5445 rad","-3.0159 rad"]

for i in range(7):
        ent_joint = model.Entity(id_short=('Joint'+str(i+1)), entity_type=model.EntityType.CO_MANAGED_ENTITY)
        prop=model.Property(id_short=("q"+str(i+1)+"max"), value_type=model.datatypes.String, value=Max[i])
        prop2=model.Property(id_short=("q"+str(i+1)+"min"), value_type=model.datatypes.String, value=Min[i])
        ent_joint.statement.add(prop)
        ent_joint.statement.add(prop2)
        smc_add.value.add(ent_joint)





#---------------------------1.submodel: nameplate---------------------------------------------------------------------------------------
#---------------------------2.submodel: technical data---------------------------------------------------------------------------------------
#---------------------------3.submodel: capabilities--------------------------------------------
#---------------------------4.submodel: operation data --------------------------------------------
#---------------------------5.submodel: skills--------------------------------------------
#---------------------------6.submodel: components--------------------------------------------
######################################################################################################################################################
object_store = model.DictObjectStore([aas, asset, submodel_nameplate, submodel_2, submodel_3, submodel_4, submodel_5, submodel_6])
file_store = aasx.DictSupplementaryFileContainer()

with aasx.AASXWriter("01_FrankaEmika_Robot_Arm_AAS.aasx") as w:

        w.write_aas(aas_id=aas_identifier, object_store=object_store, file_store=file_store, submodel_split_parts=False)

print('Finisched writing aasx file')


