class Solution {
public:
    template<class Value, class Storage, class Comparator>
    struct priority_queue_with_erase
    {
        const Value& top() const{ purge(); return queued.top(); }
        void pop() { purge(); queued.pop(); }
        bool empty() const { return queued.size() == erased.size(); }
        size_t size() const { return queued.size() - erased.size(); }
        void push(const Value& v) { queued.push(v); }
        void erase(const Value& v) { erased.push(v); }
    
    private:
        void purge() const{
            while(!erased.empty() && erased.top() == queued.top()) {
                erased.pop();
                queued.pop();
            }
        }
        mutable priority_queue<Value, Storage, Comparator> queued, erased;
    };

    struct sum_n_smallest
    {
        template<class Iter>
        sum_n_smallest(Iter begin, Iter end) {
            for(auto i = begin; i < end; ++i) {
                smaller.push(*i);
                sum += *i;
            }
        }

        void add_and_drop(int a, int d) {
            const int top_larger = larger.top();
            if(a >= top_larger == d >= top_larger) {
                 if(a == d) return;
                 if(a >= top_larger){
                    larger.erase(d);
                    larger.push(a);
                } else{
                  smaller.erase(d);
                  smaller.push(a);
                  sum += a - d;
                }
                return;
            }
            drop(d, top_larger);
            add(a);
        }

        void add(int i) {
            const int old_top = smaller.top();
            if(i < old_top) {
                smaller.push(i);
                smaller.pop(); 
                larger.push(old_top);
                sum += i - old_top;
            } else {
                larger.push(i);
            }
        }

        void drop(int i, int old_top) {
            if(i < old_top){
                smaller.erase(i);
                larger.pop();
                smaller.push(old_top);
                sum += old_top - i;
            } else {
                larger.erase(i);
            }
        }
        long long cost() const {
            return sum;
        }
    private: 
        long long sum = 0;
        priority_queue_with_erase<int, vector<int>, less<>> smaller;
        priority_queue_with_erase<int, vector<int>, greater<>> larger;
    };

    long long minimumCost(const vector<int>& nums, int k, int dist) const{
        
        // The special case when dist == k-2
        if(dist == k-2){
            long long run_sum = 0;
            for(int i = 1; i < dist + 2; ++i) {
                run_sum += nums[i];
            }
            long long min_run_sum = run_sum;
            for(auto i = dist + 2; i < nums.size(); ++i) {
                run_sum += nums[i] - nums[i - dist - 1];
                min_run_sum = min(min_run_sum, run_sum);
            }
            return nums[0] + min_run_sum;
        }
        sum_n_smallest sum_n(nums.begin() + 1, nums.begin() + k);
        for(auto i = nums.begin() + k; i < nums.begin() + dist + 2; ++i){
            sum_n.add(*i);
        }
        long long min_cost = sum_n.cost();
        for(auto i = nums.begin() + dist + 2; i < nums.end(); ++i){
            sum_n.add_and_drop(*i,*(i - dist - 1));
            min_cost = min(min_cost, sum_n.cost());
        }
        return nums[0] + min_cost;
    }
};