#!/usr/bin/env zsh

n=0
cat input | while read line; do
	num1=$(echo "$line" | cut -d- -f1)
	num2=$(echo "$line" | cut -d- -f2 | cut -d' ' -f1 )
	char=$(echo "$line" | cut -d' ' -f2 | tr -d :)
	pw=$(echo "$line" | cut -d: -f 2 | tr -d ' ')

	numpwchar=$(echo -n "$pw" | tr -cd "$char" | wc -c)

	if [ "$num1" -le "$numpwchar" ] &&
		[ "$numpwchar"  -le "$num2" ]; then
		n=$(($n + 1))
	fi
done
echo "Policy 1: $n correct pws"

n=0
cat input | while read line; do
	num1=$(echo "$line" | cut -d- -f1)
	num2=$(echo "$line" | cut -d- -f2 | cut -d' ' -f1 )
	char=$(echo "$line" | cut -d' ' -f2 | tr -d :)
	pw=$(echo "$line" | cut -d: -f 2 | tr -d ' ')

	count="$(echo "$(printf "$pw" | head -c $num1 | tail -c 1)$(printf "$pw" | head -c $num2 | tail -c 1)" | tr -cd $char | wc -c)"
	if [ "$count" -eq 1 ]; then
		n=$(($n + 1))
	fi
done
echo "Policy 2: $n correct pws"

cat <<EOF
 ________________________________________
/ You've been leading a dog's life. Stay \\
\\ off the furniture.                     /
 ----------------------------------------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||

EOF
