    class Solution {
        public int maxProfit(int[] prices) {
            int min = 10000;
            int max = 0;
            int profit=0;
            int op = 0;
            
            for (var i=0;i<prices.length;i++){
                if (prices[i] < min) {
                    min = prices[i];
                }        
                else if (prices[i]>max){
                    max = prices[i];
                }
                profit = prices[i] - min;
                if (profit>op){
                    op = profit;
                }            
            }

            if (op<=0){
                return 0;
            }
            return op;

        }
    }
