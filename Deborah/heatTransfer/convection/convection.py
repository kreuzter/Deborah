from .. convection import free as free
from .. convection import forced as forced

def Nu2h(Nu, L, k):
    '''
    convective heat transfer coefficient from Nusselt number
    
    Parameters
    ----------
    
    Nu : float
        Nusselt nuber
    
    L : float
        char. lenght
    
    k : float
        thermal conductivity [W/(m K)]
    
    Returns
    -------
    
    float
        convective heat transfer coefficient [W/(m2K)]
    
    '''
    return Nu*k/L




def Nu(**i):
    '''
    Nu function contains several empirical approximations for evaluation of Nusselt number.
    For detailed info, please see also help() of heatTransfer subpackage functions.
    
    Returns
    -------
    
    float
        Nusselt number [-]

    Raises
    ------
    
    NotImplementedError
        in case that desired geometry - mechanism combination was not implemented yet.
    
    Exception
        in case that wrong mechanism was set.

    AssertionError
        in case that parameters are out of expected range.
    
    References
    ----------
    
    See references in heatTransfer subpackage
    '''


    f = i['f']
    G = i['geometry']

    if f == '*':
        Re = i['Re']
        Pr = i['Pr']
        Ra = i['Ra']

        if Ra/(Pr*Re**2) > 10:
            f = 'free'
        elif Ra/(Pr*Re**2) < 1:
            f = 'forced'
        else:
            f = 'combined'
        print(f'Using {f} convection approximations.')

    if f == 'combined':
        raise NotImplementedError('Cannot handle combined convection yet.')

    elif f == 'free':
        if G == 'cylinderH':
            Ra = i['Ra']
            Pr = i['Pr']
            Nu = free.cylinderH(Ra, Pr)

        elif G == 'cylinderV':
            D = i['D']
            L = i['L']
            Gr = i['Ra']/i['Pr']
            assert (D >= 35*L/Gr**(0.25))
            if D >= 35*L/Gr**(0.25):
                Nu = free.wallV(Ra, Pr)

        elif G == 'wallH':
            dir = i['dir']
            Ra = i['Ra']
            Nu = free.plateH(Ra, dir)

        elif G == 'wallV':
            Ra = i['Ra']
            Pr = i['Pr']
            Nu = free.wallV(Ra, Pr)

        else:
            raise NotImplementedError('Geometry was not implemented yet.')

    elif f == 'forced':
        if G == 'pipe':
            Re = i['Re']
            Pr = i['Pr']
            Cf = i['Cf']

            Nu = forced.pipe(Re, Pr, Cf)

        else:
            raise NotImplementedError('Geometry was not implemented yet.')
    
    else:
        raise Exception('Wrong mechanism.')
    
    return Nu
