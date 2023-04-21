import random

# Define a list of ASCII arts
ascii_arts = [
    r"""
     _______
    /       \
   /         \
  /           \
  \           /
   \         /
    \_______/
    """,
    r"""
    ___________
    |         |
    |  RIP    |
    |         |
    |_________|
    """,
    r"""
     _   _
    / \ / \
   ( o | o )
    \   -   /
     (_\_/_)
    """
]

# Define a list of jokes
jokes = [
    "Why was the math book sad? Because it had too many problems.",
    "What do you get when you cross a snowman and a shark? Frostbite.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What did the grape say when it got stepped on all day? Nothing, it just let out a little wine.",
    "Why did the cookie go to the doctor? Because it felt crummy."
]

# Print a random joke and a random ASCII art
print(random.choice(jokes))
print(random.choice(ascii_arts))
