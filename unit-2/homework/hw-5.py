temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
positive_mean = 0 
negative_mean = 0 
for n in temperature_readings:
    if n > 0:
        positive_mean = positive_mean + n/6
print (f"Average of positive readings {positive_mean}")
        
for no in temperature_readings:
    if no < 0:
        negative_mean = negative_mean + no/4
print (f"Average of negative readings {negative_mean}")