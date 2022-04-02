# SQL_practice

CREATE database python_db;

CREATE TABLE `python_db`.`Hospital` ( `Hospital_Id` INT UNSIGNED NOT NULL , `Hospital_Name` TEXT NOT NULL , `Bed_Count` INT ,
PRIMARY KEY (`Hospital_Id`))

INSERT INTO `hospital` (`Hospital_Id`, `Hospital_Name`, `Bed Count`) VALUES
('1', 'Toronto General Hospital', '471'),
('2', 'St. Joseph's Health Centre', '376'),
('3', 'Mississauga Hospital', '751'),
('4', 'Credit Valley Hospital', '382')

CREATE TABLE `python_db`.`Doctor`
( `Doctor_Id` INT UNSIGNED NOT NULL ,
`Doctor_Name` TEXT NOT NULL ,
`Hospital_Id` INT NOT NULL ,
`Joining_Date` DATE NOT NULL ,
`Speciality` TEXT NULL ,
`Salary` INT NULL ,
`Experience` INT NULL ,
PRIMARY KEY (`Doctor_Id`))

INSERT INTO `doctor` (`Doctor_Id`, `Doctor_Name`, `Hospital_Id`, `Joining_Date`, `Speciality`, `Salary`, `Experience`) VALUES
('101', 'Duemler', '1', '2005-2-10', 'Pediatric', '140000', NULL),
('102', 'McBroom', '1', '2018-07-23', 'Oncologist', '120000', NULL),
('103', 'El-Ashry', '2', '2016-05-19', 'Surgeon', '125000', NULL),
('104', 'Chan', '2', '2017-12-28', 'Pediatric ', '128000', NULL),
('105', 'Platonov', '3', '2004-06-04', 'Psychiatrist', '142000', NULL),
('106', 'Izukaw', '3', '2012-09-11', 'Dermatologist', '130000', NULL),
('107', 'Jhas', '4', '2014-08-21', 'Obstetrician/Gynecologist', '132000', NULL),
('108', 'Marmor', '4', '2011-10-17', 'Radiologist', '130000', NULL)

function 1
List all doctors by specialty. First, list the name of the specialty. Then list all doctors associated with the specialty.
Their names should be displayed as "Dr. Lastname". Both the specialties and doctors should be listed in alphabetical order.

function 2
Display a numbered list of all the hospitals and allow the user to choose one. Ensure they choose a valid number, otherwise continually prompt them for a correct number.
Then, display all doctors associated with that hospital. Their names should be displayed as "Dr. Lastname -- Specialty"

function 3
Ask the user to specify a number of years. Then, display all doctors who have been with the hospital at least that long.
Use the difference between the joining date and today's date to calculate that number.
Their names should be displayed as "Dr. Lastname (Hospital Name)"
