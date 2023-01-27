package AVL;

import java.util.ArrayList;

public class PruebasAVL {
    public static void borrarEImprimir(int elemento, AVL<Integer> datos){
        datos.borra(elemento);
        System.out.println(datos.imprimeInorden());
        datos.imprimeVisualmente();
    }
    public static void main(String[] args) {
        AVL datos = new <Integer> AVL();

        //int[] arre1 = {7,4,2,3,1,9,10, 11, 12, 17, 20}; // prueba general
        /*for(int i =0; i< arre.length; i++)
            datos.inserta(arre[i]);*/
        /*
        for(int i =0; i< 10; i++) // prueba para derecha derecha
            datos.inserta(i);

         */
        for(int i = 1; i<11; i++) // prueba izquierda izquierda
            datos.inserta(i);
        //int[] arre = {4, -1, 7,-2,2, 3}; // prueba izquierda derecha

        /*int[] arre1 = {4,2,7, 1, 3, 9};
        for(int i =0; i< arre1.length; i++)
            datos.inserta(arre1[i]);*/
        datos.imprimeVisualmente();

        /*System.out.println(datos.borra(2).getPapa().getElem());
        datos.imprimeVisualmente();
        //datos.borra(3);
        System.out.println("\nMi papa fue: ");
        System.out.println(datos.borra(3).getPapa().getElem());*/
        /*borrarEImprimir(4, datos);
        borrarEImprimir(7, datos);
        borrarEImprimir(6, datos);*/


    }
}
