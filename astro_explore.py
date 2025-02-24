"""
Exploring the details of this repo; 2025-02-23.
"""

import Astrodynamics as adx


def test_scratch():
    """
    Walk thru author's code.
    """
    sun = {
        "name": "Sun",
        "color": "yellow",  # Not required; useful for plotting
        "radius": 6.957e8,
        "mass": 1.98847e30,
    }
    earth = {
        "name": "Earth",
        "color": "g",
        "e": 0.0167086,
        "a": 149598023000,
        "inc": {"sun_eq": 7.155, "ecliptic": 0.00005, "invariable_plane": 1.57869},
        "long_asc_node": -11.26064,
        "arg_periapsis": 114.20783,
        "radius": 6371000,
        "mass": 5.97217e24,
    }
    moon = {
        "name": "Moon",
        "color": "grey",
        "e": 0.0549,
        "a": 384399000,
        "inc": {"sun_eq": 0, "ecliptic": 5.145, "invariable_plane": 0},
        "radius": 1737400,
        "mass": 7.342e22,
    }
    
    # create Body object: Sun
    Sun = adx.Body(sun)
    # figure out object attributes
    attr_vars = vars(Sun)
    print(f"Sun Body object attr_vars:\n{attr_vars}")
    # figure out object methods
    method_list = [method for method in dir(Sun) if callable(getattr(Sun, method))]
    print(f"Sun object method_list:\n{method_list}")
    
    # create system object: Sun
    ems = adx.System(Sun)  # end result to be earth, moon, sun
    # figure out object attributes
    attr_vars = vars(ems)
    print(f"\nems object attr_vars:\n{attr_vars}")
    # figure out object methods
    ems_method_list = [method for method in dir(ems) if callable(getattr(ems, method))]
    print(f"ems object method_list:\n{ems_method_list}")
    
    
    # add earth to ems system
    ems.add_satellite(adx.Body(earth), earth)
    # figure out object attributes
    attr_vars = vars(ems)
    print(f"\nems object attr_vars:\n{attr_vars}")
    # object methods remain the same as above
    
    # add moon to earth orbit
    ems.satellites["Earth"].add_satellite(adx.Body(moon), moon)
    # figure out object attributes
    attr_vars = vars(ems.satellites["Earth"])
    print(f"\nems object attr_vars:\n{attr_vars}")
    
    # simulate and print works ok, but not unambiguous (to me)
    # ems.satellites["Earth"].simulate(23)
    # ems.satellites["Earth"].plot_simulation("3d", scale="Mm")
    return


def main():  # just a placeholder to help with editor navigation:--)
    pass  # avoids getting an error when empty code is not allowed


if __name__ == "__main__":
    test_scratch()  # 2025-02-03, works, but not sure of the results
    main()
