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

    assert (2300 < Re < 5e6 and 0.5 < Pr < 2300) , f'Re = {Re:.2f}, Pr = {Pr:.2f}'
    
    if 2300 < Re < 5e6 and 0.5 < Pr < 2300:
        Nu = (Re-1000)*Pr*Cf/2/(1+12.7*np.sqrt(Cf/2)*(Pr**(2/3)-1))
    
    return Nu

def circularHelical(Re, Pr, dH, D, f = 'liquid'):
    '''
    Correlation of Nu in helical circular pipe.
    
    Parameters
    ----------
    
    Re : float
        Reynolds number [-], see Deborah.fundamentals.charNumbers
    Pr : float
        Prandtl number [-], see Deborah.fundamentals.charNumbers
    
    dH : float
        hydraulical diameter [m]
    
    D : float
        diameter of helix

    f : str, optional
        options: liquid/gas, by default 'liquid'

    Returns
    -------
    
    Nu
        Nusselt number [-]
    
    References
    ----------
    [mori_1967]
    '''

    assert (Re > 2300) , f'Re = {Re:.2f}'
    dd = dH/D
    if f == 'liquid':
        assert (Pr > 1 and Re*dd**2.5 > 0.4) , f'Pr = {Pr:.2f}, Re*(d/D)**2.5 = {Re*dd**2.5:.2f}'
        Nu = Pr**0.4/41.0*Re**(5/6)*dd**(1/12)*(1+0.061/(Re*dd**2.5)**(1/6))
    elif f == 'gas':
        assert (0.5 < Pr < 5 and Re*dd**2 > 0.1) , f'Pr = {Pr:.2f}, Re*(d/D)**2 = {Re*dd**2:.2f}'
        Nu = Pr/26.2*(Pr**(2/3)-0.074)*Re**(4/5)*dd**0.1*(1+0.098/(Re*dd**2)**1/5)

    return Nu
