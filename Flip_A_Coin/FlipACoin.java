import java.util.*;
public class FlipACoin
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		List<Integer> list = new ArrayList<>();
		list.add(0);
        list.add(1);
		FlipACoin obj=new FlipACoin();
		System.out.println("Here's your chance to win Huge prize");
		System.out.println("All you have to do is guess what will be falling when we will be tossing the coin");
		System.out.println("Choose H for Head and T for Tails");
		char ch=sc.next().charAt(0);
		int s=0;
		while(true)
		{
			int x=obj.getRandomElement(list);
			if ((x==0) && (ch=='H' || ch=='h'))
			{
				s=s+100;
				System.out.println("You Won 100"+"$");
			}
			else if ((x==1) && (ch=='T' || ch=='t'))
			{
				s=s+100;
				System.out.println("You Won 100"+"$");
			}
			else
			{
				System.out.println("You Lost All Your Money :(");
				break;
			}
			System.out.println("Do You Still want to keep playing? Y/N");
			char z=sc.next().charAt(0);
			if (z=='N'||z=='n')
			{
				System.out.println("Wise Men and Women of take a step back wise choice\nYour Current Balance=> "+s);
				break;
			}
			System.out.println("Choose H for Head and T for Tails");
			ch=sc.next().charAt(0);
		}
	}
	public int getRandomElement(List<Integer> list)
    {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()));
    }
}