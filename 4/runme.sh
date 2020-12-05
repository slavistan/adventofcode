#!/usr/bin/env zsh

printf "First: "
cat input |
	tr '\n' '' |
	sed 's//\n/g' |
	tr '' ' ' |
	sed 's/:[^ ]*//g' |
	sed 's/cid \?//g' |
	awk -F ' ' '{ print NF }' |
	grep -F '7' |
	wc -l

printf "Second: "
cat input |
	tr '\n' '' |
	sed 's//\n/g' |
	tr '' ' ' |
	sed 's/ $//g' |
	sed 's/cid:[^ ]* \?//g' |
	sed 's/ $//g' |
	while read line; do
		if [ ! "$(echo -n "$line" | wc -w)" -eq 7 ]; then
			continue
		fi
		valid=1
		echo "$line" | tr ' ' '\n' | while read field; do
			key="$(echo "$field" | cut -d: -f1)"
			val="$(echo "$field" | cut -d: -f2)"
			case "$key" in
			byr)
				if ! echo "$val" | grep -q '^[0-9]\{4\}$' ||
				[ ! "$val" -ge 1920 ] || [ ! "$val" -le 2002 ]; then
					valid=0; break
				fi
				;;
			iyr)
				if ! echo "$val" | grep -q '^[0-9]\{4\}$' ||
				[ ! "$val" -ge 2010 ] || [ ! "$val" -le 2020 ]; then
					valid=0; break
				fi
				;;
			eyr)
				if ! echo "$val" | grep -q '^[0-9]\{4\}$' ||
				[ ! "$val" -ge 2020 ] || [ ! "$val" -le 2030 ]; then
					valid=0; break
				fi
				;;
			hgt)
				if echo "$val" | grep -q '^[0-9]\{2\}in$'; then
					num="$(echo "$val" | head -c 2)"
					if [ ! "$num" -ge 59 ] || [ ! "$num" -le 76 ]; then
						valid=0; break
					fi
				elif echo "$val" | grep -q '^[0-9]\{3\}cm$'; then
					num="$(echo "$val" | head -c 3)"
					if [ ! "$num" -ge 150 ] || [ ! "$num" -le 193 ]; then
						valid=0; break
					fi
				else
					valid=0; break
				fi
				;;
			hcl)
				if ! echo "$val" | grep -q '^#[0-9a-fA-F]\{6\}$'; then
					valid=0; break
				fi
				;;
			ecl)
				if ! echo "$val" | grep -q '^amb\|blu\|brn\|gry\|grn\|hzl\|oth$'; then
					valid=0; break
				fi
				;;
			pid)
				if ! echo "$val" | grep -q '^[0-9]\{9\}$'; then
					valid=0; break
				fi
				;;
			esac
		done
		if [ $valid -eq 1 ]; then
			printf "VALID: '$line'\n"
		fi
	done | wc -l


cat <<EOF
 _________________________________________
/ You are a very redundant person, that's \\
\\ what kind of person you are.            /
 -----------------------------------------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
EOF
