#include <vector>
#include <algorithm>

using namespace std;

double routeDistance(const vector<int>& path, const vector<vector<int>>& dist) {
    double total = 0;
    for (int i = 0; i < path.size() - 1; i++) {
        total += dist[path[i]][path[i + 1]];
    }
    return total;
}

vector<int> twoOpt(vector<int> path, const vector<vector<int>>& dist) {
    bool improved = true;

    while (improved) {
        improved = false;
        for (int i = 1; i < path.size() - 2; i++) {
            for (int j = i + 1; j < path.size() - 1; j++) {
                // Вычисляем расстояния рёбер до обмена
                int a = path[i - 1];
                int b = path[i];
                int c = path[j];
                int d = path[j + 1];

                double before = dist[a][b] + dist[c][d];
                double after = dist[a][c] + dist[b][d];

                // Если улучшение есть, то меняем порядок в пути
                if (after < before) {
                    reverse(path.begin() + i, path.begin() + j + 1);
                    improved = true;
                }
            }
        }
    }
    return path;
}

