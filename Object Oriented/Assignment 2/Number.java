package Learning;

public class Number 
{
   private int num;
   
   public Number(int num)
   {
	   this.num = num;
   }
   
   public static Number addNumbers(Number n1, Number n2)
   {
	   return new Number(n1.num + n2.num);
   }
   
   public Number addNumbers(Number n)
   {
	   return new Number(this.num + n.num);
   }
   
   public static void main(String []args)
   {
	   Number num1 = new Number(10);
	   Number num2 = new Number(20);
	   //ans1 should be  30
	   Number ans1 = Number.addNumbers(num1, num2);
	   // ans2 should be 30
	   Number ans2 = num1.addNumbers(num2);
   }
}

class NumberAlternate 
{
   private int num;
   
   public NumberAlternate(int num)
   {
	   this.num = num;
   }
   
   public static Number addNumbers(NumberAlternate n1, NumberAlternate n2)
   {
	   return new Number(n1.num + n2.num);
   }
   
   public void addNumbers(NumberAlternate n)
   {
	   this.num = this.num + n.num;
   }
   
   public static void main(String []args)
   {
	   NumberAlternate num1 = new NumberAlternate(10);
	   NumberAlternate num2 = new NumberAlternate(20);
	   // num1 should be 30
	   num1.addNumbers(num2);
   }
}
