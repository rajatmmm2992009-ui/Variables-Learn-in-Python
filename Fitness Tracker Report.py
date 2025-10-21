# Fitness Tracker Report

user_name = "Rajat"
user_age = 16
user_height = 5.6
user_weight = 62
daily_steps = 10000
calories_burned = 450
water_intake = 2.5
sleep_hours = 7.5

bmi = user_weight / ((user_height / 100) ** 2)
target_steps = 10000
steps_remaining = target_steps - daily_steps
calorie_deficit = 500
target_calories_burned = calories_burned + calorie_deficit

weekly_steps = [8500, 8000, 9500, 9000, 7500, 7000, 10000]
weekly_calories = [450, 500, 550, 400, 350, 300, 250]

average_steps = sum(weekly_steps) / len(weekly_steps)
average_calories = sum(weekly_calories) / len(weekly_calories)

print("Fitness Tracker Report")
print("=" * 40)
print(f"Name: {user_name}")
print(f"Age: {user_age} years")
print(f"Height: {user_height} feet")
print(f"Weight: {user_weight} kg")
print(f"BMI: {bmi:.2f}")
print(f"Today's Steps: {daily_steps}")
print(f"Steps Remaining: {steps_remaining}")
print(f"Calories Burned: {calories_burned}")
print(f"Water Intake: {water_intake} L")
print(f"Sleep: {sleep_hours} hours")
print(f"Weekly Average Steps: {average_steps:.0f}")
print(f"Weekly Average Calories: {average_calories:.0f}")


