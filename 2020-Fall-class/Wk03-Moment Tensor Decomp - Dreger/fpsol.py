#function to determine the strike, rake and dip from a dc moment tensor
#(full and deviatoric moment tenors need to be decomposed first

import math
import numpy as np

def fpsol(nu,u):
    
    """
    reads the vector normal and slip vector returning strike, rake, dip
    """

    
    dip=np.arccos(-1*nu[2])
    if nu[0] ==0. and nu[1] == 0.:
        str=0.
    else:
        str=np.arctan2(-1*nu[0],nu[1])

  

    sstr=np.sin(str)
    cstr=np.cos(str)
    sdip=np.sin(dip)
    cdip=np.cos(dip)


    if abs(sdip) > 0.:
        rake=np.arcsin(-1*u[2]/np.sin(dip));
    else:
        arg1=1.
        arg2=u[2]
        arg=np.sign(arg2)
        if arg < 0.:
            rake=np.pi
        else:
            rake=0.

    slambda=np.sin(rake)
    cdsl=cdip*slambda
  
    if abs(sstr) > abs(cstr):
        clambda=(u[1]+cdsl*cstr)/sstr
    else:
        clambda=(u[0]-cdsl*sstr)/cstr

    if slambda == 0. and clambda == 0.:
        slip=0.
    else:
        slip=np.arctan2(slambda,clambda)

      
    if dip > np.pi/2:
        dip=np.pi-dip
        str=str+np.pi
        slip=2*np.pi-slip
     
    if str < 0.: 
        str=str+2*np.pi
    
    if slip >= np.pi: 
        slip=slip-2*np.pi;
    
    
    str=str*180/np.pi
    rake=slip*180/np.pi
    dip=dip*180/np.pi
    
    return str, rake, dip
