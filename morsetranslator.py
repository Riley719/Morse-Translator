#morse translator

from bs4 import BeautifulSoup

morsecode = [   [".-", "a"], ["-...", "b"], ["-.-.", "c"], ["-..", "d"], [".", "e"], 
                ["..-.", "f"], ["--.", "g"], ["....", "h"], ["..", "i"], [".---", "j"], 
                ["-.-", "k"], [".-..", "l"], ["--", "m"], ["-.", "n"], ["---", "o"], 
                [".--.", "p"], ["--.-", "q"], [".-.", "r"], ["...", "s"], ["-", "t"], 
                ["..-", "u"], ["...-", "v"], [".--", "w"], ["-..-", "x"], ["-.--", "y"], 
                ["--..", "z"]]

html = open("morsetranslation.html", mode = "r", encoding = "utf-8")

hako1 = BeautifulSoup(html, "html.parser")
hako2 = hako1.find("textarea").text
morse = list(hako2)
morse0 = []
code = ""
translation = ""



for i in range(len(morse)):
    if morse[i] == "･":
        morse[i] = "."
    if morse[i] == "ｰ":
        morse[i] = "-"

for i in range(len(morse)):
    if morse[i] != " " and i != len(morse):
        code += morse[i]
    else:
        morse0.append(code)
        code = ""
morse0.append(code)

for i in range(len(morse0)):
    if morse0[i] == "":
        translation += " "
        i += 2
    else:
        for j in range(26):
            if morse0[i] == morsecode[j][0]:
                translation += morsecode[j][1]

hako1.find("div").clear()
hako1.find("div").append(translation)

print(hako1.find("div").text)