#include <iostream>

struct List {
    int val;
    List* next;
    List(int v): val(v), next(nullptr) {};
    void print() {
        List* current = this;
        std::cout << "HEAD: [";
        while (current) {
            std::cout << current->val << "]-->[";
            current = current->next;
        }
        std::cout << "NULL]" << std::endl;
    }
};

void reverseList(List** head) {
    List *prev = nullptr, *curr = nullptr, *next = nullptr;

    curr = *head;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
}

void clearList(List *head) {
    if (head->next)
        clearList(head->next);
    delete head;
    head = nullptr;
}

int main() {
    List* root = new List(2);
    List* l1 = new List(4);
    List* l2 = new List(6);
    List* l3 = new List(8);
    List* l4 = new List(10);
    List* l5 = new List(12);
    List* l6 = new List(14);
    List* l7 = new List(16);
    List* l8 = new List(18);
    List* l9 = new List(20);

    root->next = l1;
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = l6;
    l6->next = l7;
    l7->next = l8;
    l8->next = l9;
    l9->next = nullptr;

    std::cout << "Linked list before:\n";
    root->print();

    reverseList(&root);

    std::cout <<"\nLinked list after reversing it:\n";
    root->print();

    std::cout << "\nOnce more:\n";
    reverseList(&root);
    root->print();

    reverseList(&root);
    root->print();

    reverseList(&root);
    root->print();

    int i = 0;
    while (i < 100) {
        std::cout << '.';
        reverseList(&root);
        i++;
    }
    std::cout << std::endl;
    root->print();
    clearList(root);
    return 0;
}