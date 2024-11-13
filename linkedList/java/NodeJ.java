package java;
public class NodeJ {
    private int data;
    private NodeJ next;

    public NodeJ(int data) {
        this.data = data;
        this.next = null;
    }
    public int getData() {
        return this.data;
    }
    public NodeJ getNext() {
        return this.next;
    }
    public void setNext(NodeJ next) {
        this.next = next;
    }
}