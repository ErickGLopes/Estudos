/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programawhile;


/**
 *
 * @author devshi
 */
public class ProgramaWhile {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.print("Números ímpares:");
        int c = 0;
        while (c < 10) {
            c += 1;
            if (c % 2 == 0) {
                continue;
            }
            System.out.print(" " + c);
        }
        System.out.println("");
    }
    
}
