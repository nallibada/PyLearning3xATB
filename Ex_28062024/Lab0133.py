class Dog:
    _name = None
    _id = None
    def __init__(self, name="No one", id=0):
        self._name = name
        self._id = id

    def sleep(self):
        print(f'{self._name} is sleeping who has the id : {self._id}')

dog1=Dog("kittu",1)
dog1.sleep()

dog2=Dog("Gauri",2)
dog2.sleep()

dog3=Dog()
dog3.sleep()

