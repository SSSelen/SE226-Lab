#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int x, Node* n) { data = x; next = n; }
};

class Queue {
private:
    Node* first;
    Node* back;
    int count;
public:
    Queue() : first(nullptr), back(nullptr), count(0) {}

    bool isEmpty() {
        return first == nullptr;
    }

    void enqueue(int value) {
        Node* newNode = new Node(value, nullptr);
        if (back == nullptr) {
            first = back = newNode;
        } else {
            back->next = newNode;
            back = newNode;
        }
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty.";
            return;
        }
        Node* temp = first;
        first = first->next;
        if (first == nullptr) {
            back = nullptr;
        }
        delete temp;
        count--;
    }

    int top() {
        if (isEmpty()) {
            cout << "Queue is empty.";
            return -1;
        }
        return first->data;
    }

    int size() {
        return count;
    }

    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    }
};

int main() {
    Queue a;
    a.enqueue(14);
    a.enqueue(5);
    a.enqueue(25);
    cout << "Front item: " << a.top() << endl;
    cout << "Queue size: " << a.size() << endl;
    a.dequeue();
    cout << "Front item after dequeue: " << a.top() << endl;
    cout << "Queue size after dequeue: " << a.size() << endl;
    return 0;
}
