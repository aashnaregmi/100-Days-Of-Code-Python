import random
celebrity_list = [
    {
        "name": "Kylie Jenner",
        "location": "Los Angeles, California, USA",
        "work": "Media Personality, Businesswoman",
        "followers": 392_000_000
    },
    {
        "name": "Cristiano Ronaldo",
        "location": "Riyadh, Saudi Arabia",
        "work": "Footballer",
        "followers": 670_000_000
    },
    {
        "name": "Lionel Messi",
        "location": "Miami, Florida, USA",
        "work": "Footballer",
        "followers": 506_000_000
    },
    {
        "name": "Dwayne Johnson",
        "location": "Los Angeles, California, USA",
        "work": "Actor, Former Wrestler",
        "followers": 393_000_000
    },
    {
        "name": "Ariana Grande",
        "location": "Los Angeles, California, USA",
        "work": "Singer, Actress",
        "followers": 374_000_000
    },
    {
        "name": "Beyoncé",
        "location": "Los Angeles, California, USA",
        "work": "Singer, Songwriter",
        "followers": 313_000_000
    },
    {
        "name": "Justin Bieber",
        "location": "Los Angeles, California, USA",
        "work": "Singer",
        "followers": 294_000_000
    },
    {
        "name": "Cardi B",
        "location": "New York City, New York, USA",
        "work": "Rapper, Singer",
        "followers": 163_000_000
    },
    {
        "name": "Virat Kohli",
        "location": "Mumbai, India",
        "work": "Cricketer",
        "followers": 274_000_000
    },
    {
        "name": "Neymar Jr",
        "location": "Santos, Brazil",
        "work": "Footballer",
        "followers": 232_000_000
    },
    {
        "name": "Shraddha Kapoor",
        "location": "Mumbai, India",
        "work": "Actress",
        "followers": 95_000_000
    },
    {
        "name": "Priyanka Chopra",
        "location": "Los Angeles, California, USA",
        "work": "Actress, Producer",
        "followers": 92_000_000
    },
    {
        "name": "Balen Shah",
        "location": "Kathmandu, Nepal",
        "work": "Mayor of Kathmandu, Rapper, Civil Engineer",
        "followers": 2_300_000
    },
    {
        "name": "Nike",
        "location": "Beaverton, Oregon, USA",
        "work": "Sportswear Brand",
        "followers": 292_000_000
    },
    {
        "name": "Victoria's Secret",
        "location": "Reynoldsburg, Ohio, USA",
        "work": "Fashion Brand",
        "followers": 77_000_000
    },
    {
        "name": "UEFA Champions League",
        "location": "Nyon, Switzerland",
        "work": "Football Competition",
        "followers": 120_000_000
    },
    {
        "name": "Priyanka Karki",
        "location": "Kathmandu, Nepal",
        "work": "Actress, Singer, Producer",
        "followers": 2_500_000
    },
    {
        "name": "MrBeast",
        "location": "Greenville, North Carolina, USA",
        "work": "YouTuber, Entrepreneur",
        "followers": 73_000_000
    },
    {
        "name": "Billie Eilish",
        "location": "Los Angeles, California, USA",
        "work": "Singer, Songwriter",
        "followers": 125_000_000
    },
    {
        "name": "Drake",
        "location": "Toronto, Ontario, Canada",
        "work": "Rapper, Singer",
        "followers": 142_000_000
    }
]


# for celebrity in celebrity_list:
#     print(celebrity["name"])
#     print(celebrity["location"])
#     print(celebrity["followers"])
#     print()


while True:
 score=0
 a = random.randint(0, len(celebrity_list) - 1)

 while True:
    temp=-1
    b = random.randint(0, len(celebrity_list) - 1)

    if a == b or b==temp:

        b = random.randint(0, len(celebrity_list) - 1)

    # print(a, b)

    print(" ")

    print(f"Compare A:{celebrity_list[a]["name"]},{celebrity_list[a]["work"],{celebrity_list[a]["work"]}}")
    print(" ")

    print(f"Compare B:{celebrity_list[b]["name"]},{celebrity_list[b]["work"],{celebrity_list[b]["work"]}}")
    print(" ")



    guess=input("Guess (A OR B):").lower()



    max_follower=max(

        (celebrity_list[a]["followers"]),

        (celebrity_list[b]["followers"])

    )



    if guess=="a" and celebrity_list[a]["followers"]==max_follower:

        print("You are correct")
        score+=1
        print(f"Score:{score}")

    elif guess == "b" and celebrity_list[b]["followers"] == max_follower:

        print("You are correct")
        score+=1
        print(f"Score:{score}")

    else:

        print("You are wrong")

        break
    temp=a
    a=b

 break

