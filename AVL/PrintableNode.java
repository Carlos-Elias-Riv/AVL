package AVL;

public interface PrintableNode <T extends Comparable<T>> {
    PrintableNode getIzq();
    PrintableNode getDer();
    T getElem();
}
