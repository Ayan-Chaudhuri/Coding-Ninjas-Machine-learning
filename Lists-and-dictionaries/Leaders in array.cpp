# Given an integer array A of size n. Find and print all the leaders present in the input array. An array element A[i] is called 
# Leader, if all the elements following it (i.e. present at its right) are less than or equal to A[i].
# Print all the leader elements separated by space and in the same order they are present in the input array.


void Leaders(int arr[],int len)
{
	for (int i = 0; i < len; i++)
   {
       for (int j = i; j < len; j++)
       {
           if (arr[i] < arr[j])
           {
               break;
           }
           if (j == len - 1)
               printf("%d ", arr[i]);
       }
   }
}
