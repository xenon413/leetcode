class Solution 
{
public:
    ListNode* head = nullptr;
    ListNode* back = nullptr;
    void push_back(int data)
    {  
        ListNode* temp = new ListNode();
        temp->val = data;
        temp->next = nullptr;
        if (head == nullptr)
        {
            head = temp;
            back = temp;
            return;
        }
        back->next = temp;
        back = temp;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        int carry=0;
        int val;
        while (l1 != nullptr && l2 != nullptr)
        {
            val = l1->val + l2->val;
            l1=l1->next;
            l2 = l2->next;
            push_back((val + carry) % 10);
            if (val + carry >= 10)
                carry = 1;
            else
                carry = 0;
        }
        while (l1 != nullptr)
        {
            val = l1->val;
            l1 = l1->next;
            push_back((val + carry) % 10);
            if (val + carry >= 10)
                carry = 1;
            else
                carry = 0;
        }
        while(l2!=nullptr)
        {
            val = l2->val;
            l2=l2->next;
            push_back((val + carry) % 10);
            if (val + carry >= 10)
                carry = 1;
            else
                carry = 0;
        }
        if (carry == 1)
            push_back(1);
        return head;
    }
};