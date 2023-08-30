//Spiral Print
//For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
   // a. First row(left to right)
   // b. Last column(top to bottom)
   // c. Last row(right to left)
  //  d. First column(bottom to top)
 //Mind that every element will be printed only once.


public class Solution {

	public static void spiralPrint(int mat[][]){
        if(mat.length==0){
            return;
        }
        int rowS=0,colS=0,rowE=mat.length-1;
        int colE=mat[0].length-1;
        int i=0,j=0,c=0;
        int mul=mat.length*mat[0].length;
        while(c<mul){
     	while(j<=colE){
            System.out.print(mat[i][j]+" ");
            c++;
            j++;
        }
        rowS+=1;
        i=rowS;
        j--;
        while(i<=rowE){
            System.out.print(mat[i][j]+" ");
            c++;
            i++;
        }
        colE-=1;
        j=colE;
        i--;
        while(j>=colS){
            System.out.print(mat[i][j]+" ");
            c++;
            j--;
        }
        rowE-=1;
        i=rowE;
        j++; 
        while(i>=rowS){
            System.out.print(mat[i][j]+" ");
            c++;
            i--;
        }
        colS+=1;
        i++;
        j=colS;    
       
    }
    }
}
