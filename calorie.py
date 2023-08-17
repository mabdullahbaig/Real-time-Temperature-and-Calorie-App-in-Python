from temp import temp   #This is the main class.....
class Calorie:
    def __init__(self,weight,height,age,temp):
        self.weight=weight
        self.height=height
        self.age=age
        self.temperature=temp

    def calculate(self):
        result = 10*self.weight+6.5*self.height +5 -self.temperature*10
        return result

if __name__=="__main__":
    country = input("Country: ").lower()
    city = input("City: ").lower()
    weight = int(input("Weight(in kg): "))
    height = float(input("Height(in cm): "))
    age = int(input("Age: "))
    temperature = temp(country,city).get()
    calorie = Calorie(weight ,height ,age ,temp=temperature)
    print("You need ",calorie.calculate(), "KCal","per day")
    print("Temperature of ",country,"(",city,") is",temperature, "°C")
