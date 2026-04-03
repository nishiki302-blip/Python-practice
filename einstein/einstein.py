light_speed = 300000000 # light_speed = c
mass = int(input("m: ")) # mass = m

def main():
    #conversion of energy from mass
    energy = mass_to_energy(mass)
    print(f"E: {energy}")

# c square 
def square_light_speed(c):
    return c * c

# m to E(energy)
def mass_to_energy(m):
    # E = m * c square
    return m * square_light_speed(light_speed) 

main()