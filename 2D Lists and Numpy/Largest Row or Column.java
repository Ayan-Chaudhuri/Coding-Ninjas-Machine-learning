//Largest Row or Column
//For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row/column) 
//amongst all the rows and columns.
//Note :
//If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider 
//the ith row as answer.

public class Solution {

	
	public static void findLargest(int input[][]){
		
		/* Your class should be named Solution.
		* Don't write main() function.
	 	* Don't read input, it is passed as function argument.
	 	* Print output as specified in the question
		*/
        
        int sum=0,largestRow=Integer.MIN_VALUE,rn=0;
        for(int i=0;i<input.length;i++)
        {   sum=0;
            for(int j=0;j<input[0].length;j++)
            {
                sum+=input[i][j];
            }
            if(sum>largestRow){
                largestRow=sum;
                rn=i;}
        }
	
    
        int sum1=0,largestCol=Integer.MIN_VALUE,cn=0;
        for(int j=0;j<input[0].length;j++)
        {   sum1=0;
            for(int i=0;i<input.length;i++)
            {
                sum1+=input[i][j];
            }
         
            if(sum1>largestCol){
                largestCol=sum1;
                cn=j;}
        }
        
      //  System.out.println(sum1);
	if(largestRow>=largestCol)
    {System.out.print("row "+rn+" "+largestRow);
        //System.out.print(rn+" ");
    //System.out.print(largestRow);
    }else if(largestRow<largestCol){
         System.out.print("column "+cn+" "+largestCol);
        //System.out.print(cn+" ");
    //System.out.print(largestCol);
    }


	}

	
}
