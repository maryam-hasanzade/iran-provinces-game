import turtle
import pandas


screen = turtle.Screen()
screen.title("Iran Provinces Game")

image = "Iran.gif"
screen.addshape(image)
turtle.shape(image)


def normalize_text(text):
    return (
        text.strip()
        .replace("ي", "ی")
        .replace("ى", "ی")
        .replace("ك", "ک")
        .replace("‌", " ")
        .replace("  ", " ")
    )


data = pandas.read_csv("province.csv")
data.province = data.province.str.strip()

all_provinces = data.province.tolist()
guess_province = []

while len(guess_province) < len(all_provinces):

    answer = screen.textinput(
        title=f"{len(guess_province)}/{len(all_provinces)} Provinces Correct",
        prompt="What is another province's name?"
    )

    if answer is None:
        break

    answer = normalize_text(answer)

    if answer == "Exit":
        missing_province = []

        for province in all_provinces:
            if province not in guess_province:
                missing_province.append(province)

        pandas.DataFrame(missing_province).to_csv(
            "provinces_to_learn.csv",
            index=False
        )
        break

    if answer == "چهارمحال بختیاری":
        answer = "چهارمحال و بختیاری"

    if answer in all_provinces:

        guess_province.append(answer)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        province_data = data[data.province == answer]

        t.goto(
            province_data.x.item(),
            province_data.y.item()
        )

        t.write(answer)