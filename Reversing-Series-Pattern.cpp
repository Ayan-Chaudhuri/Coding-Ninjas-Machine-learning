# Print the following pattern for the given number of rows.
# Pattern for N = 5
  1 
  3 2 
  4 5 6 
  10 9 8 7 
  11 12 13 14 15

    
void printPatt(int n)
{
     int j, k = 0; 
      
    // loop to decide the row number 
    for (int i=1; i<=n; i++) 
    { 
        // if row number is odd 
        if (i%2 != 0) 
        { 
            // print numbers with the '*' sign in 
            // increasing order 
            for (j=k+1; j<k+i; j++) 
                cout << j << " "; 
            cout << j++ << endl; 
              
            // update value of 'k'     
            k = j;     
        } 
          
        // if row number is even 
        else
        { 
            // update value of 'k' 
            k = k+i-1; 
              
            // print numbers with the '*' in 
            // decreasing order 
            for (j=k; j>k-i+1; j--) 
                cout << j << " "; 
            cout << j << endl;     
        } 
    } 
}
