crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

print("CryptoBuddy: Hey there! I'm CryptoBuddy 🧠💸")
print("CryptoBuddy: Ask me things like 'Which crypto is trending up?' or 'What's the most sustainable coin?'")
print("CryptoBuddy: Type 'exit' to quit.")

while True:
    user_query = input("You: ").lower()

    if "exit" in user_query:
        print("CryptoBuddy: Bye! Don’t forget to do your own research 🧠📉📈")
        break
    elif "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
    elif "trending" in user_query or "up" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: These coins are showing strong growth: {', '.join(trending_coins)} 🚀")
    else:
        print("CryptoBuddy: Sorry, I didn’t understand that. Try asking about trends or sustainability.")
