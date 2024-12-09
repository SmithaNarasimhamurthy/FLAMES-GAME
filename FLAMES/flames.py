# FLAMES Game Implementation
def flames_game():
    print("Welcome to FLAMES created using Python ❤️")
    print("Check the relationship status between you and your crush right now! 😍")

    while True:
        user = input("Type 'play' to play FLAMES, 'end' to exit: ").lower()

        if user == "end":
            print("Thanks for playing FLAMES! Goodbye! 👋")
            break

        if user == "play":
            boy = input("What's your name? ").strip().lower()
            girl = input("What's your crush's name? ").strip().lower()

            # Remove common characters between boy and girl names
            for char in boy[:]:  # Use a copy of the string for iteration
                if char in girl:
                    boy = boy.replace(char, "", 1)
                    girl = girl.replace(char, "", 1)

            # Calculate the total remaining characters
            total_count = len(boy) + len(girl)

            # FLAMES logic
            flames = ["Friends", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
            while len(flames) > 1:
                split_index = (total_count % len(flames)) - 1
                if split_index >= 0:
                    flames = flames[split_index + 1:] + flames[:split_index]
                else:
                    flames.pop()

            # Display the FLAMES result with additional messages
            relationship_status = flames[0]
            print("\n🎉 The moment you've been waiting for... 🎉")
            print(f"The relationship status between you and your crush is: {relationship_status}")

            # Add personalized messages based on the result
            if relationship_status == "Friends":
                print("💖 Friendship is the foundation of every great relationship!")
            elif relationship_status == "Love":
                print("❤️ Love is in the air! It's time to confess your feelings!")
            elif relationship_status == "Affection":
                print("💞 There's a warm and affectionate bond between you two.")
            elif relationship_status == "Marriage":
                print("💍 Looks like wedding bells might be in your future!")
            elif relationship_status == "Enemies":
                print("😅 Opposites attract... or maybe not! Better luck next time.")
            elif relationship_status == "Siblings":
                print("👫 You're like siblings! A bond that's pure and strong.")

            print("\nWant to try with another name? Type 'play' again!")
        else:
            print("Invalid input. Please type 'play' or 'end'.")

# Run the FLAMES game
if __name__ == "__main__":
    flames_game()
