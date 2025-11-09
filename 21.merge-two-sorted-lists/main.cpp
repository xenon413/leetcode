class Solution 
{
public:
    ListNode* head = nullptr,* tail=nullptr;
    ListNode* push_back(ListNode* temp)
    {
        ListNode* next = temp->next;
        if (head == nullptr)
            head = tail = temp;
        else
        {
            tail->next = temp;
            tail = temp;
        }
        temp->next = nullptr;
        return next;
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) 
    {
        
        while (list1 != nullptr && list2 != nullptr)
        {
            if (list1->val >= list2->val)
                list2=push_back(list2);
            else
                list1=push_back(list1);
        }
        if (list1 != nullptr)
        {
            if (head != nullptr)
                tail->next = list1;
            else
                head = list1;
        }
            
        if (list2 != nullptr)
            if (head != nullptr)
                tail->next = list2;
            else
                head = list2;
        return head;
    }
};