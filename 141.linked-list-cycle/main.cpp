class Solution {
public:
    bool hasCycle(ListNode* head) 
    {
        vector<ListNode*>position;
        while (head!=NULL)
        {
            for (ListNode* i : position)
            {
                if (i == head)
                    return true;
            }
            position.push_back(head);
            head = head->next;
        }
        return false;
    }
};