send.py
sleep 15
sudo iw phy phy0 interface add mon0 type monitor 
sudo iw dev wlan0 del
sleep 5
kismet_client
sleep 600
sudo reboot