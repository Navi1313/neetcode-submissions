class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int start = 1, end =  0 , mid , ans , n = piles.size();      
        long long x = 0;
        for(int i = 0 ; i<n ; i++){
            end = max(end , piles[i]);
            //x += piles[i];
        }
        // start = x/h;
        // if(!start)
        // start = 1;

        while(start <= end){

            mid = start + (end-start)/2;

            long long totalTime = 0 ; 
            for(int i = 0 ; i<n ; i++){

                totalTime += piles[i]/mid ;
                if(piles[i]%mid)
                totalTime++;
            }

            if(totalTime > h){
                start = mid+1;
            }
            else{
                ans = mid ; 
                end = mid-1;
            }
        }
        return ans ; 
    }
};