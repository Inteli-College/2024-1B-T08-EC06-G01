#!/bin/bash

# if the directory "env" does not exist, create a virtual environment
if [ ! -d "env" ]; then
	echo "Creating virtual environment..."
	python3 -m venv env
fi

source env/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null

cd camera

# ROS_DOMAIN_ID=69 ros2 run cannabot_camera camera
python3 main.py
