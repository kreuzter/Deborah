import numpy as np

def pipe(Re, Pr, Cf):
    '''
    Correlation for turbulent pipe flow, forced convection.
    
    Parameters
    ----------
    Re : float
        Reynolds number [-], see Deborah.fundamentals.charNumbers
    Pr : float
        Prandtl number [-], see Deborah.fundamentals.charNumbers
    Cf : float
        Fanning friction factor (skin friction factor) [-], see Deborah.fundamentals.friction
    
    Returns
    -------
    float
        Nusselt number [-]
    
    References
    ----------
    [gnielinski_1976]
    '''

    assert (2300 < Re < 5e6 and 0.5 < Pr < 2300)
    
    if 2300 < Re < 5e6 and 0.5 < Pr < 2300:
        Nu = (Re-1000)*Pr*Cf/2/(1+12.7*np.sqrt(Cf/2)*(Pr**(2/3)-1))
    
    return Nu
