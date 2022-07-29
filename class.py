class Computer:
    def config(self):
        print("i3,16gb,1tb")

com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)