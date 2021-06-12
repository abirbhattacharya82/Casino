import java.util.*;
public class Twenty_one_sticks
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("WARNING: YOU WILL NEVER WIN THIS GAME");
		int x=21;
		while(x>1)
		{
			System.out.println("Pick Up 1-4 Sticks");
			int x_i=sc.nextInt();
			if (x_i>4 || x_i<1)
			{
				System.out.println("Illegal You are Disqualified");
				break;
			}
			else
			{
				x=x-5;
				int y=5-x_i;
				System.out.println("I pick "+y+" Sticks");
				System.out.println("Sticks Remaining: "+x);
			}
		}
		System.out.println("You Lost \n:(");		
	}
}