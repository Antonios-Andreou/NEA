from airDensity import air_density
velocity_placeholder = 1
wing_area_placeholder = 1
#GET VELOCITY / WING AREA FROM DB, ALSO ADD A TRY INCASE NO PLANES IN DATABASE SO NO CRASH


def modern_lift_equation(density,velocity,wing):
    velocity *= velocity
    answer = density*velocity
    answer /= 2
    answer *= wing
    return answer

lift = modern_lift_equation(air_density,velocity_placeholder,wing_area_placeholder)

print(lift)
