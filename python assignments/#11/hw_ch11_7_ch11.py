class Patient:
    def __init__(self, id, name, gender, age, address, no, dob, height, weight):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address
        self.no = no
        self.dob = dob
        self.height = height
        self.weight = weight

    def setPatientID(self, id): 
        self.id = id
    def getPatientID(self):
        return self.id
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setGender(self, gender):
        self.gender = gender
    def getGender(self):
        return self.gender
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address
    def setPhoneNumber(self, no):
        self.no = no
    def getPhoneNumber(self):
        return self.no
    def setDOB(self, dob):
        self.dob = dob
    def getDOB(self):
        return self.dob
    def setHeight(self, height):
        self.height = height
    def getHeight(self):
        return self.height
    def setWeight(self, weight):
        self.weight = weight
    def getWeight(self):
        return self.weight
    def patient_details(self):
        print("Patient ID : ", self.id, "\nPatient Name : ", self.name, "\nGender : ", self.gender, "\nAge : ", self.age,"\nAddress : ", self.address, "\nDate of Birth : ", self.dob, "\nPhone Number : ", self.no,"\nHeight : ", self.height, "\nWeight : ", self.weight)


class Doctor:
    def __init__(self, name, regNumber, qualification, specialization, no, officeHours, location):
        self.name = name
        self.regNumber = regNumber
        self.qualification = qualification
        self.specialization = specialization
        self.no = no
        self.officeHours = officeHours
        self.location = location

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setRegNumber(self, regNumber):
        self.RegNumber = regNumber
    def getRegNumber(self):
        return self.regNumber
    def setQualification(self, qualification):
        self.qualification = qualification
    def getQualification(self):
        return self.qualification
    def setSpecialization(self, specialization):
        self.specialization = specialization
    def getSpecialization(self):
        return self.specialization
    def setPhoneNumber(self, no):
        self.no = no
    def getPhoneNumber(self):
        return self.no
    def setOfficeHours(self, officeHours):
        self.officeHours = officeHours
    def getOfficeHours(self):
        return self.officeHours
    def setOfficeLocation(self, location):
        self.location = location
    def getOfficeLocation(self):
        return self.location
    def doctorDetails(self):
        print("Doctor's ID : ", self.regNumber, "\nDoctor's Name : ", self.name, "\nQualification : ", self.qualification,"\nSpecialization : ", self.specialization, "\nPhone Number : ", self.no,"\nOffice Hours : ", self.officeHours, "\nOffice Location : ", self.location)


class PatientMedicalRecord:
    def __init__(self, prevCheckupDate, doctorID, id, heathProblem, medication, charges, report):
        self.prevCheckupDate = prevCheckupDate
        self.doctorID = doctorID
        self.id = id
        self.heathProblem = heathProblem
        self.medication = medication
        self.charges = charges
        self.report = report
    def setprevCheckUpDate(self, prevCheckupDate):
        self.prevCheckupDate = prevCheckupDate
    def getprevCheckUpDate(self):
        return self.prevCheckupDate
    def setDoctorID(self, doctorID):
        self.doctorID = doctorID
    def getDoctorID(self):
        return self.doctorID
    def setPatientID(self, id):
        self.id = id
    def getPatientID(self):
        return self.id
    def setSymptoms(self, heathProblem):
        self.heathProblem = heathProblem
    def getSymptoms(self):
        return self.heathProblem
    def setMedication(self, medication):
        self.medication = medication
    def getMedication(self):
        return self.medication
    def setCharges(self, charges):
        self.charges = charges
    def getCharges(self):
        return self.charges
    def setReport(self, report):
        self.report = report
    def getReport(self):
        return self.report
    def patientRecord_details(self):
        print("Date of Previous Checkup : ", self.prevCheckupDate, "\nPatient Id : ", self.id, "\nDoctor Id : ", self.doctorID,"\nHealth problems : ", self.heathProblem, "\nMedicines : ", self.medication,"\nCharges : $", self.charges, "\nReport : ", self.report)

patient_Det = Patient(21, "Roy Kean", "Male", 52, "Manchester", 8989756489, "04-10-1970", 5, 12)
print("Patient Details")
patient_Det.patient_details()
doc = Doctor("Dr. Strange", 1111,"DO", "Nuerologist and general care physician", 9890204211, "10 AM - 9 PM", "Kansas city")
print("\nDoctor Details")
doc.doctorDetails()
patientRec = PatientMedicalRecord("09-10-2017", doc.getRegNumber(), patient_Det.getPatientID() , "cold , weakness and high sugar level" , "Glicomat GP1, Voveron", 1000, "Diabetese")
print("\nPatient Record")
patientRec.patientRecord_details()