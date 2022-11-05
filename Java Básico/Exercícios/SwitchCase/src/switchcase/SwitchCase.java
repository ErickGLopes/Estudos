/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package switchcase;

import java.util.Scanner;

/**
 *
 * @author devshi
 */
public class SwitchCase {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner t =  new Scanner(System.in);
        System.out.print("Qtde de pernas: ");
        int pernas = t.nextInt();
        String tipo = "Isso é um";
        switch (pernas) {
            case 1:
                tipo += " Saci";
                break;
            case 2:
                tipo += " Bípede";
                break;
            case 3:
                tipo += " Tripé";
            case 4:
                tipo += " Quadrúpede";
                break;
            case 6:
            case 8:
                tipo += "a Aranha";
                break;
            default:
                tipo += " ET";
        }
        System.out.println(tipo);
        
        
    }
    
}
