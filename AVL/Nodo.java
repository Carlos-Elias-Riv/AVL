package AVL;

public class Nodo<T extends Comparable<T>> implements PrintableNode {
    T elem;
    Nodo<T> izq, der, papa;
    int cont;
    int fe;

    public Nodo() {
        elem = null;
        izq = null;
        der = null;
        cont = 0;
    }

    public Nodo<T> getPapa() {
        return papa;
    }


    public Nodo(T elem) {
        cont = 1;
        this.elem = elem;
    }

    public int hijos() {
        int h = 0;
        if(izq != null)
            h+=1;
        if(der != null)
            h+=1;

        return h;
    }

    public int descendencia() {
        int cont = 0;
        if (izq != null)
            cont += izq.descendencia() + 1;
        if (der != null)
            cont += der.descendencia() + 1;


        return cont;
    }
    public  void  cuelga(Nodo<T> nuevo){
        if(nuevo == null)
            return;
        if(nuevo.getElem().compareTo(elem) <= 0){
            izq = nuevo;
            izq.setPapa(this);
        }
        else{
            der = nuevo;
            der.setPapa(this);
        }

    }



    public T getElem() {
        return elem;
    }

    public Nodo<T> getIzq() {
        return izq;
    }

    public Nodo<T> getDer() {
        return der;
    }

    public void setIzq(Nodo<T> nodo) {

        izq = nodo;
        if(izq != null)
            izq.setPapa(this);
    }

    public void setElem(T elem) {
        this.elem = elem;
    }

    public void setDer(Nodo<T> nodo) {
        der = nodo;
        if(der != null)
            der.setPapa(this);
    }

    public void setPapa(Nodo<T> papa) {
        this.papa = papa;
    }

    public int getFe() {
        return fe;
    }

    public void setFe(int fe) {
        this.fe = fe;
    }

    public String toString() {
        return "(" + elem + "," + fe + ")";
    }

}
