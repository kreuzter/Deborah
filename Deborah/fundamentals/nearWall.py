from os import error
import numpy as np

def f2Cf(f):
    '''
    converts Darcy friction factor to Fanning friction factor
    
    Parameters
    ----------
    
    f : float
        Darcy friction factor [-]
    
    Returns
    -------
    
    float
        Fanning friction factor [-]
    
    '''
    return f/4

def f(Re, eps, D, Ed = 'H'):
    ''' 
    Parameters
    ----------
    
    Re : float
        Reynolds number [-]
    
    eps : float
        - surface roughness [m] +/- 60 %: 
            - commercial steel    : 0.0450e-3 
            - stainless steel     : 0.0020e-3 
            - copper/brass tubing : 0.0015e-3 
            - glass (smooth)      : 0.
    
    D : float
        char. dim. [m]

    Ed : str/float, optional
        if default, Haalands approximation is used, 
        else value of maximum error
    
    Returns
    -------
    
    float
        Darcy friction factor [-]

    Raises
    ------
    
    error
        If limit of maximum steps (100) was reached and E is still > Ed.

    assertionError
        - Ed is not 'H' or float
        - Ed > 1e-2 (this is an approximate error of Haaland equation)
    
    References
    ----------
    approximation for Ed == 'H' [haaland_1983], 
    else Colebrook equation (+ [haaland_1983] as a first guess),
    eps table [cengel_2020]
    '''
    maxSteps = 100
    pomO = -1.8*np.log10(6.9/Re+(eps/D/3.7)**1.11)
    if Ed == 'H':
        pass
    else:
        assert (type(Ed) == float)
        assert (Ed < 1e-2)
        i = 0
        E = Ed + 1
        while E >= Ed and i <= maxSteps:
            pom = -2.*np.log10(eps/D/3.7+2.51*pomO/Re)
            E = np.abs(np.abs(pom) - np.abs(pomO))/pom
            pomO = pom
            i = i+1
        if i == maxSteps:
            raise error('Limit of maximum steps was reached and E is still > Ed.')
    return pomO**(-2)

def dp(f, L, u, rho, D):
    '''
    dp [summary]
    
    Parameters
    ----------
    
    f : float
        Darcy friction factor [-]
    
    L : float
        lenght [m]
    
    u : float
        mean velocity [m/s]

    rho : float
          density [kg/m3]
    
    D : float
        char. dim. [m]

    Returns
    -------
    
    float
        pressure loss [m]
    
    '''

    return f*L*rho*u**2/D/2

def nearWallThickness(nu, uTau, yp):
    return nu*yp/uTau

def wallShearStress(Cf,rho,u):
    '''  
    Parameters
    ----------
    
    Cf : float
        Fanning friction factor [-]
    
    rho : float
        density [kg/m3]
    
    u : float
        Free stream velocity [m/s]
    
    Returns
    -------
    
    float
        Tau [Pa] - Wall Shear Stress
    
    '''
    return Cf*rho*u**2/2

def yp(uTau, y, kinVis):
    return uTau*y/kinVis


def shearVelocity(Tau, rho):
    '''   
    Parameters
    ----------
    
    Tau : float
        Wall Shear Stress [Pa] 
    
    rho : float
        density [kg/m-3]

    Returns
    -------
    
    float
        Shear Velocity u_Tau [m/s]
    
    '''
    return np.sqrt(Tau/rho)