# las/laz file format parsing:
# https://pylas.readthedocs.io/en/latest/installation.html

# pip install pylas
# pip install laszip - for handling .laz

# using laz does not seem to be functional - can't figure out how to set it up the way it expects
# CloudCompare seems to be good software for doing the conversion: https://www.danielgm.net/cc/forum/viewtopic.php?t=4371

import pylas

las = pylas.read( "USGS_LPC_TX_Pecos_Dallas_2018_D19_14SPB5768.laz" )
print( np.unique( las.classification ) )