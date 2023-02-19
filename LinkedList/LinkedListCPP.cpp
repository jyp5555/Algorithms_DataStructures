#include <iostream>
using namespace std;

struct Node
{
    struct Node *next;//*prev;//
    int data;
};

struct Head
{
    Node* head;
};

class LinkedListCPP
{
private:
    /* data */
public:
    Head* createList(){
        Head* H = new Head;
        H->head = NULL;
        return H;
    }
    
    void addNodeLast(Head* H, int inputData){
        Node* NewNode = new Node;
        Node* LastNode;
        NewNode->data = inputData;
        NewNode->next = NULL;
        
        if(H->head == NULL){
            H->head = NewNode;
            return;
        }

        LastNode = H->head;
        while(LastNode->next != NULL) LastNode = LastNode->next;
        LastNode->next = NewNode;
    }

    void deleteNodeLast(Head* H){
        Node* prevNode;
        Node* delNode;

        if(H->head == NULL) return;
        if(H->head->next == NULL){
            delete H->head;
            H->head = NULL;
            return;
        }else{
            prevNode = H->head;
            delNode = H->head->next;
            while (delNode->next != NULL)
            {
                prevNode = delNode;
                delNode = prevNode->next;
            }
            free(delNode);
            prevNode->next = NULL;
        }
    }

    void addNodeHere(Head* H, int afterData, int addData){
        Node* prevNode;
        prevNode = H->head;

        while(prevNode->data != afterData){
            prevNode = prevNode->next;
        }

        Node* NewNode = new Node;
        NewNode->data = addData;
        NewNode->next = prevNode->next;
        prevNode->next = NewNode;
        return;
    }

    void deleteNodeHere(Head* H, int delData){
        Node* delNode;
        Node* prevNode;
        prevNode = H->head;

        while(prevNode->next->data != delData){
            prevNode = prevNode->next;
        }

        delNode = prevNode->next;
        prevNode->next = delNode->next;

        free(delNode);
        return;
    }

    void searchNode(Head* H, int searchData){
        Node* someNode;
        someNode = H->head;

        while (someNode->data != searchData)
        {
            someNode = someNode->next;
        }

        cout << someNode->data <<endl;
        return;
    }

    void printList(Head* H){
        Node* p;
        p = H->head;

        while(p != NULL){
            cout << p->data;
            p=p->next;
            if(p!= NULL) cout << "-->";
        }

        cout << "" << endl;
    }
};

int main(void){
    LinkedListCPP lists;
    
    Head* current;
    current = lists.createList();
    lists.addNodeLast(current,1);
    lists.addNodeLast(current,2);
    lists.addNodeLast(current,4);
    lists.printList(current);
    lists.addNodeHere(current,2,3);
    lists.printList(current);
    lists.deleteNodeLast(current);
    lists.printList(current);
    lists.deleteNodeHere(current,2);
    lists.printList(current);
    lists.searchNode(current,3);
    lists.printList(current);
}

