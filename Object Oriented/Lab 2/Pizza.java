package random;

/*
 * Tyler Hackel
 * Tyler.Hackel@Marquette.edu
 * 9/4/18
 * Chapter 4 Review Question #11
 */

public class Pizza {
	private String size;
	private int cheeseToppings;
	private int pepperoniToppings;
	private int hamToppings;
	
	public Pizza(String size, int cheese, int pepperoni, int ham) {
		this.setSize(size);
		this.setCheeseToppings(cheese);
		this.setPepperoniToppings(pepperoni);
		this.setHamToppings(ham);
	}
	
	public String getDescription() {
		return "Size: " + this.size + ", # of cheese toppings: " + this.cheeseToppings 
				+ ", # of pepperoni toppings: " + this.pepperoniToppings + ", # of ham toppings: " +
				this.hamToppings + ", Cost: " + this.calcCost();
	}
	
	public double calcCost() {
		double cost = (this.cheeseToppings * 2.0) + (this.pepperoniToppings * 2.0) + (this.hamToppings * 2.0);
		if (this.size.equals("Small")) {
			cost += 10;
		} else if(this.size.equals("Medium")) {
			cost += 12;
		} else cost += 14;
		
		return cost;
	}

	public int getHamToppings() {
		return hamToppings;
	}

	public void setHamToppings(int hamToppings) {
		this.hamToppings = hamToppings;
	}

	public int getPepperoniToppings() {
		return pepperoniToppings;
	}

	public void setPepperoniToppings(int pepperoniToppings) {
		this.pepperoniToppings = pepperoniToppings;
	}

	public int getCheeseToppings() {
		return cheeseToppings;
	}

	public void setCheeseToppings(int cheeseToppings) {
		this.cheeseToppings = cheeseToppings;
	}

	public String getSize() {
		return size;
	}

	public void setSize(String size) {
		this.size = size;
	}
	
	public static void main(String[] args) {
		Pizza pie = new Pizza("Large", 1, 1, 2);
		System.out.println(pie.getDescription());

	}
}
