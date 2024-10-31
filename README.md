# digitaltwin

### C# dotnet run step
1. dotnet new console -n MyFirstApp
2. cd MyFirstApp
3. open Program.cs file
4. edit
5. dotnet run
   
### Install .NET SDK:

- Download and install the .NET SDK [here](https://dotnet.microsoft.com/download/dotnet).
- After installation, you can verify the installation by running `dotnet --version` in the command line.

### Install VS Code:

- Download and install VS Code [here](https://code.visualstudio.com/).

### Install C# Extension:

- Open VS Code, go to the extensions panel (use the shortcut `Ctrl+Shift+X`).
- Search for "C#" and install the extension provided by Microsoft.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### Installing Omniverse in Ubuntu
1. install cache and nucleus (document from Gitlab)
2. unistall all the nvida
```
sudo apt-get remove --purge '^nvidia-.*'
sudo apt autoremove
sudo apt autoclean
```
- install a new driver
  download .run files here: https://www.nvidia.com/en-us/drivers/unix/
3. Terminal installing driver  
  Change to the directory where you have the .run file stored.  
  
    -Type: chmod 755 filename.run  

    -Type: sudo ./filename.run  

  eg: sudo ./NVIDIA-Linux-x86_64-550.90.07.run

  4. Terminal
```
     cd ~/.local/share/ov/pkg/isaac-sim-4.0.0
     
     xdg-open extension_examples
```
```
     cd ~/.local/share/ov/pkg/isaac-sim-2023.1.1
     
     xdg-open extension_examples
```
   6.  -open user example
  ```    
/home/masais/.local/share/ov/pkg/isaac-sim-4.0.0/extension_examples/user_examples
```

lib: https://docs.omniverse.nvidia.com/py/isaacsim/source/extensions/omni.isaac.core/docs/index.html#robots
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### Run Simulation in IssacSim
# 1. Robot Movement
   ```
   cd ziyu/robotControlProgram/build
   ```
   enter the robot control folder
2. Turn on IssacSim, impoert the project: PandaAIS
3. Change the environment light
4. Press F to center the view.
5. Press Start Run button in Issac.
6. run the pickup and place program firstly in the above file-located Terminal:
   ```
   ./bottleplacingloopPICKPALCEbottle 192.168.80.105

   ```
7. Check the simulation. It should work now.
# 2. Bottle Movement

1. file path:
   ```
   cd ziyu/CSCMQTTIssacSim
   ```
2. Close the Issac Sim Simulator, then open it again to reset.
3. Open the PLC control prog on HIWI_51 Windows Computer:
   	Desktop:Ziyu Li folder->myJoghurt folder-> KIFabrik->IEC -> sln project
4. open the project, import, run.
5. Press the Stop button on myJughurt table -> Press init button and wait-> Press Start 
6. Repeat step 2,3,4,5 above.
7. run the prog:
```
   dotnet run

   ```
8. Put bottle on belt 1
9. Ckeck the Simulation
# 3. Robot fetch the bottle.
1. All same as 1. Robot Movement
2. only step 6 changes: run the fetch program in the above file-located Terminal:
   ```
   ./bottleplacingloopFetchbottle 192.168.80.105

   ```


-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### WIFI Configuration
#1. check all the wlan infos
```
uname -r
```
5.15.0-105-generic
```
 lspci -nnk | grep 0280 -A3
```
00:14.3 Network controller [0280]: Intel Corporation Device [8086:7af0] (rev 11)
	DeviceName: Onboard - Ethernet
	Subsystem: Intel Corporation Device [8086:0094]
	Kernel driver in use: iwlwifi
```
sudo lshw -C network
```
 *-network                 
       description: Wireless interface
       product: Intel Corporation
       vendor: Intel Corporation
       physical id: 14.3
       bus info: pci@0000:00:14.3
       logical name: wlo1
       version: 11
       serial: 70:1a:b8:9b:b5:4f
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress msix bus_master cap_list ethernet physical wireless
       configuration: broadcast=yes driver=iwlwifi driverversion=5.15.0-105-generic firmware=64.97bbee0a.0 so-a0-gf-a0-64.uc latency=0 link=no multicast=yes wireless=IEEE 802.11
       resources: iomemory:480-47f irq:18 memory:4802124000-4802127fff

       
  *-network
       description: Ethernet interface
       product: Intel Corporation
       vendor: Intel Corporation
       physical id: 0
       bus info: pci@0000:03:00.0
       logical name: enp3s0
       version: 03
       serial: 04:7c:16:49:9f:79
       size: 1Gbit/s
       capacity: 1Gbit/s
       width: 32 bits
       clock: 33MHz
       capabilities: pm msi msix pciexpress bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
       configuration: autonegotiation=on broadcast=yes driver=igc driverversion=5.15.0-105-generic duplex=full firmware=1073:8754 ip=192.168.80.100 latency=0 link=yes multicast=yes port=twisted pair speed=1Gbit/s
       resources: irq:16 memory:51100000-511fffff memory:51200000-51203fff


2. download the iwlwifi files
   
https://launchpad.net/ubuntu/+source/backport-iwlwifi-dkms

http://archive.ubuntu.com/ubuntu/pool/universe/b/backport-iwlwifi-dkms/

4. install the drive:
```
sudo apt install backport-iwlwifi-dkms
make
sudo make install
```

Make sure dkms package is installed by running command: 
```
sudo apt-get install dkms.
```
Go to this page ubuntu wiki.

You will find a table under the "Packages" heading. ...

Click the arrow (to the left) to expand the row of the selected package.

Under the new section "Package files", click the file ending with ". ...

Reboot.


### method
1. update the linux
   
run 
```
sudo apt-get upgrade linux-generic-hwe-20.04
```
 followed by 
 ```sudo reboot```.
 
 To check that version 5.15 was installed, run apt list linux-generic-hwe* and you should see linux-generic-hwe-20.04/focal-updates,focal-security,now 5.15.0.46.49~20.04.16 amd64 [installed].

3. download all the dependencies and files
4. 
https://packages.ubuntu.com/focal/kernel/linux-generic-hwe-20.04

Before installing the package, you will need to install these dependencies first by clicking on their links. In my case, I installed the dependencies that had the label [amd64] next to them, since my laptop runs a 64-bit architecture. Unfortunately, these dependencies have their own dependencies, so you will have to click on each one and then download the corresponding .deb file. In total there were 7 .deb files that I had to download, so this does not take too much time. To download each package, click on the amd64 link under the Download <package name> title. Then, click on the link security.ubuntu.com/ubuntu. Once all packages are downloaded, put them all into a folder


6. run the file
7. 
cd into this folder, and then run ```sudo dpkg -i *.deb```. You will get an error that the linux-generic-hwe-20.04 package could not be installed, but that is OK. Just run sudo reboot, and once logged in again, check that you have version 5.15 of the linux kernel by running uname -r. You should see 5.15.0-46-generic. 
