import sqlite3
db_connect = sqlite3.connect('PawsomePetsDatebase.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()


#Populates the schema of the DB and inserts the tuples that were inserted in Part 3 (Can find them in the documentation)
query = """
CREATE TABLE Clinic(
    ClinicNo INT PRIMARY KEY CHECK (ClinicNo > 0),
    C_Name VARCHAR(255),
    Address VARCHAR(255),
    PhoneNo INT
);

CREATE TABLE StaffMember(
    StaffNo INT PRIMARY KEY CHECK (StaffNo > 0),
    S_Name VARCHAR(255),
    Address VARCHAR(255),
    PhoneNo INT,
    DOB VARCHAR(255),
    S_Position VARCHAR(255),
    Salary INT,
    ClinicNo INT NOT NULL CHECK (ClinicNo > 0),
    FOREIGN KEY (ClinicNo) REFERENCES Clinic(ClinicNo) ON DELETE CASCADE
);

CREATE TABLE Owner(
    OwnerNo INT PRIMARY KEY CHECK (OwnerNo > 0),
    O_Name VARCHAR(255),
    Address VARCHAR(255),
    PhoneNo INT
)
;

CREATE TABLE Pet(
    PetNo INT PRIMARY KEY CHECK (PetNo > 0),
    P_Name VARCHAR(255),
    DOB VARCHAR(255),
    Species VARCHAR(255),
    Breed VARCHAR(255),
    Color VARCHAR(255),
    OwnerNo INT NOT NULL CHECK (OwnerNo > 0),
    ClinicNo INT NOT NULL CHECK (ClinicNo > 0),
    FOREIGN KEY (OwnerNo) REFERENCES Owner(OwnerNo) ON DELETE CASCADE,
    FOREIGN KEY (ClinicNo) REFERENCES Clinic(ClinicNo) ON DELETE CASCADE
);

CREATE TABLE Examination(
    ExamNo INT PRIMARY KEY CHECK (ExamNo > 0),
    ChiefComplaint VARCHAR(255),
    Description VARCHAR(255),
    DateSeen VARCHAR(255),
    ActionTaken VARCHAR(255),
    StaffNo INT NOT NULL CHECK (StaffNo > 0),
    PetNo INT NOT NULL CHECK (PetNo > 0),
    FOREIGN KEY (StaffNo) REFERENCES StaffMember(StaffNo) ON DELETE SET NULL,
    FOREIGN KEY (PetNo) REFERENCES Pet(PetNo) ON DELETE CASCADE
);

INSERT INTO Clinic VALUES (1, 'Greensville Pet Clinic', '148 Legacy Dr, Greensville', 2059790010);
INSERT INTO Clinic VALUES (2, 'Johnsons Family Clinic', '1266 14th St, Palm City', 5625816405);
INSERT INTO Clinic VALUES (3, 'Pet Care Plus', '680 American Highway, San Jose', 9043821680);
INSERT INTO Clinic VALUES (4, 'Pet Care Plus', '2385 Lakeview Rd, Brisk Springs', 9064831160);
INSERT INTO Clinic VALUES (5, 'Fidos Finest', '112 Commons Parkway, West Brooks', 3480065275);

INSERT INTO StaffMember VALUES (1, 'John Doe', '12 Green Lane, San Jose', 8241506835, '1993-05-06', 'Veterinarian', 85000, 3);
INSERT INTO StaffMember VALUES (2, 'Molly Saunders', '64 Hampton Cr, Palm City', 6851276458, '1999-11-20', 'Front Desk', 40000, 2);
INSERT INTO StaffMember VALUES (3, 'Jake Longe', '110 Commons Parkway, West Brooks', 2036221555, '2003-10-03', 'Front Desk', 38000, 5);
INSERT INTO StaffMember VALUES (4, 'Victor Perez', '12 34th St, Greensville', 4056522525, '1980-01-23', 'Clinic Manager', 75000, 1);
INSERT INTO StaffMember VALUES (5, 'Loise Smith', '324 165th St, Brisk Springs', 6854246116, '1986-09-09', 'Clinic Manager', 74000, 4);

INSERT INTO Owner VALUES (1, 'Steve Jobs', '435 Lakeside Dr, Albany', 1563856696);
INSERT INTO Owner VALUES (2, 'Bill Gates', '81 Komodo Ln, Atlanta', 6852251203);
INSERT INTO Owner VALUES (3, 'Mark Robinson', '16276 45th St, Miami', 3056821027);
INSERT INTO Owner VALUES (4, 'Leroy Jacobs', '103 Jefferson St, Austin', 6830255203);
INSERT INTO Owner VALUES (5, 'Lisa Grober', '12 Stevenson Ln, Parktown', 4015822652);

INSERT INTO Pet VALUES (1, 'Fido', '2010-05-26', 'Dog', 'Lab', 'Black', 1, 2);
INSERT INTO Pet VALUES (2, 'Dolly', '2021-12-01', 'Cat', 'Siamese', 'White', 1, 4);
INSERT INTO Pet VALUES (3, 'Rocky', '2002-02-15', 'Turtle', 'Snapping', 'Brown', 4, 3);
INSERT INTO Pet VALUES (4, 'Pebbles', '2006-06-06', 'Hamster', 'Syrian', 'Tan', 2, 3);
INSERT INTO Pet VALUES (5, 'Keiko', '2019-04-23', 'Dog', 'German Shepherd', 'Black/Brown', 3, 5);

INSERT INTO Examination VALUES (1, 'Red rash on paws', 'There are multiple small red dots on bottom of paws', '2022-06-16', 'Medication Prescribed', 1, 1);
INSERT INTO Examination VALUES (3, 'Animal barely moves', 'The animal seems to not move very often the owner is concerned', '2022-11-13', 'No action taken', 1, 3);
INSERT INTO Examination VALUES (4, 'Cuts on body', 'Animal appears to have a few small cuts on body', '2022-11-13', 'Prescribed cream and placed cone on neck', 1, 1);
INSERT INTO Examination VALUES (5, 'Red spot on nose', 'A red rash is on the animals nose', '2022-12-03', 'Medication Prescribed', 1, 5);
INSERT INTO Examination VALUES (2, 'Pet is limping', 'The pet is limping on the front right leg when it walks', '2022-07-02', 'Put cast on leg', 1, 2);
"""
queries = query.split(";", -1)
i = 1

for q in queries:
    cursor.execute(q)

# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()