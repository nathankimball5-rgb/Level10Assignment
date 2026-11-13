import pandas as pd

info = pd.read_csv("cfb.csv")
correct_input = False

while correct_input == False:
    try:
        user_szn = int(input("Enter a season to analyze: "))
        correct_input = True
    except ValueError:
        print("Please Enter a year using only digits.")

win_categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}

season_data = info.loc[info["Season"] == user_szn]

if season_data.empty:
    print("Season not found.")

else:

    for i, team  in season_data.iterrows():
        if team["Win"] >= 10:
            win_categories["10 or more wins"].append(team["Team"])
        elif team["Win"] >= 8:
            win_categories["8-9 wins"].append(team["Team"])
        elif team["Win"] >= 6:
            win_categories["6-7 wins"].append(team["Team"])
        else:
            win_categories["Fewer than 6 wins"].append(team["Team"])

    print(f"College Football Results for {user_szn}")

    for category, teams in win_categories.items():
        print()
        print(category + ": ")
        for i in teams:
            names_wanted = i.rsplit(" (",1)
            print(names_wanted[0])