#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
./OFpre/main_pre.py

get new samples from "path2newSample", which is made by gpOpt_TBL.nextGPsample()
write new geometry to "path2run"/"caseName"/system/yTopParams.in
"""
# %% import libraries
# import numpy as np
import sys

# %% logging
import logging
# # create logger
logger = logging.getLogger("OFpre/main_pre.py")
if (logger.hasHandlers()):
    logger.handlers.clear()
logger.setLevel(logging.INFO)

def add_handler():
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)s - %(funcName)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # if not logger.handlers:
    #     logger.addHandler(ch)
    logger.addHandler(ch)

add_handler()

# %% global variables
# path2run ='..' # without last "/"
# caseName = 'OFcase'
# path2newSample = '../gpOptim/workDir/newSampledParam.dat'

# %% funcs
# def get_params(path2file):
#     """
#     Parameters
#     ----------
#     path2file : str
#         including file name

#     Returns
#     -------
#     theta : float64, size=(nPar,)
#         new sample
#     """
#     try:
#         theta = np.loadtxt("%s" % path2file, skiprows=2)
#     except:
#         logger.error("couldn't read from %s" % path2file)
#         sys.exit(1)
#     logger.info("read new sample from: %s" % path2file)
#     return theta

def write_yTopParams(Nx,Ny,Lx,Ly,theta,U_infty,t,path2case):
    """
    Parameters
    ----------
    global
    path2run, caseName
    
    theta : float64, size=(nPar,)
        output of get_params()
    
    write theta to "path2run"/"caseName"/system/yTopParams.in
    """
    try:
        scf = open('%s/system/yTopParams.in' % path2case,'w')
        for i,param in enumerate(theta):
            scf.write('theta%d %g;\n' % (i+1,param)) # start from theta1
        scf.write("Nx %d;\n" % Nx)
        scf.write("NxHalf %d;\n" % (Nx//2))
        scf.write("Ny %d;\n" % Ny)
        scf.write("NyHalf %d;\n" % (Ny//2))
        scf.write("Lx %f;\n" % Lx)
        scf.write("LxHalf %f;\n" % (Lx/2))
        scf.write("Ly %f;\n" % Ly)
        scf.write("LyHalf %f;\n" % (Ly/2))
        dx=Lx/Nx
        dt=dx/U_infty
        scf.write("dt %f;\n" % dt)
        scf.write("tEnd %d;\n" % t)
    except:
        logger.error("couldn't write to %s/system/yTopParams.in" % path2case)
        sys.exit(1)
    scf.close()
    logger.info('write new sample to: %s/system/yTopParams.in' % path2case)
