#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX_N = 1000;
const int MAX_M = 1000;
const int MAX_K = 10;

char graph[MAX_N][MAX_M + 1];
int visited[MAX_N][MAX_M][MAX_K + 1][2]; // [y][x][벽부순횟수][낮/밤]
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

struct State {
    int y, x, day, cnt;
};

int main() {
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    for (int i = 0; i < n; ++i) {
        scanf("%s", graph[i]);
    }

    // visited 초기화
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            for (int c = 0; c <= k; ++c)
                for (int d = 0; d < 2; ++d)
                    visited[i][j][c][d] = -1;

    queue<State> q;
    visited[0][0][0][0] = 1;
    q.push({0, 0, 0, 0}); // y, x, day, cnt

    while (!q.empty()) {
        State cur = q.front(); q.pop();
        int y = cur.y, x = cur.x, day = cur.day, cnt = cur.cnt;
        for (int i = 0; i < 4; ++i) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            int nday = 1 - day;

            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;

            if (graph[ny][nx] == '0') {
                if (visited[ny][nx][cnt][nday] == -1) {
                    visited[ny][nx][cnt][nday] = visited[y][x][cnt][day] + 1;
                    q.push({ny, nx, nday, cnt});
                } else if (visited[ny][nx][cnt][nday] > visited[y][x][cnt][day] + 1) {
                    visited[ny][nx][cnt][nday] = visited[y][x][cnt][day] + 1;
                    q.push({ny, nx, nday, cnt});
                }
            } else { // 벽
                if (day == 1) {
                    if (visited[y][x][cnt][nday] == -1) {
                        visited[y][x][cnt][nday] = visited[y][x][cnt][day] + 1;
                        q.push({y, x, nday, cnt});
                    } else if (visited[y][x][cnt][nday] > visited[y][x][cnt][day] + 1) {
                        visited[y][x][cnt][nday] = visited[y][x][cnt][day] + 1;
                        q.push({y, x, nday, cnt});
                    }
                } else {
                    if (cnt + 1 > k) continue;
                    if (visited[ny][nx][cnt + 1][nday] == -1) {
                        visited[ny][nx][cnt + 1][nday] = visited[y][x][cnt][day] + 1;
                        q.push({ny, nx, nday, cnt + 1});
                    } else if (visited[ny][nx][cnt + 1][nday] > visited[y][x][cnt][day] + 1) {
                        visited[ny][nx][cnt + 1][nday] = visited[y][x][cnt][day] + 1;
                        q.push({ny, nx, nday, cnt + 1});
                    }
                }
            }
        }
    }

    int answer = -1;
    for (int i = 0; i <= k; ++i) {
        for (int j = 0; j < 2; ++j) {
            int v = visited[n-1][m-1][i][j];
            if (v == -1) continue;
            if (answer == -1 || answer > v) answer = v;
        }
    }
    printf("%d\n", answer);
    return 0;
}
