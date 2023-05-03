class Patient:
    def __init__(self, name, pincode, phoneNumber, is_corona):
        self.name = name
        self.pincode = pincode
        self.phoneNumber = phoneNumber
        self.is_corona = is_corona

    @property
    def getName(self):
        return self.name

    @property
    def getPincode(self):
        return self.pincode

    @property
    def getPhoneNumber(self):
        return self.phoneNumber

    @property
    def getIs_Corona(self):
        return self.is_corona


class CoronaPatient:
    def __init__(self):
        self.patient = []

    def addPatient(self, newPatient):
        self.patient.append(newPatient)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.patient) > 0:
            pat = self.patient[0]
            self.patient.pop(0)
            return pat
        else:
            raise StopIteration

    def getLessCases(self):
        pincode_dict = {}
        for p in self.patient:
            if p.getIs_Corona:
                pincode = p.getPincode
                if pincode in pincode_dict:
                    pincode_dict[pincode] += 1
                else:
                    pincode_dict[pincode] = 1

        return min(pincode_dict, key=pincode_dict.get)

    def countPositiveCase(self):
        count = 0
        for p in self.patient:
            if p.getIs_Corona:
                count += 1
        return count


patient1 = Patient("John Doe", 560001, "9999999999", False)
patient2 = Patient("Jane Doe", 560002, "8888888888", True)
patient3 = Patient("Joe Bloggs", 560003, "7777777777", True)
patient4 = Patient("Joe Bloggs", 560004, "7777777777", True)
patient5 = Patient("Joe Bloggs", 560004, "7777777777", True)
patient6 = Patient("Joe Bloggs", 560003, "7777777777", True)
patient7 = Patient("Joe Bloggs", 560004, "7777777777", True)
patient8 = Patient("Joe Bloggs", 560008, "7777777777", True)

coronaPatient = CoronaPatient()
coronaPatient.addPatient(patient1)
coronaPatient.addPatient(patient2)
coronaPatient.addPatient(patient3)
coronaPatient.addPatient(patient4)
coronaPatient.addPatient(patient5)
coronaPatient.addPatient(patient6)
coronaPatient.addPatient(patient7)
coronaPatient.addPatient(patient8)

print(coronaPatient.getLessCases())
print(coronaPatient.countPositiveCase())

for cp in coronaPatient:
    print(cp.getName)
