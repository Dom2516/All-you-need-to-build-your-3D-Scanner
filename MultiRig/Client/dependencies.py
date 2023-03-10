import os

def installDependencies():
    os.system('sudo apt-get -y update')
    os.system('sudo apt-get -y upgrade')
    os.system('sudo raspi-config nonint do_camera 0')
    os.system('sudo raspi-config nonint do_memory_split 256')
    os.system('sudo apt -y install python3-pip')
    os.system('pip3 install picamera flask requests')
    os.system('sudo apt-get -y install python3-rpi.gpio')
    os.system('sudo apt-get -y install zip unzip')
    
installDependencies()
