# HEALTH CARE SYSTEM


print("💻 Welcome to QuickHealth Pro Max – Terminal Edition\n")

# User inputs
name = input("👤 Enter your name: ")
gender = input("🚻 Enter your gender (male/female/other): ")
age = int(input("🎂 Enter your age: "))
city = input("📍 Enter your city (e.g., New York, Phoenix): ").lower()

print("\n💢 Select your main symptom from the list below:")
print("Options: fever, cough, fatigue, headache, chest pain, breathlessness")
symptom = input("🩺 Main symptom: ").lower()

temp = float(input("🌡️ Enter your body temperature (°F): "))
days_unwell = int(input("⏱️ How many days have you felt unwell? "))
smoke = input("🚬 Do you smoke? (yes/no): ").lower()
sleep = int(input("🛌 Hours of sleep last night: "))

print("\n🧠 Current mood options: calm, anxious, sad, irritable")
mood = input("🧘 Your current mood: ").lower()

pre_existing = input("❗ Do you have any pre-existing conditions (yes/no)? ").lower()

print("\n🔄 Processing your inputs...\n")

# Basic diagnostic output
print(f"✅ Health Summary for {name}:")

if temp > 103 or days_unwell > 5:
    risk = "High risk. Consider seeing a doctor immediately."
elif temp > 99.5:
    risk = "Medium risk. Monitor your symptoms and rest."
else:
    risk = "Low risk. You seem fine. Rest, hydrate, and check again in a day or two."

print(f"🟢 {risk}")

print("\n📌 Personalized Recommendations:")
if city == "delhi":
    print(" - If you're in delhi, the nearest urgent care is open till 10 PM.")

print("\n💬 Mental Health Tip:")
print("Keep it up! Share your positivity with others.")

print(f"\n🙏 Thank you for using QuickHealth Pro Max, {name}!")
print("Stay safe and take care. 💙")