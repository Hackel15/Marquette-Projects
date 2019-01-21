package random;

public class PizzaOrder {
	
	public Pizza pizza1;
	public Pizza pizza2;
	public Pizza pizza3;
	public int numPizzas;
	
	public PizzaOrder() {
		// TODO Auto-generated constructor stub
	}
	
	public void SetNumPizzas(int numPizza) {
		this.numPizzas = numPizza;
	}
	
	public void setPizza1(Pizza pizza) {
		if (this.numPizzas > 0) {
			this.pizza1 = pizza;
		}
	}
	
	public void setPizza2(Pizza pizza) {
		if (this.numPizzas > 1) {
			this.pizza2 = pizza;
		}
	}
	
	public void setPizza3(Pizza pizza) {
		if (this.numPizzas > 2) {
			this.pizza3 = pizza;
		}
	}
	
	public double calcTotal() {
		if (this.numPizzas == 1) {
			return (this.pizza1.calcCost());
		}
		else if (this.numPizzas == 2) {
			return (this.pizza1.calcCost() + this.pizza2.calcCost());
		}
		else if (this.numPizzas == 3) {
			return (this.pizza1.calcCost() + this.pizza2.calcCost() + this.pizza3.calcCost());
		}
		else {
			return 0.0;
		}
	}
	
	public void printReceipt() {
		if (this.numPizzas == 1) {
			System.out.println(this.pizza1.getDescription());
		}
		else if (this.numPizzas == 2) {
			System.out.println(this.pizza1.getDescription());
			System.out.println(this.pizza2.getDescription());
		}
		else if (this.numPizzas == 3) {
			System.out.println(this.pizza1.getDescription());
			System.out.println(this.pizza2.getDescription());
			System.out.println(this.pizza3.getDescription());
		}
		System.out.println("Total Order Cost: " + this.calcTotal());
	}

	public static void main(String[] args) {
		Pizza pizza1 = new Pizza("Small", 1, 1, 1);
		Pizza pizza2 = new Pizza("Medium", 1, 1, 1);
		Pizza pizza3 = new Pizza("Large", 1, 1, 1);
		PizzaOrder dominosQueue = new PizzaOrder();
		
		//Orders 1 pizzas
		dominosQueue.SetNumPizzas(1);
		dominosQueue.setPizza1(pizza1);
		
		dominosQueue.printReceipt();
		
		//Orders 2 pizzas
		dominosQueue.SetNumPizzas(2);
		dominosQueue.setPizza1(pizza1);
		dominosQueue.setPizza2(pizza2);
		
		dominosQueue.printReceipt();
		
		//Orders 3 pizzas
		dominosQueue.SetNumPizzas(3);
		dominosQueue.setPizza1(pizza1);
		dominosQueue.setPizza2(pizza2);
		dominosQueue.setPizza3(pizza3);
		
		dominosQueue.printReceipt();
		
		
	}

}
