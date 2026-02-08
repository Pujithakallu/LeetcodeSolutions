/*
 * Problem 146: LRU Cache
 * =====================
 * Difficulty: Medium
 * Tags: Hash Table, Linked List, Design, Doubly-Linked List
 * Pattern: Design / Hash Map + Linked List
 *
 * Time Complexity:  O(1) per operation
 * Space Complexity: O(capacity)
 */

class LRUCache {
    int cap;
    list<pair<int,int>> lst;
    unordered_map<int, list<pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}
    
    int get(int key) {
        if (!mp.count(key)) return -1;
        lst.splice(lst.end(), lst, mp[key]);
        return mp[key]->second;
    }
    
    void put(int key, int value) {
        if (mp.count(key)) {
            mp[key]->second = value;
            lst.splice(lst.end(), lst, mp[key]);
            return;
        }
        if ((int)lst.size() == cap) {
            mp.erase(lst.front().first);
            lst.pop_front();
        }
        lst.push_back({key, value});
        mp[key] = prev(lst.end());
    }
};
