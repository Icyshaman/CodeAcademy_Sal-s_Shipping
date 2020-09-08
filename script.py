def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.50 + 20
  elif weight > 2 and weight <= 6:
    return weight * 3.0 + 20
  elif weight > 6 and weight <= 10:
    return weight * 4.0 + 20
  else:
    return weight * 4.75 + 20
print(ground_shipping(8.4))

premium_ground_shipping = 125.0

def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight > 2 and weight <= 6:
    return weight * 9.0
  elif weight > 6 and weight <= 10:
    return weight * 12.0
  else:
    return weight * 14.25
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  gs = ground_shipping(weight)
  ds = drone_shipping(weight)
  if gs < ds and gs < premium_ground_shipping:
    return 'The cheapest way to ship '+str(weight)+' pound package is using ground shipping and it will cost $'+str(gs)+'.'
  elif ds < gs and ds < premium_ground_shipping:
    return 'The cheapest way to ship '+str(weight)+' pound package is using drone shipping and it will cost $'+str(ds)+'.'
  else:
    return 'The cheapest way to ship '+str(weight)+' pound package is using premium ground shipping and it will cost $'+str(premium_ground_shipping)+'.'

print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))