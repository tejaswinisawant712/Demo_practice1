class Dog:  # Define Dog class
    def sound(self):  # Define method
        print("Bark")  # Print dog sound

class Cat:  # Define Cat class
    def sound(self):  # Same method name
        print("Meow")  # Print cat sound

d = Dog()  # Create Dog object
c = Cat()  # Create Cat object

d.sound()  # Call Dog method
c.sound()  # Call Cat method
