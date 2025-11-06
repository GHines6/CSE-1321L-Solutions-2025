
print("[Electrical Energy Consumption Calculator]")
volts = int(input("Enter the voltage (in volts): "))
resistance = int(input("Enter the resistance (in ohms): "))
time = int(input("Enter the time the device was used (in hours): "))
conversion_factor = int(1000)
energy = float(float(volts * volts) * time) / float(resistance * conversion_factor)
print(f"The device consumed {round(float(energy), 2)} kWh of energy.")
