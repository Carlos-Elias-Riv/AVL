package AVL;


import java.util.ArrayList;

public class AVL<T extends Comparable<T>> {


    /* The attributes of the class AVL are raiz, which represents the root and cont that represents the quantity
       of elements in the tree
     */

    Nodo<T> raiz;
    int cont;

    // First we have an empty constructor, that initializes an empty AVL tree
    public AVL() {

        raiz = null;
        cont = 0;
    }
    // Another constructur, that intiliazes an AVL tree with one element
    public AVL(T elem) {
        raiz = new Nodo<T>(elem);
        cont+=1;
    }
    /* The inserta method is used to insert an element to the tree. If the tree is empty, the element becomes the root,
       if the tree is no

     */
    public void inserta(T elem) {
        Nodo<T> actual = raiz;
        Nodo<T> nuevo = new Nodo<T>(elem);
        boolean encontre = false;
        if (raiz == null) {
            raiz = nuevo;
            cont ++;
        }
        else{
            Nodo<T> papa = actual;
            while(actual != null && !encontre){
                papa = actual;
                if(nuevo.getElem().compareTo(actual.getElem())< 0 )
                    actual = actual.getIzq();
                else{
                    if(nuevo.getElem().compareTo(actual.getElem()) == 0)
                        encontre = true;
                    else
                        actual = actual.getDer();
                }
            }

            if(!encontre){
                actual = papa;
                actual.cuelga(nuevo);
                cont ++;
            }
            actual = nuevo;
            boolean termine = nuevo.getPapa() == null;
            while(!termine){
                if(actual == raiz)
                    termine = true;
                else {
                    papa = actual.getPapa();
                    if (actual == papa.getIzq()){
                        papa.setFe(papa.getFe()-1);
                    }
                    else
                        papa.setFe(papa.getFe()+1);
                    if(Math.abs(papa.getFe()) == 2){
                        rota(papa);
                        termine = true;
                    }
                    if(papa.getFe() == 0)
                        termine = true;
                }

                actual = papa;
            }
        }

    }
    public void rota(Nodo<T> alfa) { // recibe un nodo que sabe que esta en valor absoluto 2
        if(alfa.getFe() < 0) // izquierda
            if(alfa.getIzq().getFe() < 0) // izquierda
                rotaIzquierdaIzquierda(alfa);
            else // derecha
                rotaIzquierdaDerecha(alfa);
        else // derecha
            if(alfa.getDer().getFe() < 0) // izquierda
                rotaDerechaIzquierda(alfa);
            else // derecha
                rotaDerechaDerecha(alfa);

    }

    private Nodo<T> borraPrivado(T elem) {
        Nodo<T> nodo = encuentra(raiz,  elem);


        Nodo<T> resp = new Nodo<T>(elem);

        if(nodo == null)
            return null;
        resp.setPapa(nodo.getPapa());
        if(nodo.getIzq() == null && nodo.getDer() == null){
            if(nodo == raiz) {
                raiz = null;
            }
            if(nodo == nodo.getPapa().getIzq())
                nodo.getPapa().setIzq(null);
            else
                nodo.getPapa().setDer(null);
            cont --;
            return resp;
        }

        if(nodo.getIzq() == null || nodo.getDer() == null){
            if(nodo == raiz){
                if(nodo.getIzq()!= null) {
                    raiz = nodo.getIzq();
                    nodo.getIzq().setPapa(null);
                }
                else {
                    raiz = nodo.getDer();
                    nodo.getDer().setPapa(null);
                }
            }
            else{
                if(nodo.getDer() == null)
                    nodo.getPapa().cuelga(nodo.getIzq());
                else
                    nodo.getPapa().cuelga(nodo.getDer());

            }
            cont--;
            return resp;

        }

        Nodo<T> actual = nodo.getDer();
        while(actual.getIzq()!= null){
            actual = actual.getIzq();
        }

        nodo.setElem(actual.getElem());
        if(actual != nodo.getDer())
            actual.getPapa().setIzq(actual.getDer());
        else
            nodo.setDer(actual.getDer());

        return resp;
    }

    public void borra(T elem) {
        Nodo<T> borrado = borraPrivado(elem);
        if(borrado == null)
            return;



        //else falta que hacer cuando borro la raiz

        ajustarDespuesBorrar(borrado.getPapa());
        actualizacionFesForzada(raiz);
        if(Math.abs(raiz.getFe())== 2)
            rota(raiz);

    }



    private void ajustarDespuesBorrar(Nodo<T> actual) {
        if(actual == null)
            return;


        actualizaFes(actual);
        if(Math.abs(actual.getFe())== 2){
            rota(actual);
        }
        ajustarDespuesBorrar(actual.getPapa());

    }

    public void rotaIzquierdaIzquierda(Nodo<T> actual){ // recibe el nodo desfasado por dos
        Nodo<T> psi = null;
        psi = actual.getPapa();
        Nodo<T> beta = actual.getIzq();
        Nodo<T> d = actual.getDer();
        Nodo<T> c = beta.getDer();
        Nodo<T> omega = beta.getIzq();
        Nodo<T> a = omega.getIzq();
        Nodo<T> b = omega.getDer();




        beta.setDer(actual);
        actual.setIzq(c);

        if(psi!= null)
            psi.cuelga(beta);
        else{
            raiz = beta;
            beta.setPapa(null);
        }
        beta.setFe(0);
        actualizaFes(actual);

    }

    public void rotaDerechaDerecha(Nodo<T> alfa){ // recibe el nodo desfasado por dos

        Nodo<T> beta, omega, a, b, c, d;
        Nodo<T> psi = null;
        psi = alfa.getPapa();



        beta = alfa.getDer();
        omega= beta.getDer();
        a = alfa.getIzq();
        b = beta.getIzq();
        c = omega.getIzq();
        d = omega.getDer();

        beta.setIzq(alfa);
        alfa.setDer(b);


        if(psi!= null) {
            psi.cuelga(beta);

        }
        else {
            raiz = beta;
            beta.setPapa(null);
        }
        beta.setFe(0);
        actualizaFes(alfa);





    }


    public void rotaIzquierdaDerecha(Nodo<T> alfa) {
        Nodo<T> beta, omega, a, b, c, d;
        Nodo<T> psi = null;


        psi = alfa.getPapa();

        beta = alfa.getIzq();
        d = alfa.getDer();
        a = beta.getIzq();
        omega = beta.getDer();
        b = omega.getIzq();
        c= omega.getDer();

        beta.setDer(b);
        omega.setIzq(beta);
        omega.setDer(alfa);
        alfa.setIzq(c);

        if(psi!= null)
            psi.cuelga(omega);
        else{
            raiz = omega;
            omega.setPapa(null);
        }

        omega.setFe(0);
        actualizaFes(beta);
        actualizaFes(alfa);

    }

    public void rotaDerechaIzquierda(Nodo<T> alfa) {
        Nodo<T> beta, omega, a, b, c, d, psi;
        psi = alfa.getPapa();

        beta = alfa.getDer();
        a = alfa.getIzq();
        omega = beta.getIzq();
        b = omega.getIzq();
        c = omega.getDer();
        d = beta.getDer();






        omega.setDer(beta);
        alfa.setDer(b);
        omega.setIzq(alfa);
        beta.setIzq(c);

        if(psi != null)
            psi.cuelga(omega);
        else{
            raiz = omega;
            omega.setPapa(null);
        }

        omega.setFe(0);
        actualizaFes(alfa);
        actualizaFes(beta);


    }

    public String imprimeInorden() {
        ArrayList<String> al = new ArrayList<String>();
        inOrden(al);
        return al.toString();

    }

    private ArrayList<String> inOrden(ArrayList<String> al) {
        Nodo<T> actual = raiz;
        inOrden(actual, al);
        return al;
    }

    private void inOrden(Nodo<T> actual, ArrayList<String> al) {
        if(actual == null)
            return;
        inOrden(actual.getIzq(), al);
        al.add(actual.getElem().toString());
        inOrden(actual.getDer(), al);
    }

    public Nodo<T> encuentra(Nodo<T> actual, T elem) {
        if(actual == null)
            return null;
        if(actual.getElem().equals(elem))
            return actual;
        Nodo<T> temporal = encuentra(actual.getDer(), elem);
        if(temporal== null)
            return encuentra(actual.getIzq(), elem);
        else
            return temporal;
    }



    public void actualizaFes(Nodo<T> nodo) {

       if(nodo!= null) {

           if (nodo.getIzq() != null && nodo.getDer() != null) {// tiene ambos hijos

               nodo.setFe(alturaArbol(nodo.getDer(), 1) - alturaArbol(nodo.getIzq(), 1));
           }
           else if (nodo.getIzq() != null) { // tiene solo hijo izquierdo


               nodo.setFe(-alturaArbol(nodo.getIzq(), 1));
           }
           else if(nodo.getDer()!= null) { // tiene solo hijo derecho


               nodo.setFe(alturaArbol(nodo.getDer(), 1));
           }
           else // no tiene ningun hijo
               nodo.setFe(0);
       }

    }

    public void actualizacionFesForzada(Nodo<T> nodo) {
        if(nodo == null)
            return;
        actualizaFes(nodo);
        actualizacionFesForzada(nodo.getIzq());
        actualizacionFesForzada(nodo.getDer());

    }

    public int alturaArbol(Nodo<T> nodo, int count) {
        if(nodo == null)
            return count;
        else {

            if(nodo.getIzq() != null || nodo.getDer() != null)
                count = count +1;
            int max1 = alturaArbol(nodo.getIzq(), count);
            int max2 = alturaArbol(nodo.getDer(), count);
            if(max1 > max2)
                return max1;
            else
                return max2;
        }




    }

    public void imprimeArbol(Nodo<T> actual, int espacio) {
        if(actual == null)
            return;
        espacio = espacio +10;
        imprimeArbol(actual.getDer(), espacio);
        for(int i =0; i< espacio; i++)
            System.out.print(" ");

        System.out.println("(" + actual.getElem() + ","+ actual.getFe()+")");
        System.out.println("\n");
        imprimeArbol(actual.getIzq(), espacio);
    }

    public void imprimeVisualmente() {
        imprimeArbol(raiz, 0);
    }


}
