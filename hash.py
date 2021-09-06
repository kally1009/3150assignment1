import time
import math

# Bart's way -->line by line.


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
        return self.mSSN == other.mSSN

    def __gt__(self, other):
        return self.mSSN > other.mSSN

    def __lt__(self, other):
        return self.mSSN < other.mSSN

    def __int__(self):
        return int(self.mSSN.replace('-', ''))


def isPrime(x):
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
    gTotalAge += (s.getAge())
    tcount += 1
    return gTotalAge


def main():
    # insert
    count = 0
    item = Hash(300000)
    fin = open("InsertNamesMedium.txt", "r")
    start = time.time()
    for line in fin:
        words = line.split()
        s_object = Student(words[0], words[1], words[2], words[3], words[4])
        insert_status = item.Insert(s_object)
        if insert_status == False:
            count += 1
    print("Number of Duplicate Students: ", count)
    end = time.time()
    insertTime = end-start
    print("It took ", insertTime, "seconds to insert students")
    fin.close()

    # traverse
    global gTotalAge, tcount
    start3 = time.time()
    item.Traverse(addAges)
    end3 = time.time()
    total3 = end3-start3
    avg_age = gTotalAge / tcount
    print("Total time to traverse is ", total3, "seconds.")
    print("average age from traverse is", avg_age)

    dne_count = 0
    start2 = time.time()
    fin = open("DeleteNamesMedium.txt", "r")
    for line in fin:
        ssn_delete = line.strip()
        s3 = Student("", "", ssn_delete, "", "0")
        s4 = item.Delete(s3)
        if s4 == False:
            dne_count += 1
    end2 = time.time()
    total2 = end2-start2
    print(dne_count, "student(s) does not exist")
    print("It took ", total2, "seconds to delete students")
    fin.close()

    start1 = time.time()
    totalAge = 0
    totalCount = 0
    dne_count1 = 0
    fin = open("RetrieveNamesMedium.txt", "r")
    for line in fin:
        ssn = line.strip()
        s = Student("", "", ssn, "", "0")
        s2 = item.Retrieve(s)
        if s2 is None:
            dne_count1 += 1
        else:
            totalAge += (s2.getAge())
            totalCount += 1
    end1 = time.time()
    total1 = end1-start1
    print("Total time to retrieve was ", total1, "seconds.")
    print("Could not retireve", dne_count1, "students")
    print("Average age of retrieved students is", totalAge/totalCount)
    fin.close()


main()
