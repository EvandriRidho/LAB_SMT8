import java.util.Scanner; 

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan Bilangan Pertama : ");
        int firstNumber = scanner.nextInt();

        System.out.print("Masukkan Bilangan Kedua : ");
        int secondNumber = scanner.nextInt(); 

        System.out.println(firstNumber + " + " + secondNumber + " : " + (firstNumber + secondNumber));
        System.out.println(firstNumber + " - " + secondNumber + " : " + (firstNumber - secondNumber));
        System.out.println(firstNumber + " * " + secondNumber + " : " + (firstNumber * secondNumber));
        System.out.println(firstNumber + " / " + secondNumber + " : " + (firstNumber / secondNumber));
        
        scanner.close(); 
    }
}