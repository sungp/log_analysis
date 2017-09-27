===============================================================================
The python script connects to local postresql db named "news" and generates three sepearte reports. 
The following is the step by step instruction on how to setup the database

1. Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org(https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

2. Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com (https://www.vagrantup.com/downloads.html). Install the version for your operating system.

3. Download the VM configuration
Fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory

4. Start the VM 
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
1. 

5. Login into VM
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM

===============================================================================
To run the python code, the following instruction describes how to setup up the database properly and run the script

1. Download the Database
Download the data (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory

2. Setup the database
After logging into VM, cd into the vagrant directory and run the following command
%  psql -d news -f newsdata.sql

% python logreport.py
