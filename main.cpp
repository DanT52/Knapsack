#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <tuple>

using namespace std;

struct Item {
    string name;
    int weight;
    int value;

    Item(const string& n, int w, int v) : name(n), weight(w), value(v) {}
};
struct DPEntry {
    set<int> used_indices;
    int total_value;
    int total_weight;

    DPEntry() : total_value(0), total_weight(0) {}
};


DPEntry knapsack(const vector<Item>& items, int max_weight) {
    vector<DPEntry> dp(max_weight + 1);

    // first loop though the items to include from the first to last item
    for (int i = items.size() - 1; i >= 0; --i) {

        // inner loop goes though from max_weight to 0
        // this is because the higher weights depend on the results from the lower
        // weights calculated in the previous loop
        for (int j = max_weight; j >= 1; --j) { 
            // at any given value we can either take that item or skip it
            int take = 0;
            if (j - items[i].weight >= 0) {
                take = items[i].value + dp[j - items[i].weight].total_value;
            }

            int skip = dp[j].total_value;

            // only need to modify if we take as the skip value is just the previous lops
            // value and is already in the dp array
            if (take > skip) {
                dp[j] = dp[j - items[i].weight];
                dp[j].used_indices.insert(i);
                dp[j].total_value = take;
                dp[j].total_weight = dp[j - items[i].weight].total_weight + items[i].weight;
            }
        }
    }

    return dp[max_weight];
}

int main() {
    int maxWeight;
    cin >> maxWeight;
    cin.ignore(); // ignore \n

    // read in all the items from std in into the item vector
    // this is a vector of Item structs.
    vector<Item> items;
    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue; // skip empty
        stringstream ss(line);
        string name;
        int weight, value;
        char delimiter;

        getline(ss, name, ';');
        ss >> weight >> delimiter >> value;

        items.emplace_back(name, weight, value);
    }

    // run the knapsack dp function
    DPEntry result = knapsack(items, maxWeight);

    // i do all this weird stuff to get the right output order
    // use a hashmap with the item name value and weight as the key
    // count how many times that exact item occured in the result
    map<tuple<string, int, int>, int> item_counts;
    for (int idx : result.used_indices) {
        const Item& item = items[idx];
        auto key = make_tuple(item.name, item.weight, item.value);
        item_counts[key]++;
    }

    // now we loop though the input items
    // if a patricular item is in the item_counts hashmap and its count is > 0
    // then we print that item and decrement its count in the hashmap by 1
    for (const Item& item : items) {
        auto key = make_tuple(item.name, item.weight, item.value);
        if (item_counts[key] > 0) {
            cout << item.name << ", " << item.weight << ", " << item.value << endl;
            item_counts[key]--;
        }
    }

    // print the final weight and stuff
    cout << "final weight: " << result.total_weight << endl;
    cout << "final value: " << result.total_value << endl;

    return 0;
}