# https://www.codewars.com/users/sajjad-salam




def rental_car_cost(d):
    cost=40*d
    if d>=7:
        cost=cost-50
      
    elif d>3:
        cost=cost-20
    return cost      
    
   
   
s=rental_car_cost(4)
print(s)    