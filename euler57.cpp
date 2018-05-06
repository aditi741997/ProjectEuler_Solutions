// euler57
#include <iostream>
#include <string>
#include <sstream>

PROBLEM OF OVERFLOW!!!


int main()
{
	int ni = 3;
	int di = 2;
	int count = 0;
	int y = 0;   // for new values of n,d
	int ln = 1;   // length of numr
	int ld = 1;   // length of denr
	for (int x = 1; x < 1000; x++)
	{
		// xth iteration mein x+1th expansion
		y = ni + 2*di;
		di = ni + di;
		ni = y;
		std::cout << ni << "  " << di << std::endl;
		std::ostringstream ss;
		std::ostringstream ss2;
		ss << ni;
		std::string S = ss.str();
		ln = S.length();
		ss2 << di;
		S = ss2.str();
		ld = S.length();
		if (ln > ld)
		{
			count += 1;
		}
	}
	std::cout << count << std::endl;

}