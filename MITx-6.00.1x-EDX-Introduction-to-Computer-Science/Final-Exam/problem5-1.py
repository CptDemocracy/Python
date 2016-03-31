"""
Final Exam Problem 5-1

Consider the following code and then answer the coding question and 
the following two questions after:

[ref.href] https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_6+2T2015+type@asset+block/code_exam5.py

Fill in the code for setGrade, getGrade, setPset, and getPset, using 
the courseInfo class functions. Paste your entire definition of the 
edx class in the following box.

class edx(object):
    
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def findCourse(self, courseName):
        """
        courseName: string

        returns: a course by the specified courseName arg
                 None if no such course was found        
        """
        for course in self.myCourses:
            if course.courseName == courseName:
                return course
        return None
        
    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        if grade < 0 or grade > 100:
            raise ValueError("grade out of bounds of 0 and 100")
        if type(course) != str:
            raise TypeError("course arg not of type str")
        
        targetCourse = self.findCourse(course)
        if targetCourse != None:
            targetCourse.setGrade(grade)

    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        targetCourse = self.findCourse(course)
        if targetCourse != None:
            return targetCourse.getGrade()
        return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        if type(pset) != str and type(pset) != int and type(pset) != float:
            raise TypeError("pset arg not a number and not a string")
        if score < 0 or score > 100:
            raise ValueError("grade out of bounds of 0 and 100")
        if type(course) != str:
            raise TypeError("course arg not of type str")

        targetCourse = self.findCourse(course)
        if targetCourse != None:
            targetCourse.setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        if type(pset) != str and type(pset) != int and type(pset) != float:
            raise TypeError("pset arg not a number and not a string")
        if type(course) != str:
            raise TypeError("course arg not of type str")
        
        targetCourse = self.findCourse(course)
        if targetCourse != None:
            return targetCourse.getPset(pset)
        return -1
