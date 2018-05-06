// bouncy. 112
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool Inc(int x)
{
	std::ostringstream ss;
	ss << x;
	std::string s = ss.str();
	int l = s.length();
	bool sofar = true;
	for (int x = 0; x < l - 1 && sofar; x ++)
	{
		if (s[x] > s[x+1])
			sofar = false;
	}
	return sofar;
}

bool Dec(int x)
{
	std::ostringstream ss;
	ss << x;
	std::string s = ss.str();
	int l = s.length();
	bool sofar = true;
	for (int x = 0; x < l - 1 && sofar; x ++)
	{
		if (s[x] < s[x+1])
			sofar = false;
	}
	return sofar;
}

int main()
{
	int curr_bouncy_no = 0;
	bool sofar = false;
	int total = 99;
	while (!sofar)
	{
		total += 1;
		if (!Inc(total) && !Dec(total))
		{
			curr_bouncy_no += 1;
		}
		if (100*curr_bouncy_no == 99*total)
		{
			sofar = true;
		}
	}
	std::cout << total << std::endl;
}