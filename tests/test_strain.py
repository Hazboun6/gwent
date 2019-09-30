#!/usr/bin/env python
# coding: utf-8

import numpy as np

import pytest

import astropy.constants as const
import astropy.units as u

import gwent
from gwent import detector
from gwent import binary

load_directory = gwent.__path__[0] + '/LoadFiles/InstrumentFiles/'

# ####################################################################
# # Initialize different instruments

# ### aLIGO

Ground_T_obs = 4*u.yr


#aLIGO
@pytest.fixture
def aLIGO():
    aLIGO_filedirectory = load_directory + 'aLIGO/StrainFiles/'
    aLIGO_filename = 'aLIGODesign.txt'
    aLIGO_filelocation = aLIGO_filedirectory + aLIGO_filename

    aLIGO = detector.GroundBased('aLIGO',Ground_T_obs,
                                 load_location=aLIGO_filelocation,I_type='A')
    return aLIGO

#Einstein Telescope
@pytest.fixture
def ET():
    ET_filedirectory = load_directory + 'EinsteinTelescope/StrainFiles/'
    ET_filename = 'ET_B_data.txt'
    ET_filelocation = ET_filedirectory + ET_filename

    ET = detector.GroundBased('ET',Ground_T_obs,
                              load_location=ET_filelocation,I_type='A')
    return ET

SpaceBased_T_obs = 4*u.yr
LISA_Other_filedirectory = load_directory + 'LISA_Other/StrainFiles/'

#### LISA Example 1
#Modelled off of the Science Requirements document from https://lisa.nasa.gov/documentsReference.html.
def test_LISA_ex1():
    LISA_Other_filedirectory = load_directory + 'LISA_Other/StrainFiles/'
    LISA_ex1_filename = 'LISA_Allocation_S_h_tot.txt'
    LISA_ex1_filelocation = LISA_Other_filedirectory + LISA_ex1_filename

    #`I_type` should be Effective Noise Spectral Density
    LISA_ex1 = detector.SpaceBased('LISA Example 1',SpaceBased_T_obs,
        load_location=LISA_ex1_filelocation,I_type='E')

#### LISA Example 2
#Modelled off of Robson,Cornish,and Liu 2018, LISA (https://arxiv.org/abs/1803.01944).
def test_LISA_ex2():
    LISA_ex2_filedirectory = load_directory + '/InstrumentFiles/LISA_Other/StrainFiles/'
    LISA_ex2_filename = 'LISA_sensitivity.txt'
    LISA_ex2_filelocation = LISA_ex2_filedirectory + LISA_ex2_filename

    #`I_type` should be Effective Noise Spectral Density
    LISA_ex2 = detector.SpaceBased('LISA Example 2',SpaceBased_T_obs,
        load_location=LISA_ex2_filelocation,I_type='E')

#### LISA Example 3
#Generated by http://www.srl.caltech.edu/~shane/sensitivity/
def test_LISA_Larson():
    LISA_Other_filedirectory = load_directory + 'LISA_Other/StrainFiles/'
    LISA_ex3_filename = 'scg_6981.dat'
    LISA_ex3_filelocation = LISA_Other_filedirectory + LISA_ex3_filename

    #`I_type` should be Amplitude Spectral Density
    LISA_ex3 = detector.SpaceBased('LISA Example 3',SpaceBased_T_obs,
        load_location=LISA_ex3_filelocation,I_type='A')

#### Simulated NANOGrav Continuous Wave Detection Sensitivity
#Samples from Mingarelli, et al. 2017 (https://arxiv.org/abs/1708.03491) 
#of the Simulated NANOGrav Continuous Wave Detection Sensitivity.

NANOGrav_filedirectory = load_directory + 'NANOGrav/StrainFiles/'

#NANOGrav continuous wave sensitivity
NANOGrav_background = 4e-16 # Unsubtracted GWB amplitude: 0,4e-16
NANOGrav_dp = 0.95 #Detection Probablility: 0.95,0.5
NANOGrav_fap = 0.0001 #False Alarm Probability: 0.05,0.003,0.001,0.0001
NANOGrav_Tobs = 15 #Observation years: 15,20,25

NANOGrav_filename = 'cw_simulation_Ared_' + str(NANOGrav_background)
NANOGrav_filename += '_dp_' + str(NANOGrav_dp) + '_fap_' + str(NANOGrav_fap)
NANOGrav_filename += '_T_' + str(NANOGrav_Tobs) + '.txt'
NANOGrav_filelocation = NANOGrav_filedirectory + NANOGrav_filename

def test_pta_NANOGrav_cw_no_GWB():
    NANOGrav_cw_no_GWB = detector.PTA('NANOGrav CW Detection no GWB',
        load_location=NANOGrav_filelocation)

#NANOGrav continuous wave sensitivity
NANOGrav_background_2 = 0 # Unsubtracted GWB amplitude: 0,4e-16
NANOGrav_dp_2 = 0.95 #Detection Probablility: 0.95,0.5
NANOGrav_fap_2 = 0.0001 #False Alarm Probability: 0.05,0.003,0.001,0.0001
NANOGrav_Tobs_2 = 15 #Observation years: 15,20,25

NANOGrav_filename_2 = 'cw_simulation_Ared_' + str(NANOGrav_background_2)
NANOGrav_filename_2 += '_dp_' + str(NANOGrav_dp_2)
NANOGrav_filename_2 += '_fap_' + str(NANOGrav_fap_2) + '_T_'
NANOGrav_filename_2 += str(NANOGrav_Tobs_2) + '.txt'
NANOGrav_filelocation_2 = NANOGrav_filedirectory + NANOGrav_filename_2

def test_pta_NANOGrav_cw_GWB():
    NANOGrav_cw_GWB = detector.PTA('NANOGrav CW Detection no GWB',
        load_location=NANOGrav_filelocation_2)

#### NANOGrav Continuous Wave 11yr Upper Limit
#Sample from Aggarwal, et al. 2019 (https://arxiv.org/abs/1812.11585) of the NANOGrav 11yr continuous wave upper limit.
def test_pta_():
    NANOGrav_cw_ul_file = NANOGrav_filedirectory + 'smoothed_11yr.txt'
    NANOGrav_cw_ul = detector.PTA('NANOGrav CW Upper Limit',
        load_location=NANOGrav_cw_ul_file)

#### SKA-esque Detector
#Fiducial parameter estimates from Sesana, Vecchio, and Colacino, 2008 (https://arxiv.org/abs/0804.4476) section 7.1.

#sigma_rms timing residuals in nanoseconds to seconds
sigma_SKA = 10*u.ns.to('s')*u.s
T_SKA = 15*u.yr #Observing time in years
N_p_SKA = 20 #Number of pulsars
#Avg observation cadence of 1 every week in [number/yr]
cadence_SKA = 1/(u.wk.to('yr')*u.yr)

#SKA with White noise only
@pytest.fixture
def SKA_WN():
    SKA_WN = detector.PTA('SKA, WN Only',
        T_SKA,N_p_SKA,sigma_SKA,cadence_SKA)
    return SKA_WN

#SKA with White and Varied Red Noise
def test_pta_SKA_WN_RN():
    SKA_WN_RN = detector.PTA('SKA, WN and RN',
        T_SKA,N_p_SKA,sigma_SKA,cadence_SKA,
        A_rn=[1e-16,1e-12],alpha_rn=[-3/4,1])

#SKA with White Noise and a Stochastic Gravitational Wave Background
def test_pta_SKA_WN_GWB():
    SKA_WN_GWB = detector.PTA('SKA, WN and GWB',
        T_SKA,N_p_SKA,sigma_SKA,cadence_SKA,
        A_GWB=4e-16)

#### NANOGrav-esque Detector
#Fiducial 11yr parameter estimates from Arzoumanian, et al., 2018 https://arxiv.org/abs/1801.01837

#rms timing residuals in nanoseconds to seconds
sigma_nano = 100*u.ns.to('s')*u.s
T_nano = 15*u.yr #Observing time in years
N_p_nano = 18 #Number of pulsars
#Avg observation cadence of 1 every 2 weeks in number/year
cadence_nano = 1/(2*u.wk.to('yr')*u.yr)

#NANOGrav with White Noise only
def test_pta_NANOGrav_WN():
    NANOGrav_WN = detector.PTA('NANOGrav, WN Only',
        T_nano,N_p_nano,sigma_nano,cadence_nano)

#NANOGrav with White and Varied Red Noise
def test_pta_NANOGrav_wRN():
    NANOGrav_WN_RN = detector.PTA('NANOGrav, WN and RN',
        T_nano,N_p_nano,sigma_nano,cadence_nano,
        A_rn=[1e-16,1e-12],alpha_rn=[-3/4,1])

#NANOGrav with White Noise and a Stochastic Gravitational Wave Background
def test_pta_NANOGrav_WN_GWB():
    NANOGrav_WN_GWB = detector.PTA('NANOGrav, WN and GWB',
        T_nano,N_p_nano,sigma_nano,cadence_nano,
        A_GWB=4e-16)


# ####################################################################
# # Calculate LISA amplitude spectral densities for various models

L = 2.5*u.Gm  #armlength in Gm
L = L.to('m')
LISA_T_obs = 4*u.yr

#### LISA Proposal 1
#Values taken from the ESA L3 proposal, Amaro-Seaone, et al., 2017 (https://arxiv.org/abs/1702.00786)
f_acc_break_low = .4*u.mHz.to('Hz')*u.Hz
f_acc_break_high = 8.*u.mHz.to('Hz')*u.Hz
f_IMS_break = 2.*u.mHz.to('Hz')*u.Hz
A_acc = 3e-15*u.m/u.s/u.s
A_IMS = 10e-12*u.m

Background = False

@pytest.fixture
def LISA_prop1():
    LISA_prop1 = detector.SpaceBased('LISA',
                          LISA_T_obs,L,A_acc,f_acc_break_low,
                          f_acc_break_high,A_IMS,f_IMS_break,
                          Background=Background)
    return LISA_prop1

#### LISA Proposal 2
#Values from Robson, Cornish, and Liu 2019 https://arxiv.org/abs/1803.01944 using the Transfer Function Approximation within.
f_acc_break_low = .4*u.mHz.to('Hz')*u.Hz
f_acc_break_high = 8.*u.mHz.to('Hz')*u.Hz
f_IMS_break = 2.*u.mHz.to('Hz')*u.Hz
A_acc = 3e-15*u.m/u.s/u.s
A_IMS = 1.5e-11*u.m
Background = False

def test_LISA_prop2():
    LISA_prop2 = detector.SpaceBased('LISA Approximate',
                           LISA_T_obs,L,A_acc,f_acc_break_low,
                           f_acc_break_high,A_IMS,f_IMS_break,
                           Background=Background,T_type='A')

# #######################################################################
# # BBH strain calculation

#Vars = [M,q,chi1,chi2,z]
M = [1e6,65.0,1e10]
q = [1.0,18.0,1.0]
x1 = [0.95,0.0,-0.95]
x2 = [0.95,0.0,-0.95]
z = [3.0,0.093,20.0]

def test_BBHStrain(ESA_LISA,aLIGO,SKA_Hazboun,ET):
    source_1 = binary.BBHFrequencyDomain(M[0],q[0],z[0],x1[0],x2[0],
        instrument=LISA_prop1)
    source_2 = binary.BBHFrequencyDomain(M[1],q[1],z[1],x1[1],x2[1],
        instrument=aLIGO)
    source_3 = binary.BBHFrequencyDomain(M[2],q[2],z[2],x1[2],x2[2],
        instrument=SKA_WN)
    source_4 = binary.BBHFrequencyDomain(M[1],q[0],z[1],x1[1],x2[1],
        instrument=ET)


# ### Numerical Relativity from EOB subtraction

EOBdiff_filedir = gwent.__path__[0] + '/LoadFiles/DiffStrain/EOBdiff/'

def test_NR_EOB():
    diff0002 = binary.BBHTimeDomain(M[1],q[0],z[1],
        load_location=EOBdiff_filedirectory+'diff0002.dat')
    diff0114 = binary.BBHTimeDomain(M[1],q[0],z[1],
        load_location=EOBdiff_filedirectory+'diff0114.dat')
    diff0178 = binary.BBHTimeDomain(M[1],q[0],z[1],
        load_location=EOBdiff_filedirectory+'diff0178.dat')
    diff0261 = binary.BBHTimeDomain(M[1],q[0],z[1],
        load_location=EOBdiff_filedirectory+'diff0261.dat')
    diff0303 = binary.BBHTimeDomain(M[1],q[0],z[1],
        load_location=EOBdiff_filedirectory+'diff0303.dat')
