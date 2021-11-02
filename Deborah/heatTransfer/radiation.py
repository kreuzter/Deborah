def radiation(T, eps):
    '''
    
    Parameters
    ----------
    
    T : float
        Thermodynamic temperature [K]
    
    eps : float
        emissivity [-]
        polished metals: 0.02 - 0.2
        anodized aluminum: 0.82
        black paint: 0.98
        white paint: 0.9
        water: 0.96
        vegetation: 0.92 - 0.96

    Returns
    -------
    
    float
        energy emitted from m^2 of by radiation
    
    References
    ----------
    eps from [cengel_2020]
    '''
    return eps*5.67e-8*T**4