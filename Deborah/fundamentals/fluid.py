import CoolProp.CoolProp as CP
from .. fundamentals import charNumbers as CN
from .. fundamentals.converter import viscosity as vis

class fluid:
    '''
    Class to manipulate with properties of fluids.    

    References
    ----------
    [coolprop]
    '''
    def __init__(self, **i):
        '''
        Parameters
        ----------
    
        F : string
        p : float
        T : float
        
        
        References
        ----------
        [coolprop]
        '''
        self.F = i['F']
        self.T = i['T']
        self.p = i['p']

        self.rho = self.prop('D')
        self.eta = self.prop('V')
        self.nu = vis.eta2nu(self.eta, self.rho)
        self.k = self.prop('L')
        self.cp = self.prop('C')

        self.Pr = CN.Pr(self.cp, self.eta, self.k)

    def prop(self, s):
        return CP.PropsSI(s,'P', self.p, 'T', self.T, self.F)


