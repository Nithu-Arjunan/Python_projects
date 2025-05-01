# Project to know your personality

import time

# Display heading

print("🧠 Know your Personality")
print("✨ Lets discover who you really are with some fun magic")
print(64 * '-')

# Code to enter user details

print("📝 Enter Your Details")

name = input("👤 Your Name").strip()
age = int(input("🎂 Your Age"))
city = input("🏙️ City You Live In").strip()
food = input("🍕 Your Favorite Food").strip()
color = input("🎨 Your Favorite Colo").strip()
animal = input("🐾 Your Spirit Animal").strip()
hobby = input("🎮 One Thing You LOVE Doing")

age_in_months = age *12

time.sleep(3)

print("🔍 Scanning colors, foods, and animal energies...")
print("💫 Calculating your personality type using complex non-scientific logic...")
print(f"Hey {name.title()} , here's your fun personality report")

time.sleep(5)

print(f"🌆 You're from {city.title()}, a place of dreams!")
print(f"🍿 You love {food} and enjoy doing {hobby}.")
print(f"🎨 You vibe with the color {color} and your spirit animal is the {animal}.")
print(f"📅 You've lived approximately {age_in_months} months already.")

# Title calculator
if age < 18:
    title = "Young Explorer"
elif age <= 30:
    title = "Adventurer"
else:
    title = "Wise Owl"

print(f"🧩 You belong to the {title} tribe.")

# Personality code calculator

age_part = str(age)[-1]
Personality_code = name[:2].upper() + age_part + animal[0] + color[0]

print(f"🔐 Your Secret Personality Code is: 💡 {Personality_code}")

print("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")
print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")



