bool isLucky(int n) {
        int count = 2;
        while(count<=n){
            if(n%count==0){
                return false;
            }
            
            
            n=n-(n/count);
            count++;
            
        }
        
        return true;
    }