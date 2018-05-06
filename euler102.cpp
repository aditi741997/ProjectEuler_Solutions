// trying 102.
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int sameSide(int m, int c,int y,int x1,int y1)
{
	// line is mx + c - y = 0
	int p1 = m*x1 + c - y*y1;
	if ((p1 >= 0 && c >= 0) || (p1 < 0 && c < 0))
	{
		return true;
	}
	else
		return false;
}

int main()
{
	// read file
	// line wise karte jao.
	int tcount = 0;
	std::string line = "";
	std::ifstream efile ("p102_triangles.txt");
	if (efile.is_open())
	{
		while (getline(efile,line))
		{
			// line is ith line. split by ','
			for (int i = 0; i < line.length() ; i ++)
			{
				if (line[i] == ',')
				{
					line[i] = ' ';
				}
			}
			vector<int> int_array;
			stringstream ss(line);
			int temp;
			while (ss >> temp)
			{
				int_array.push_back(temp);
			}
			// check if origin inside triangle.
			int a1 = int_array[0];
			int b1 = int_array[1];
			int a2 = int_array[2];
			int b2 = int_array[3];
			int a3 = int_array[4];
			int b3 = int_array[5];
			if (sameSide(b2 - b1,a2*b1 - a1*b2,a2 - a1,a3,b3) && sameSide(b3 - b2,a3*b2 - a2*b3,a3 - a2,a1,b1) && sameSide(b1 - b3,a1*b3 - a3*b1,a1 - a3,a2,b2))
			{
				tcount += 1;
			}
		}
		efile.close();
	}
	std::cout << tcount << std::endl;
}