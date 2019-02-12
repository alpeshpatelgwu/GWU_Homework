START TRANSACTION;

-- This procedure accepts course code, section, 
-- student ID, and effective date as parameters

USE gwsis
DELIMITER $$

SELECT * FROM classparticipant
SELECT * FROM student

CREATE PROCEDURE `terminate_student_enrollment`(
IN StudentID_in varchar(45), IN CourseCode_in varchar(45), IN Section_in varchar(45), IN EndDate_in date)
BEGIN

DECLARE StudentID_rm int;
DECLARE CourseCode_rm int;
DECLARE Section_rm int;
DECLARE StartDate_rm date;

SET StudentID_rm = (SELECT ID_Student FROM student WHERE StudentID = StudentID_in);
SET CourseCode_rm = (SELECT CourseCode FROM course WHERE CourseCode = CourseCode_in);
SET Section_rm = (SELECT Section FROM class WHERE Section = Section_in);

DELETE FROM classparticipant cp
INNER JOIN class c ON cp.ID_Class = c.ID_Class
INNER JOIN course co ON c.ID_Course = co.ID_Course
WHERE co.ID_Course = CourseCode_rm AND cp.ID_StudentID = StudentID_rm;
END$$
use gwsis

