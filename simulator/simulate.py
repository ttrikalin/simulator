#import numpy as np 

import pint  
ureg = pint.UnitRegistry() 

'''
Very important!
import the pint module for units  

Usage: 

    from pint import UnitRegistry  
    u = UnitRegistry() 

    age = 45 * u.year 
    print(age.units)
    print(age.magnitude)

    # print age in days 
    print(age.to(u.day))
    # age is still measured in years 

    # change age unit in place to seconds 
    age.ito(u.second)

'''

import agents.agent as ag

def main():
    populationSize = 20
    population =[] 
    population = [ ag.Agent('agent {:0>6d}'.format(n), 'male', 35*ureg.year) for n in range(populationSize)]


    tom = population[0]
    print (tom.age)
    print (tom.cardiacSystem.heart.biscupidValve.hasProlapse)

    return population



population = main()

tom = population[0]
tom.age
tom.cardiacSystem.heart.biscupidValve.hasProlapse


