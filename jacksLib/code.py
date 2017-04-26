def do_something(kepMag):

    """
    this function estimates a flux value in electron counts per second given a Kepler magnitude,
    
    
    It uses the zero point suggested in the Kepler instrument handbook.
    
    Parameters
    ----------
    kepMag : float
        pass a kepler magnitude to the function
        
    Returns
    -------
    float
        Returns kepler flux in electron counts per second 
    """ # complete
    #def kepMag_to_flux(kepMag):
    f12 = 1.74*10**5
    f_kep = 10**(-0.4*(kepMag-12))*f12
    return f_kep
