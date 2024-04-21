# """lets say there is no actual screeen or GUI window in the setup then solutions""""

!apt-get install -y xvfb
!Xvfb :99 -screen 0 1024x768x24 &
!export DISPLAY=:99


# then run the code
