#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> courses(numCourses);
        vector<int> visit(numCourses, 0);

        for(int i = 0; i < prerequisites.size(); i++){
            courses[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        for(int i = 0; i < numCourses; i++){
            if(!visit[i] && dfs(i, courses, visit)){
                return false;
            }
        }
        return true;
    }

    bool dfs(int crs, vector<vector<int>> &courses, vector<int> &visit){
        visit[crs] = 1;
        for (int v : courses[crs]){
            if(!visit[v]){
                visit[v] = 1;
                if(dfs(v, courses, visit)){
                    return true;
                }
            }
            else if(visit[v] == 1){
                return true;
            }
        }
        visit[crs] = 999;
        return false;
    }


};