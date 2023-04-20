from temperatureGet import weather_info

absolute_pressure = 101325
temperature = weather_info["features"][0]["properties"]["timeSeries"][1]["screenTemperature"]
specific_gas_constant = 287
#values needed for air density

def air_density (absolute,temp,gas):
    answer = gas*temp
    answer = absolute/answer
    return answer

air_density = air_density(absolute_pressure,temperature,specific_gas_constant)

