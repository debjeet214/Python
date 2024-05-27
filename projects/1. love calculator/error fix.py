# """lets say there is no actual screen or GUI window in the setup then solution is this""""
# This solution will help in gettinggg a virtual working window screen for the online compiler or any mac users

!apt-get install -y xvfb
!Xvfb :99 -screen 0 1024x768x24 &
!export DISPLAY=:99


# then run the code
