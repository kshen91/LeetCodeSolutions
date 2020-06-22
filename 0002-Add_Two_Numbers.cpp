/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode *dummyHead = new ListNode();
      ListNode *tmp = dummyHead;
      bool bCarry = false;
      int nextVal = 0;

      while (l1 != nullptr && l2 != nullptr) {
        nextVal = l1->val + l2->val;
        if (nextVal >= 10) {
          nextVal -= 10;
          bCarry = true;
        }
        ListNode *nextNode = new ListNode(nextVal);
        tmp->next = nextNode;

        tmp = tmp -> next;
        l1 = l1 -> next;
        l2 = l2 -> next;

        if (bCarry) {
          bCarry = false;
          if (l1 != nullptr && l2 != nullptr) {
            l1->val += 1;
          } else {
            ListNode *carryNode = new ListNode(1);
            if (l1 == nullptr) {
              l1 = carryNode;
              continue;
            }
            l2 = carryNode;
          }
        }
      }

      if (l1 == nullptr) {
        tmp -> next = l2;
      } else {
        tmp -> next = l1;
      }

      return dummyHead->next;
    }
};
