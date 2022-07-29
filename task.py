benz = {"price":5500000,"fuel":"petrol","top_speed_in_km":250,"seater":5,"gear_type":"automatic"}
swift = {"price":592000,"fuel":"petrol","top_speed_in_km":165,"seater":5,"gear_type":"manual"}
scorpion = {"price":1653000,"fuel":"disel","top_speed_in_km":165,"seater":7,"gear_type":"manual"}

price = int(input())
fuel = (input())
top_speed_in_km =int(input())
seater = input(int())
gear_type = input(str())
if("price">=5500000):
        print("cars avilable")
if(fuel=="disel"):
        print(scorpion)
else:
    print("two models available")
if(fuel=="petrol" and top_speed_in_km==250):
        print(benz)
