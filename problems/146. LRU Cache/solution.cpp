class Node
{
public:
    int key;
    int value;
    Node *prev;
    Node *next;

    Node(int key, int value)
    {
        this->key = key;
        this->value = value;
        this->prev = NULL;
        this->next = NULL;
    }

    void removeBindings()
    {
        if (this->prev != NULL)
            this->prev->next = this->next;
        if (this->next != NULL)
            this->next->prev = this->prev;
        this->prev = NULL;
        this->next = NULL;
    }
};

class DoublyLinkedList
{
public:
    Node *head;
    Node *tail;

    DoublyLinkedList()
    {
        this->head = NULL;
        this->tail = NULL;
    }

    void setHeadTo(Node *node)
    {
        if (this->head == node)
            return;
        else if (this->head == NULL)
        {
            this->head = node;
            this->tail = node;
        }
        else
        {
            if (node == this->tail)
                this->removeTail();
            node->removeBindings();
            this->head->prev = node;
            node->next = this->head;
            this->head = node;
        }
    }

    void removeTail()
    {
        if (this->tail == NULL)
            return;
        if (this->tail == this->head)
        {
            this->tail = NULL;
            this->head = NULL;
            return;
        }
        this->tail = this->tail->prev;
        this->tail->next = NULL;
    }
};

class LRUCache
{
public:
    int maxSize;
    int currentSize;
    DoublyLinkedList *linkedlist;
    unordered_map<int, Node *> cache;
    LRUCache(int maxSize)
    {
        this->maxSize = maxSize > 1 ? maxSize : 1;
        this->currentSize = 0;
        this->linkedlist = new DoublyLinkedList();
    }

    int get(int key)
    {
        if (this->cache.find(key) == this->cache.end())
        {
            return -1;
        }
        Node *node = this->cache[key];
        this->linkedlist->setHeadTo(node);
        return node->value;
    }

    void put(int key, int value)
    {
        // if the key is not in the cache
        if (this->cache.find(key) == this->cache.end())
        {
            // check if we have got enough capacity
            if (this->currentSize < this->maxSize)
                this->currentSize++;
            else
                this->evictLeastUsed();
            Node *node = new Node(key, value);
            this->cache[key] = node;
            this->linkedlist->setHeadTo(node);
        }
        else
        {
            cache[key]->value = value;
        }

        this->linkedlist->setHeadTo(cache[key]);
    }

    void evictLeastUsed()
    {
        int key = this->linkedlist->tail->key;
        this->linkedlist->removeTail();
        this->cache.erase(key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */