# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2016 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA  02110-1301, USA.
"""
Simple example that connects to one crazyflie (check the address at the top
and update it to your crazyflie address) and send a sequence of setpoints,
one every 5 seconds.

This example is intended to work with the Loco Positioning System in TWR TOA
mode. It aims at documenting how to set the Crazyflie in position control mode
and how to send setpoints.
"""
import logging
import time
import numpy as np

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import natnetclient as natnet

import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from timeit import default_timer as timer
import matplotlib

# Set communication address of the quadrotor
uri = 'radio://0/60/2M'

# Set camera system address
camera_IP = '10.12.28.134'

if __name__ == '__main__':
    # Set initial position
    client = natnet.NatClient(client_ip=camera_IP, data_port=1511, comm_port=1510)
    hand = client.rigid_bodies['Rigid_Body_1']  # Assuming a Motive Rigid Body is available that you named "Hand"
    Last_time = timer()
    while True:
        Current_time = timer()
        if (Current_time - Last_time) >= 0.1:
            #hand = client.rigid_bodies['Rigid_Body_1']  # Assuming a Motive Rigid Body is available that you named "Hand"
            #hand1 = client.rigid_bodies['Rigid_Body_2']  # Assuming a Motive Rigid Body is available that you named "Hand"
            print(client)
            Last_time = Current_time






