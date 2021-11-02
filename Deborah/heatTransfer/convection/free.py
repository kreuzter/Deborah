def cylinderH(Ra, Pr):
    '''
    free convection, horizontal cylinder
    
    Parameters
    ----------
    
    Ra : float
        Rayleigh number, see Deborah.fundamentals.charNumbers
    
    Pr : float
        Prandtl number, see Deborah.fundamentals.charNumbers
        
    Returns
    -------
    
    float
        Nusselt number
    
    References
    ----------
    Ra <= 1e12: [churchill_1975]
    '''

    assert (Ra <= 1e12)
    if Ra <= 1e12:
        Nu = (0.6+0.387*Ra**(1/6)/(1+(0.559/Pr)**(9/16))**(8/27))**2

    return Nu

def cylinderV(Ra, Pr, Gr, D, L):
    '''
    free convection, vertical cylinder
    
    Parameters
    ----------
    
    Ra : float
        Rayleigh number
    
    Pr : float
        Prandtl number
    
    Gr : float
        [description]
    
    D : float
        [description]
    
    L : float
        [description]
        
    Returns
    -------
    
    float
        Nusselt number
    
    References
    ----------
    D >= 35*L/Gr**(0.25): [cebeci_1974]
    '''

    assert (D >= 35*L/Gr**(0.25))
    if D >= 35*L/Gr**(0.25):
        Nu = wallV(Ra, Pr)

    return Nu

def wallV(Ra, Pr):
    '''
     free convection, vertical wall
    
    Parameters
    ----------
    
    Ra : float
        Rayleigh number [-]
    
    Pr : float
        Prandtl number

    Returns
    -------
    
    float
        Nusselt number
    
    References
    ----------
    Ra <= 1e12 and Ra >=0.1: [churchill_1975a]
    '''
    assert (Ra <= 1e12 and Ra >=0.1)
    if Ra <= 1e12 and Ra >=0.1:
        Nu = (0.825 + 0.387*Ra**(1/6)/(1+(0.492/Pr)**(9/16))**(8/27))**2

    return Nu

def plateH(Ra, dir):
    '''
    free convection, horizontal plate
    
    Parameters
    ----------
    
    Ra : float
        Rayleigh number [-]
    
    dir : string
        uppper surface: dir == 'u'
        lower surface: dir == 'l'
    
    Returns
    -------
    
    float
        Nusselt number
    
    Note
    ----
    char. lenght = surfaceArea / perimeter

    References
    ----------
    u: 1e4 <= Ra <= 1e11 [cengel_2020]
    l: 1e5 <= Ra <= 1e11 [cengel_2020]
    '''

    assert (dir == 'u' or dir == 'l')

    if dir == 'u':
        assert (1e4 <= Ra <= 1e11)
        if 1e4 <= Ra <= 1e7:
            Nu = 0.54*Ra**0.25
        elif 1e7 <= Ra >= 1e11:
            Nu = 0.15*Ra**(1/3)
    elif dir == 'l':
        assert (1e5 <= Ra <= 1e11)
        if 1e5 <= Ra <= 1e11:
            Nu = 0.27*Ra**0.25

    return Nu
