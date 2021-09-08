#Code Originally written by Kalicia Adams. Some Modifications made by Kalicia Adams and Jandir Porta.
import time
import math
class Student:
    def __init__(self, firstName, lastName, SSN, email, age):
        self.mfirstName = firstName
        self.mlastName = lastName
        self.mSSN = SSN
        self.memail = email
        self.mage = int(age)

    def getSSN(self):
        return self.mSSN

    def getFirstName(self):
        return self.mfirstName

    def getLastName(self):
        return self.mlastName

    def getEmail(self):
        return self.memail

    def getAge(self):
        return self.mage

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.mSSN == other.mSSN

    def __gt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.mSSN > other.mSSN

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.mSSN < other.mSSN

    def __int__(self):
        return int(self.mSSN.replace('-', ''))


def isPrime(x):
    if x==None:
        return None
    elif type(x) == float:
        return False
    elif type(x) == str:
        return False
    elif x <= 1:
        return False
    s = int(math.sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True


class Hash:
    def __init__(self, neededsize):
        actualsize = 2*neededsize+1
        while not isPrime(actualsize):
            actualsize += 2
        self.mTable = []
        for i in range(actualsize):
            self.mTable.append(None)
        self.mSize = 0

    def Insert(self, item):
        if self.Exists(item):
            return False
        key = int(item)  # override int method in init
        index = key % len(self.mTable)
        while self.mTable[index]:
            index += 1
            if index >= len(self.mTable):
                index = 0
        self.mTable[index] = item
        self.mSize += 1
        return True

    def Retrieve(self, item):
        if not self.Exists(item):
            return None
        key = int(item)
        index = key % len(self.mTable)
        while True:
            if self.mTable[index] and self.mTable[index] == item:
                return self.mTable[index]
            index += 1
            if index >= len(self.mTable):
                index = 0

    def Exists(self, item):
        if not item:
            return None
        key = int(item)
        index = key % len(self.mTable)
        while True:
            if self.mTable[index] is None:
                return False
            if self.mTable[index] and self.mTable[index] == item:
                return True
            index += 1
            if index >= len(self.mTable):
                index = 0

    def Traverse(self, callbackFunction):
        for i in self.mTable:
            if i:
                callbackFunction(i)

    def Delete(self, item):
        if not item:
            return None
        if not isinstance(item, Student):
            return False
        if not self.Exists(item):
            return False
        key = int(item)
        index = key % len(self.mTable)
        while self.mTable[index] and self.mTable[index] != item:
            index += 1
            if index >= len(self.mTable):
                index = 0
        self.mTable[index] = False
        self.mSize -= 1
        return True

    def size(self):
        return self.mSize


gTotalAge = 0
tcount = 0


def addAges(s):
    global gTotalAge, tcount
    if type(s) is int:
        return False
    elif type(s) is str:
        return False
    elif type(s) is None:
        raise Exception("Can't be None")
    elif s.getAge() == None:
        raise Exception("Age can't be none")
    gTotalAge += (s.getAge())
    tcount += 1
    return gTotalAge