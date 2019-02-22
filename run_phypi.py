#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' script run_phypi.py to execute PhyPiDAQ 

    usage: run_phypi.py <config>.daq
'''

import sys
from phypidaq.runPhyPiDAQ import *

if __name__ == "__main__": # - - - - - - - - - - - - - - - - - - - -
 if len(sys.argv) != 2 :
   print("run_phypi.py usage:\n run_phypi.py <config>.daq")
   sys.exit(1)      
  
 daq=runPhyPiDAQ(verbose=0) # 1: normal output
                            # 0: only errors are printed
                            # 2: verbose output

 daq.setup()
 print( "DAQ set-up:\n", yaml.dump(daq.PhyPiConfDict))

 daq.run()
