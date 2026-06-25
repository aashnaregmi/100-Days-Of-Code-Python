import random
celebrity_list = [
    {
        "name": "Taylor Swift",
        "location": "New York, USA",
        "work": "Singer, Songwriter",
        "followers": 274_000_000
    },
    {
        "name": "Selena Gomez",
        "location": "Los Angeles, California, USA",
        "work": "Singer, Actress, Businesswoman",
        "followers": 418_000_000
    },
    {
        "name": "Kim Kardashian",
        "location": "Los Angeles, California, USA",
        "work": "Media Personality, Businesswoman",
        "followers": 355_000_000
    },
    {
        "name": "Zendaya",
        "location": "Los Angeles, California, USA",
        "work": "Actress, Singer",
        "followers": 177_000_000
    },
    {
        "name": "Jennifer Aniston",
        "location": "Los Angeles, California, USA",
        "work": "Actress, Producer",
        "followers": 44_300_000
    },
    {
        "name": "Hailey Bieber",
        "location": "Los Angeles, California, USA",
        "work": "Model, Businesswoman",
        "followers": 55_500_000
    }
]


# for celebrity in celebrity_list:
#     print(celebrity["name"])
#     print(celebrity["location"])
#     print(celebrity["followers"])
#     print()
while True:
 a = random.randint(0, len(celebrity_list) - 1)
 while True:
    b = random.randint(0, len(celebrity_list) - 1)
    if a == b:
        b = random.randint(0, len(celebrity_list) - 1)
    # print(a, b)

    print(f"Compare A:{celebrity_list[a]["name"]},{celebrity_list[a]["work"],{celebrity_list[a]["work"]}}")
    print(f"Compare B:{celebrity_list[b]["name"]},{celebrity_list[b]["work"],{celebrity_list[b]["work"]}}")

    guess=input("Guess (A OR B):").lower()

    max_follower=max(
        (celebrity_list[a]["followers"]),
        (celebrity_list[b]["followers"])
    )

    if guess=="a" and celebrity_list[a]["followers"]==max_follower:
        print("You are correct")
    elif guess == "b" and celebrity_list[b]["followers"] == max_follower:
        print("You are correct")
    else:
        print("You are wrong")
        break
    a=b
 break

