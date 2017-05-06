import sys
l = []
for i in range(23):
	l.append('')
l[0] = "     <layout>\n"
l[1] = "      <configItem>\n"
l[2] = "        <name>jdt-lat</name>\n"
l[3] = "        <shortDescription>jdt-lat</shortDescription>\n"
l[4] = "        <description>Judeo-Tat (Latin)</description>\n"
l[5] = "        <languageList><iso639Id>jdt</iso639Id><iso639Id>jdt-lat</iso639Id></languageList>\n"
l[6] = "      </configItem>\n"
l[6] = "    </layout>\n"
l[7] = "     <layout>\n"
l[8] = "      <configItem>\n"
l[9] = "        <name>jdt-cyr</name>\n"
l[10] = "        <shortDescription>jdt-cyr</shortDescription>\n"
l[11] = "        <description>Judeo-Tat (Cyrillic)</description>\n"
l[12] = "        <languageList><iso639Id>jdt</iso639Id><iso639Id>jdt-cyr</iso639Id></languageList>\n"
l[13] = "      </configItem>\n"
l[14] = "    </layout>\n"


with open('evdex.xml', 'r+') as f:
	read_data = f.read()
	data = read_data.split('\n')
	for line in range(len(data)):
		#print line
		if '</layoutList>'in data[line]:

			line = sys.getsizeof(data[:line])
			f.seek(line)
			for i in l:
				f.write(i)

