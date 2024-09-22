class Solution
{
  public:
    string lookandsay(int n) {
        if( n==1){
            return "1";
        }
        if( n==2){
             return "11";
        }
        string str = "11";
        int count = 1;
        while(n>=3){
            count = 1;
            string temp = "";
            for(int i=0;i<str.size()-1;i++){
                if(str[i]==str[i+1]){
                    count++;
                }
                else{
            
                    temp += to_string(count)+str[i];
                    count=1;
                }
            }
            temp+=to_string(count)+str[str.size()-1];
            str = temp;
            n--;
        }
        
        return str;
    }   
};