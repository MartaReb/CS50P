from emoji import emojize

user_emoji = input("Input: ")
outcome = emojize(user_emoji, language='alias')
print(f"Output: {outcome}")