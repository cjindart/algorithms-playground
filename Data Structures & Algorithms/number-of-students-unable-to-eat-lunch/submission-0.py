class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # if no students, return 0
        if not students:
            return 0
        
        # to keep track of rejections
        counter = 0
        
        # else, loop through to give students sandwiches
        while students:
            # get student pref at start of list
            stud = students.pop(0)
            # if same as first sandwich, remove both
            if stud == sandwiches[0]:
                sandwiches.pop(0)
                counter = 0 
            else:
                # otherwise, move student to the end
                students.append(stud)
                # increase counter
                counter += 1
                # if counter longer than length of students, return
            if counter > len(students):
                break
        
        return len(students)
            