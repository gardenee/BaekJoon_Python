score = {"A+": 4.5, "A0": 4, "B+": 3.5, "B0": 3, "C+": 2.5, "C0": 2, "D+": 1.5, "D0": 1, "F": 0, "P": 0}
tot_score = 0.0
tot_credit = 0

for _ in range(20):
    subject, credit, grade = input().split()
    tot_score += score[grade] * float(credit)
    if grade != "P": tot_credit += float(credit)

print(tot_score/tot_credit)
