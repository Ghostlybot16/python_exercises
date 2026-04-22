from math import pi

def circ_area(r):
    """Returns area of a circle
    
    Parameters:
        r (int): The radius value to use to find area 
    
    Returns: 
        (float) Area of circle
    """
    return round(pi * r**2, 4) 
    

radius = float(input("Radius: ")) # Store user input

area = circ_area(radius)   

print(f"Area: {area}") # Terminal output 