/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package numeros;

import java.util.Scanner;

/**
 *
 * @author devshi
 */
public class Numeros {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int n, s = 0;
        String resp = "S";
        Scanner t = new Scanner(System.in);
        do {
            System.out.print("Digite um número: ");
            n = t.nextInt();
            s += n;
            System.out.print("Deseja continuar? [S/n]: ");
            resp = t.next().toUpperCase();
        } while (resp.equals("S"));
        System.out.println("=-=-=-=-=-=-=-=-=");
        System.out.println("A soma é " + s);
        System.out.println("=-=-=-=-=-=-=-=-=");

        
    }
    
}
