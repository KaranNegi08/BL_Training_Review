# Task: Student Eligibility Filter using Sets
# Problem Statement

# You are given two sets:
# Students who submitted assignments
# Students who attended classes

# You need to determine:

# Who is eligible (both submitted + attended)
# Who is not eligible
# Who only did one of the activities
# Input
# submitted = {"Geeta", "Rahul", "Amit", "Sneha"}
# attended = {"Amit", "Sneha", "Kiran", "Geeta"}
# Requirements
# Find Eligible Students

# Students who are in both
# Find Not Eligible Students

# Students who are:
# Only submitted OR
# Only attended

submitted = {"Geeta", "Rahul", "Amit", "Sneha","karan"}
attended = {"Amit", "Sneha", "Kiran", "Geeta"}

eligible_students= submitted & attended
print(f" Eligible Students are: {eligible_students}")



not_eligible = submitted - eligible_students
print(f"Not eligible Students: {not_eligible}")
