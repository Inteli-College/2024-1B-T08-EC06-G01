#!/bin/bash

# if the directory "env" does not exist, create a virtual environment
if [ ! -d "env" ]; then
	echo "Creating virtual environment..."
	python3 -m venv env
fi

source env/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null

cd workspace

# get the site-packages path by getting pip show setuptools (setuptools always comes with pip)
VENV_PATH=$(pip show setuptools | grep "Location: " | awk '{print $2}')

export PYTHONPATH="$PYTHONPATH:$VENV_PATH"

echo "Building package..."
colcon build > /dev/null

source install/setup.bash

# ROS_DOMAIN_ID=69 ros2 run websocket_robot websocket_robot

# ROS_DOMAIN_ID=69 ros2 run cannabot lidar_teste

# ROS_DOMAIN_ID=69 ros2 run cannabot cannabot

# ROS_DOMAIN_ID=69 ros2 run cannabot_camera camera