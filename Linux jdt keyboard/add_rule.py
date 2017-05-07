#David Yelsey
#Adds keyboard in evdev.xml right before </layoutList>

l = []
for i in range(16):
	l.append('')
l[0] = "     <layout>\n"
l[1] = "      <configItem>\n"
l[2] = "        <name>jdt-cyr</name>\n"
l[3] = "        <shortDescription>jdt-cyr</shortDescription>\n"
l[4] = "        <description>Judeo-Tat (Cyrillic)</description>\n"
l[5] = "        <languageList><iso639Id>jdt</iso639Id><iso639Id>jdt-cyr</iso639Id></languageList>\n"
l[6] = "      </configItem>\n"
l[7] = "    </layout>\n"
l[8] = "     <layout>\n"
l[9] = "      <configItem>\n"
l[10] = "        <name>jdt-cyr-russian</name>\n"
l[11] = "        <shortDescription>jdt-cyr-russian</shortDescription>\n"
l[12] = "        <description>Judeo-Tat (Russian)</description>\n"
l[13] = "        <languageList><iso639Id>jdt</iso639Id><iso639Id>jdt-cyr-russian</iso639Id></languageList>\n"
l[14] = "      </configItem>\n"
l[15] = "    </layout>\n"

to_add = ''
for line in l:
	to_add += line

buf = []
with open("evdev.xml", "r") as in_file:
    buf = in_file.readlines()

with open("evdev.xml", "w") as out_file:
    for line in buf:
        if "</layoutList>" in line:
            line = to_add + line
        out_file.write(line)
