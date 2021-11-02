def nu2eta(nu, rho):
    """
    returns dynamic viscosity
    nu - kinematic viscosity 
    rho - density
    """
    return nu*rho

def eta2nu(eta, rho):
    """
    returns kinematic viscosity
    eta - dynamic viscosity, 
    rho- density
    """
    return eta/rho