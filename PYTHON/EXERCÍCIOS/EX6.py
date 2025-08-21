metro = float(input("Digite uma distância em metros:"))
print("A medida de {}m corresponde a:".format(metro))
print("{}km \n {}hm \n {}dm \n {}cm \n {}mm".format(metro/1000, metro/100, metro*10, metro*100, metro*1000))