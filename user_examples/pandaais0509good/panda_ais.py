# Copyright (c) 2020-2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.


from gc import callbacks
import numpy as np
import os
import datetime
from threading import Timer
from math import pi
import socket
import json
import time
import json, requests
import carb

from omni.isaac.examples.base_sample import BaseSample # Scenarios inherit from BaseSample
# Adding items to the scene
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.core.objects.ground_plane import GroundPlane
from omni.isaac.core.scenes import Scene
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage
# General robot imports (simplified API from Isaac Sim to avoid Pixar's or other USD APIs)
from omni.isaac.core.robots import Robot
from omni.isaac.core.utils.types import ArticulationAction
# Franka Panda specific imports
from omni.isaac.franka import Franka
from omni.isaac.core.prims import RigidPrim

GRAD_TO_RAD = 2*pi/360
HOST_ADDR = "127.0.0.1"
# PORT = 32323 # Port of the Azure Client App (or the simulation)
PORT = 8080
# From: https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        #self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

class PandaAIS(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        # Here additional members can be defined such as _tasks, _controllers
        self._logger = None
        # TCP/IP socket to the Azure Client App
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # DEVELOP MEMBERS
        self._updateTimer = RepeatedTimer(0.2, self.update_joint_position_member)
        self._connectTimer = RepeatedTimer(2, self.connect_to_datasource)
        self._jointPos1 = 0.0
        self._turnDirectionPos = True
        return

    def setup_scene(self):
        # 1: Set up world scene 
        world = self.get_world()
        print("[INFO] Set up world scene.")
        #world.scene.add_default_ground_plane()

        # # 2. Add groundplane to world scene 
        #world.scene.add(GroundPlane(prim_path="/World/groundPlane", size=1050, color=np.array([0.5, 0.5, 0.5])))
        # print("[INFO] Added groundplane to scene.")

        # # 3. Add Franka robot to world scene  
        # absolute_asset_path1 = "/home/masais/panda/Franka/franka_zy.usd"
        # add_reference_to_stage(usd_path=absolute_asset_path1, prim_path="/World/franka")
        # panda_robot = world.scene.add(Robot(prim_path="/World/franka/franka", name="panda_robot", 
        #                                     # scale =[100],
        #                                     position=[0.23988, -0.7097, 1],
        #                                     # orientation = [1,0,0,-1]
        #                                     ))
        # print("Added robot to the scene")
        # print("Num of degrees of freedom before first reset: " + str(panda_robot.num_dof)) # prints None


        ##ziyu 04.09 commit myjoghurt to franka----------------------------------------------------------------------------------------------------------------------------
        # 3. Add myJoghurt to world scene  
        absolute_asset_path = "/home/masais/panda/Franka/myziyu0509.usd"
        # This will create a new XFormPrim and point it to the usd file as a reference
        # Similar to how pointers work in memory
        add_reference_to_stage(usd_path=absolute_asset_path, prim_path="/World/myJoghurt")
       # myjoghurt = world.scene.add(RigidPrim(prim_path="/World/myJoghurt/myJoghurt_ZIyu", name="myjoghurt", 
        #                                     # scale = [1],
       #                                      position=[0,0,100]
       #                                     ))
        
        panda_robot = world.scene.add(Robot(prim_path="/World/myJoghurt/myJoghurt_ZIyu/franka", name="panda_robot", 
                                     scale =[100],
        #                              #position=[25.57,-69.78,-4.86],
        #                             # orientation = [1,0,0,-1]
                                    ))
        
        
        # print("[INFO] Added plant to scene.")



        
        
        bottle = world.scene.add(RigidPrim(prim_path="/World/myJoghurt/myJoghurt_ZIyu/Geometry/VN3066_000_Layout_Uni_Kassel_070919_0/_691296_GLAS_mit_Barcode_33_2581",

                                                           name="bottle",
                                                          #position=[418.74569,-958.25394,-10],
        #                                                   scale=[1]
                                                          ))
    #ziyu end commit----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #ziyu change myjoghurt to franka testing the gripper
        # world.scene.add(GroundPlane(

        #     prim_path="/World/groundPlane", 

        #     size=25,

        #     color=np.array([0.5, 0.5, 0.5])))

        # print("[INFO] Added groundplane to scene.")

 



        # # # 3. Add panda to world scene  

        # # absolute_asset_path = "/home/panda/Franka/franka.usd"

        # panda_prim_path="/World/Panda_Robot"

        # absolute_asset_path = "/home/masais/panda/Franka/franka_zy.usd"

        # # This will create a new XFormPrim and point it to the usd file as a reference

        # add_reference_to_stage(usd_path=absolute_asset_path, prim_path=panda_prim_path)

        # panda_robot = world.scene.add(Robot(prim_path="/World/Panda_Robot", name="panda_robot", 

        #                             position = [0, 0, 0.43], # Feng Xu 12.07.2024 0.45 to 0.43

        #                             orientation = [1,0,0,-1]))

        # print("[INFO] Added panda to scene.")
        return


    async def setup_post_load(self):
        self._world = self.get_world()
        self._franka = self._world.scene.get_object("panda_robot")
        #self._bottle = self._world.scene.get_object("bottle")
        # self._myjoghurt= self._world.scene.get_object("myjoghurt")
        # initial_joint_positions = [0.0, -1.0, 0.0, -2.0, 0.0, 1.5, 0.7,0.1,0.1]
        # self._franka.set_joint_positions(initial_joint_positions)
       # self._world.get_physics_context().set_gravity([0,0,-9.81])
        
        # self._casing = self._world.scene.get_object("casing") 
        # self._ring = self._world.scene.get_object("ring")
        # self._table = self._world.scene.get_object("table")

        print("------ Panda Infos ------")
        print("  DOF-Names     : ", self._franka.dof_names)
        print("  DOF-Properties: ", self._franka.dof_properties)
        # current_bottle_pose = self._bottle.get_world_pose()
        # print("Current bottle position: ", current_bottle_pose)


        print("---- Set-Up Logger ----")
        filepath = os.path.join("/home/masais/panda", "test_node2_full_integration.txt")
        self._logger = open(filepath, 'a')
        self._logger.write("\nStarting new entry at: {t}".format(t=datetime.datetime.now()))
        print("Finished logger setup")

        print("[SETUP] Setup the socket connection")
        self._connectTimer.start()        
        
        # This is an implicit PD controller of the jetbot/ articulation
        # setting PD gains, applying actions, switching control modes..etc.
        # can be done through this controller.
        # Note: should be only called after the first reset happens to the world
        
        #self._jetbot_articulation_controller = self._jetbot.get_articulation_controller()
        
        # Adding a physics callback to send the actions to apply actions with every
        # physics step executed.
        
        #self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
        #self._world.add_physics_callback("logging_jointpos", callback_fn=self.log_joint_position_during_sim)

        ## ziyu manuell apply action
        # self._franka.apply_action(control_actions = ArticulationAction(
        #             joint_positions=[0.285453,-0.246976,0.407148,-2.135107,0.033087,1.897359,-0.401687,0.05,0.05],
        #             joint_efforts=None,
        #             joint_velocities=None
        #         ))
        self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
       ## end modify
        # self._world.add_physics_callback("sending_actions", callback_fn=self.send_mir_actions)
        return
    
    def log_joint_position_during_sim(self, step_size):
        self._logger.write("\n{t} \nJoint-Pos.: {pos}\nJoint-Vel.: {vel}\nSoll: {d}".format(t=datetime.datetime.now(), 
                                                                                 pos=self._franka.get_joint_positions(), 
                                                                                 vel=self._franka.get_joint_velocities(),
                                                                                 d=self._jointPos1))
        return
    # def send_mir_actions(self,step_size):

    #     ip_mir = "192.168.50.250" # without ":8080"
    #     authorization_mir = "Basic RGlzdHJpYnV0b3I6NjJmMmYwZjFlZmYxMGQzMTUyYzk1ZjZmMDU5NjU3NmU0ODJiYjhlNDQ4MDY0MzNmNGNmOTI5NzkyODM0YjAxNA=="
    #     language_mir = "en_US"

    #     host = "http://" + ip_mir + "/api/v2.0.0/"
    #     headers = {}
    #     headers["Content-Type"] = "application/json"
    #     headers["Authorization"] = authorization_mir
    #     headers["Accept-Language"]= language_mir

    #     get_coord = requests.get(host + "/status", headers = headers).json()
    #     print(get_coord['position'])
    #     print(type(get_coord['position']['x']))
    #     position_mir = [get_coord['position']['y']-26,get_coord['position']['x']-25, 0]
    #     roll = get_coord['position']['orientation']/180*3.14
    #     pitch = 0
    #     yaw = 0
    #     qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    #     qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    #     qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    #     qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    #     orientation_mir = [qx, qy, qz, qw]

    #     self._casing.set_world_pose(position=position_mir, orientation=orientation_mir ) 
    #     return
    
    # def send_robot_actions(self, step_size):
    #     try:
    #         # Clear the receive buffer 
    #         self._client.setblocking(0)
    #         chunks = []
    #         while True:
    #             try:
    #                 chunk = self._client.recv(4096)
    #                 if not chunk:
    #                     break
    #                 chunks.append(chunk)
    #             except socket.error:
    #                 break
    #         self._client.setblocking(1)
            
    #         data = b''.join(chunks)
    #         if not data:
    #             return

    #         # Only process the last complete packet
    #         messages = data.decode('utf-8').strip().split('\n')
    #         last_message = messages[-1]
    #         #zy changes the message number
    #         #last_message = messages

    #         print("Read data: ", last_message)

    #         json_list_buffer = json.loads(last_message)
    #         #nparray = np.array(json_list_buffer)
    #         #zy if connect the robot directly, the data should remove q 
    #         nparray = np.array(json_list_buffer['q'])
    #         print("nparray: ", nparray)
    #         print("Array size:", nparray.size)

    #         if nparray.size >= 9:
    #             nparray_new = nparray[0:9]  # Take the first 7 elements for joint positions
    #             # self._franka.set_joint_positions(nparray_new)
    #             self._franka.set_joint_positions(nparray_new)
    #             print("new array is", nparray_new)
                
    #             # get current time
    #             now = datetime.datetime.now()
    #             # print current time
    #             print("Current local time:", now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3])

    #             self._franka.apply_action(control_actions = ArticulationAction(
    #                 joint_positions=nparray_new,
    #                 joint_efforts=None,
    #                 joint_velocities=None
    #             ))
    #         elif nparray.size == 7:
    #             nparray_new = np.append(nparray, [0, 0])
    #             #self._franka.set_joint_positions(nparray_new)
    #         else:
    #             print("Skipped array of incompatible size: ", nparray.size)
            
    #         self._logger.write("\n{t} Joint-Pos.: {pos}".format(t=datetime.datetime.now(), 
    #                                                             pos=nparray_new))

    #     except Exception as ex:
    #         print(f"Exception while converting data: {ex}")    

    #     return

    def send_robot_actions(self, step_size): 

        self._franka.apply_action(control_actions = ArticulationAction(
                    joint_positions=[0.285453,-0.246976,0.407148,-2.135107,0.033087,1.897359,-0.401687,5,5],
                    joint_efforts=None,
                    joint_velocities=None
                ))
        print("  DOF-Names     : ", self._franka.dof_names)
        print("  DOF-Properties: ", self._franka.get_applied_action())
        # sleep(500)
        # self._franka.apply_action(control_actions = ArticulationAction(
        #             joint_positions=[1,1,1,1,1,1,1,-0.01,-0.01],
        #             joint_efforts=None,
        #             joint_velocities=None
        #         ))


        try:
            # Clear the receive buffer 
            self._client.setblocking(0)
            chunks = []
            while True:
                try:
                    chunk = self._client.recv(4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
                except socket.error:
                    break
            self._client.setblocking(1)
            
            data = b''.join(chunks)
            if not data:
                return

            # Only process the last complete packet
            messages = data.decode('utf-8').strip().split('\n')
            last_message = messages[-1]

            print("Read data: ", last_message)

            # JZh added update_count_sum to count total number of data received from RCP
            # self.update_count_sum=self.update_count_sum+1
            # print(self.update_count_sum)
            # end

            json_list_buffer = json.loads(last_message)
            nparray = np.array(json_list_buffer)
            print("nparray: ", nparray)
            print("Array size:", nparray.size)

            if nparray.size == 9:
                nparray_new = nparray[0:9]  # Take the first 7 elements for joint positions
                # self._franka.set_joint_positions(nparray_new)
                
                # get current time
                now = datetime.datetime.now()
                # print current time
                print("Current local time:", now.strftime("%Y-%m-%d %H:%M:%S:%f")[:-3])

                self._franka.apply_action(control_actions = ArticulationAction(
                    joint_positions=nparray_new,
                    joint_efforts=None,
                    joint_velocities=None
                ))
            elif nparray.size == 7:
                nparray_new = np.append(nparray, [0, 0])
                self._franka.set_joint_positions(nparray_new)
            else:
                print("Skipped array of incompatible size: ", nparray.size)
            
            self._logger.write("\n{t} Joint-Pos.: {pos}".format(t=datetime.datetime.now(), 
                                                                pos=nparray_new))

        except Exception as ex:
            print(f"Exception while converting data: {ex}")    

        return

        


    async def setup_pre_reset(self):
        #self._updateTimer.stop()
        #self._connectTimer.start()
        return

    async def setup_post_reset(self):
        return

    def world_cleanup(self):
        #self._updateTimer.stop()
        return

    #------------------------------------------#
    # Unrelated to Omnvierse utility functions #
    #------------------------------------------#
    def update_joint_position_member(self):
        if(self._turnDirectionPos and self._jointPos1 <= 89.5*GRAD_TO_RAD):
            self._jointPos1 += 0.1
        elif(self._turnDirectionPos and self._jointPos1 > 89.5*GRAD_TO_RAD):
            self._turnDirectionPos = False
        elif(not self._turnDirectionPos and self._jointPos1 >= -89.5*GRAD_TO_RAD):
            self._jointPos1 -= 0.1
        else:
            self._turnDirectionPos = True
        
    def connect_to_datasource(self):
        print("Connecting to simulation on port: ", PORT)
        try:
            self._client.connect((HOST_ADDR, PORT))
            print("[DONE] Connected to the server app")
            self._connectTimer.stop()
        except:
            print("[ERROR] Could not connect to a server app")