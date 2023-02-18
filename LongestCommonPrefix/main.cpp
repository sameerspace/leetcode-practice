#include
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solution
{

public:
    string longestCommonPrefix(vector<string> &strs)
    {

        vector<vector<char>> map;
        for (int i = 0; i < strs.size(); i++)
        {
            for (int j = 0; j < strs[i].size(); j++)
            {
                map[i].push_back(strs[i][j]);
            }
        }

        cout << map << endl;
    }
};

int main()
{
}
