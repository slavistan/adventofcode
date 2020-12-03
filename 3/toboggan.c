/* gcc toboggan.c -o runme && runme */

#include <stdio.h>
#include <string.h>

int
main() {
	FILE *f;
	size_t n, m, i, j, lindex, numtrees, rightby, downby, prodnumtrees;
	char *p;
	char lindata[16384] = {0};
	const size_t right[] = { 1, 3, 5, 7, 1};
	const size_t down[] = { 1, 1, 1, 1, 2};

	f = fopen("./input", "r");

	/*
	 * Determine height and width
	 */
	fgets(lindata, sizeof(lindata), f);
	n = strlen(lindata) - 1;
	p = lindata + n;
	m=0;
	while (fgets(p, sizeof(lindata), f)) {
		p += n; // assuming constant width
		m += 1;
	}
	if (*(p + n) == '\n') {
		*(p + n) = '\0';
	}
	m+=1;

	/*
	 * Traverse "grid" and apply linear transform
	 */
	prodnumtrees = 1;
	for (int k = 0; k < sizeof(right) / sizeof(size_t); ++k) {
		rightby = right[k];
		downby = down[k];
		numtrees = i = j = 0;
		while (i < m) {
			lindex = n * i + j;
			if (lindata[lindex] == '#') {
				numtrees += 1;
			}
			i += downby;
			j = (j + rightby) % n;
		}

		prodnumtrees *= numtrees;
		printf("Slope (%lu, %lu): Numtrees = '%lu'\n", downby, rightby, numtrees);
	}
	printf("Product of numtrees = %lu\n", prodnumtrees);

	printf(
		" _____________________________________\n"
		"< Excellent day to have a rotten day. >\n"
		" -------------------------------------\n"
		"        \\   ^__^\n"
		"         \\  (oo)\\_______\n"
		"            (__)\\       )\\/\\\n"
		"                ||----w |\n"
		"                ||     ||\n");
}
