#include <iostream>
#include <vector>

using namespace std;

void compute_beauty() {
    int num_nodes;
    cin >> num_nodes;


    vector<vector<int>> graph(num_nodes + 1);

    
    for (int i = 0; i < num_nodes - 1; ++i) {
        int node1, node2;
        cin >> node1 >> node2;
        graph[node1].push_back(node2);
        graph[node2].push_back(node1);
    }

    int leaf_nodes = 0;

    
    for (int i = 1; i <= num_nodes; ++i) {
        if (graph[i].size() == 1) {
            ++leaf_nodes;
        }
    }

    int internal_nodes = num_nodes - leaf_nodes;

    
    int beauty_value = leaf_nodes * 3 + internal_nodes * 2;

    cout << beauty_value << endl;
}

int main() {
    int test_cases;
    cin >> test_cases;

    
    while (test_cases--) {
        compute_beauty();
    }

    return 0;
}
