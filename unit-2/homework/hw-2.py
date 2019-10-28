worker_type = input("Worker type: ")
hours_worked = int(input("Hours worked: "))

if worker_type == "contract":
    overtime = 120*hours_worked
    weekly_wages = (overtime) - (overtime*0.25)
elif hours_worked <= 40:
    weekly_wages = 50*hours_worked
elif hours_worked > 40:
    overtime = hours_worked - 40
    weekly_wages = (overtime*60) + (40*50)
elif hours_worked <=20:
    weekly_wages = 65*hours_worked
elif hours_worked > 20:
    overtime = hours_worked - 20
    weekly_wages = (overtime*70) + (20*65)

print(f"weekly_wages = {weekly_wages}")