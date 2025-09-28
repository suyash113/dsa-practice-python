# class Solution:
#     def printNumber(self):
#         # t = int(input("Enter a num: "))
#         return int(input("Enter a num: "))

# sol = Solution()
# print(sol.printNumber())

# class Solution:
#     def studentGrade(self, marks):
#         Grade = ""
#         if marks >= 90:
#             Grade = "A"
#         elif marks >= 70:
#             Grade = "B"
#         elif marks >= 50:
#             Grade = "C"
#         elif marks >= 35:
#             Grade = "D"
#         else:
#             Grade = "Fail"
#         return Grade
# print(Solution().studentGrade(95)) 

class Solution:
    def whichWeekDay(self, day):
        match day:

            case 1:
                
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:  # Default case
                print("Invalid")
Solution().whichWeekDay(2)