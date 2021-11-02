def Re(u, D, nu):
    """
    returns Reynolds number
    u - flow speed [m/s], 
    D - characteristic dimension [m], 
    nu - kinematic viscosity [m2/s]
    """
    return u*D/nu

def Pr(cp, eta, k):
    """
    returns Prandtl number
    cp - specific heat of the fluid,
    eta - dynamic viscosity,
    k - thermal conductivity [W/(m K)]
    """
    return cp*eta/k

def Ra(rho,beta,dT,l,g,eta,alpha):
    """
    returns Rayleigh number
    rho - density, 
    beta - th. expansion coefficient, 
    dT - temp difference across l,
    l - distance,
    g - gravitational acceleration,
    eta - dynamic viscosity,
    alpha - thermal diffusivity
    """
    return rho*beta*dT*l**3*g/(eta*alpha)

def Ra(Gr, Pr):
    return Gr*Pr

def Gr(g, beta, Tw, Tinf, L, nu):
    """
    returns Grashof number
    g - acceleration due to Earth's gravity
    beta - the coefficient of thermal expansion
    Tw - the surface temperature
    Tinf - the bulk temperature
    L - char. dim.
    nu - kinematic viscosity.
    """
    return g*beta*(Tw-Tinf)*L**3/nu**2