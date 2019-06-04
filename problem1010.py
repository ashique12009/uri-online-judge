product1 = list(map(float, input().split()))
product2 = list(map(float, input().split()))
#product 1 total price
product1TotalPrice = product1[1] * product1[2]
#product 2 total price
product2TotalPrice = product2[1] * product2[2]
cartTotal = product1TotalPrice + product2TotalPrice
print("VALOR A PAGAR: R$ " + str("{:.2f}".format(cartTotal)))