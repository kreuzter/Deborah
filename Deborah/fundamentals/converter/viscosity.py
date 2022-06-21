def nu2eta(nu, rho):
    """
    returns dynamic viscosity

    Parameters
    ----------

    nu - kinematic viscosity 

    rho - density
    """
    return nu*rho

def eta2nu(eta, rho):
    """
    returns kinematic viscosity
    
    Parameters
    ----------
    
    eta - dynamic viscosity,
     
    rho- density
    """
    return eta/rho