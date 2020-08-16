import java.util.*;
class Main
{
  public static void main(String[] args)
  {
    Scanner sc=new Scanner(System.in);
    int t=sc.nextInt();
    while(t>0)
    {
      t--;
      int n=sc.nextInt();
      int[] a=new int[n];
      for(int i=0;i<n;i++)
        a[i]=sc.nextInt();
      int res=0;
      int[] left=new int[n];
      int[] right=new int[n];
      int max=a[n-1];
      for(int i=n-2;i>=0;i--)
      {
        if(max>a[i])
		right[i]=max;
        else right[i]=-1;
        if(a[i]>max)
        {
          max=a[i];
        }
      }
      TreeSet<Integer> set = new TreeSet<>();
      for(int i=1;i<n;i++)
      {
        set.add(a[i-1]);
        Integer result=set.lower(a[i]);
        if(result!=null)
          left[i]=result;
        else left[i]=-1;
      }
      for(int i=1;i<n-1;i++)
      {
        if(left[i]!=-1 && right[i]!=-1)
        res=Math.max(res,left[i]-a[i]+right[i]);
      }
      System.out.println(res);
    }
  }
}