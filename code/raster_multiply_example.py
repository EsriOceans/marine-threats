#!/usr/bin/python
"""
  Threat Matrix Model

 
  Original Author: Matthew Perry and Shaun Walbirdge 
  ArcGIS port: Shaun Walbridge

python $PROJECT_DIR/code/threats/threat_model.py $PROJECT_DIR/data/matrices/generated/all_med_annual_sst.csv model_all_med_annual_sst



"""

# ArcGIS implementation
import arcpy
from arcpy.sa import *
from arcpy import env

# Python system libraries
import sys
import os
import time

name = "combo_test.tif"
arcpy.AddMessage("  %s" % name)

env.workspace = "E:\\work\\massachusetts\\threat_model\\demo\\output"

threat_raster = "E:\\work\\massachusetts\\threat_model\\demo\\habitats\\habitat_seagrass_global.tif"
habitat_raster = "E:\\work\\massachusetts\\threat_model\\demo\\threats\\threat_fert_global_ln_normalized.tif"

arcpy.AddMessage(habitat_raster)
arcpy.AddMessage(threat_raster)

combo = Raster(threat_raster) * Raster(habitat_raster)
# The save method automagically figures out the right type to save 
# by looking at the extension. Sweet! 
combo.save(name)
