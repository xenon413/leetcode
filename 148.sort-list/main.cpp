 class Solution {
 public:
     ListNode* sortList(ListNode* head)
     {
         if (head == nullptr)return head;
         vector<int>vec;
         ListNode* temp = head;
         while (temp != nullptr)
         {
             vec.push_back(temp->val);
             temp = temp->next;
         }
         sort(vec.begin(), vec.end());
         temp = head;
         for (int i : vec)
         {
             temp->val = i;
             temp=temp->next;
         }
         return head;
     }
 };