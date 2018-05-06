// euler 145.
// reversible no.s
#include <iostream>
#include <string>
#include <sstream>

bool isReversible(int n)
{
	// first find reverse.
	std::ostringstream ss;
	ss << n;
	std::string strN = ss.str();
	std::string strRev = "";
	int len = strN.length();
	for (int i = 0; i < len; i ++)
	{
		strRev += strN[len - 1- i];
	}
	
}

int main()
{
	int Rcount = 0;
	for (int i = 1; i < 1000000000; i ++)
	{
		if isReversible(i)
		{
			Rcount += 1;
		}
	}
	std::cout << Rcount << std::endl;
}