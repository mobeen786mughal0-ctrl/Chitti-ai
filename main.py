from google import genai

print("🤖 Chitti: Oye hoye! Main aa gaya 🔥")
print("Kuch bhi pooch le yaar. Thak jaaye to 'bye' likh dena\n")

API_KEY = "AQ.Ab8RN6K0Z_EOFmwVJJCgXMldpngd3HaTlA1-_o_0lq5TFpG0oQ"

client = genai.Client(api_key=API_KEY)

while True:
    user = input("Tu: ")
    if user.lower() == "bye":
        print("🤖 Chitti: Chal bhai Allah Hafiz! Phir milte hain 😎")
        break
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user
        )
        print("🤖 Chitti:", response.text, "\n")
    except Exception as e:
        print("🤖 Chitti: Uff error aa gaya:", e, "\n")
