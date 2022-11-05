/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package operadoresaritimeticos;

/**
 *
 * @author devshi
 */
public class OperadoresAritimeticos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        /*int n1 = 3;
        int n2 = 5;
        float m = (float) (n1 + n2) / 2;
        System.out.printf("A média é %.2f\n", m);*/
        
        /*int numero = 10;
        int valor = 5 + ++numero;
        System.out.println(numero);
        System.out.println(valor);*/
        
        int num1 = (int) Math.pow(5, 2);
        int num2 = (int) Math.sqrt(num1);
        int num3 = (int) Math.cbrt(27); // Raíz cúbica
        int num4 = (int) Math.abs(-15); // Exclui o negativo do número
        float num5 = (float) Math.PI;
        float num6 = (float) Math.floor(3.9); // Faz o arredondamento sempre para baixo, floor = chão
        float num7 = (float) Math.ceil(3.1); // Faz o arredondamento sempre para cima
        float num8 = (float) Math.round(8.4); // Arredondamento aritimético
        double num9 =  20 + Math.random() * (30-20);
        
        System.out.println("Número 1 = "+ num1);
        System.out.println("Número 2 = "+ num2);
        System.out.println("Número 3 = "+ num3);
        System.out.println("Número 4 = "+ num4);
        System.out.println("Número 5 = "+ num5);
        System.out.println("Número 6 = "+ num6);
        System.out.println("Número 6 = "+ num7);
        System.out.println("Número 6 = "+ num8);
        System.out.println("Número 6 = "+ (int) num9);
    }
    
}
