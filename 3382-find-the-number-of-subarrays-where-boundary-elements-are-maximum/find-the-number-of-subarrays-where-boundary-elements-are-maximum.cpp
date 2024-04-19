class Solution {
public:
    long long numberOfSubarrays(vector<int>& nums) {
        int n = nums.size();
        stack<pair<int,int>> st;
        long long cnt =0;
        for(int i=0;i<n;i++){
            int k = nums[i];
            while(!st.empty() && i<n &&st.top().first<nums[i]){
                st.pop();
            }
            if(st.empty()){
                st.push({nums[i],1});
            }
            else if(!st.empty() && i<n && st.top().first==nums[i]){
                cnt+=st.top().second;
                int h = st.top().second+1;
                // st.push({nums[i],});
                st.pop();
                st.push({nums[i],h});
            }
            else if(i<n && st.top().first>nums[i]){
                st.push({nums[i],1});
            }
        }
        return cnt+n;
    }
};