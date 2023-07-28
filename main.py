# las/laz file format parsing:
# https://pylas.readthedocs.io/en/latest/installation.html

# pip install pylas
# pip install laszip - for handling .laz

import pylas

las = pylas.read( "USGS_LPC_TX_Pecos_Dallas_2018_D19_14SPB5768.laz" )
print( np.unique( las.classification ) )