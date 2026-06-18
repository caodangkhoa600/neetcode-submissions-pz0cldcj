class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
    {
        return false;
    }

    map<char, int> c;
    string r = "";
    for (int i = 0; i < s.length(); i++)
    {
        if (c.find(s[i]) == c.end())
        {
            c.insert({s[i], 1});
            r = r + s[i];
        }
        else
        {
            c[s[i]]++;
        }
    }

    for (int i = 0; i < t.length(); i++)
    {
        if (c.find(t[i]) == c.end())
        {
            return false;
        }
        else
        {
            c[t[i]]--;

            if (c[t[i]] < 0)
            {
                return false;
            }

            if (c[t[i]] == 0)
            {
                c.erase(t[i]);
            }
        }
    }

    return c.empty();

    }
};
