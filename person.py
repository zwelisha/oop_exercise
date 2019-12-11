"""
Copyright @2019
Author: Zwelisha Mthethwa
"""
class Person():
    def __init__(this, name, age, gender, interests):
        this.name = name
        this.age = age
        this.gender = gender
        this.interests = interests

    def hello(this):
        interests = this.interests
        hello_string = "Hello, my name is " + this.name + " and I am " + str(this.age) + " years old." + " My interests are "
        for i in range(len(interests)-1):
            if i != len(interests)-2:
                hello_string += interests[i] + ", "
            else:
                hello_string += interests[i]
        hello_string += " and " + interests[-1] + "."
        return hello_string
        
def main():
    person = Person('Ryan',30,'male',['being a hardarse','agile', 'ssd hard drives'] )
    greeting = person.hello()
    print(greeting)

if __name__ == '__main__':
    main()
