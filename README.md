# Virtual Field Robot Event 

<img src="https://www.fieldrobot.com/event/wp-content/uploads/2021/01/FRE-logo-v02.png" width="250"> 
<img src="https://www.wur.nl/upload/58340fb4-e33a-4d0b-af17-8d596fa93663_WUR_RGB_standard.png" width="250"> 
<img src="https://www.uni-hohenheim.de/typo3conf/ext/uni_layout/Resources/Public/Images/uni-logo-en.svg" width="250">


# Installation
1.	Get a computer with ubuntu 18.04*. If you do not have a ubuntu 18.04 machine, you can install a virtual machine following the bullet points below. If you already have an ubuntu 18.04 machine you can skip to step 2.
	* Download and install VM ware from the VMware website: https://my.vmware.com/en/web/vmware/downloads/details?downloadGroup=PLAYER-1600&productId=1039&rPId=51984. Download "VMware Workstation 16.0.0 Player for Windows" if you are using a windows computer. Within VMware we install a virtual Linux computer. 
	* Create a new virtual machine using VMware
		* Change the configuration about the number of CPU cores used, the max number of RAM to use and the max allowable hard disk space. 
	* Select ubuntu 18.04 as iso. https://releases.ubuntu.com/18.04.5/ubuntu-18.04.5-desktop-amd64.iso 
2.	Open a terminal(Ctrl + Alt + T) and type ‘sudo apt install git’ to install git
3.	Clone the FRE git repository by typing ‘git clone https://github.com/FieldRobotEvent/Virtual_Field_Robot_Event’ in the terminal. This will create a folder  named ‘fre_virtual_event’, containing all the files need to run the simulation.
4.	Install all required software by typing ‘sudo sh fre_virtual_event/install_required_software.sh’ 
5.	After the installation type ‘source ~/.bashrc’ in the terminal. 
6.	You can now run the simulation by running ‘roslaunch simple_world simple_world.launch'. 
7. 	You can controll the robot, and see the sensor autput using 'roslaunch jackal_viz view_robot.launch'. If you encounter any errors, we refer you to the troubleshooting section. 
8.	The robot used in the simulation is the Clearpath Jackal, you can find detailed instructions and documentation at http://www.clearpathrobotics.com/assets/guides/kinetic/jackal/simulation.html 

*) Feel free to use other versions of Ubuntu, ROS, packages and other software. We have only tested the above versions and software.

# Trouble shooting
* If you encounter the error: ‘VMware: vmw_ioctl_command error Invalid argument.’ When launching gazebo. Then you should type ‘echo "export SVGA_VGPU10=0" >> ~/.profile’ in the terminal and reboot your (virtual) machine. 
* If you encounter the error ‘Error in REST request’ when launching gazebo. Then you should open ‘~/.ignition/fuel/config.yaml’ and change the line: ‘url: https://api.ignitionfuel.org’ to ‘url:  https://api.ignitionrobotics.org’. 






